import asyncio
import random
import time
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import pika

from .database import Base, engine, get_db
from .models import Cita, IncidenteLog, Paciente, Receta

# Initialize DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediSalud HIS API Gateway & Microservices Sim")

# Enable CORS for React SPA
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Seed database on start
def seed_db():
    db = next(get_db())
    if db.query(Paciente).count() == 0:
        pacientes = [
            Paciente(nombre="Juan Carlos Pérez", documento="1798364810", historia_clinica="HC-2025-001", alergias="Penicilina, Sulfas"),
            Paciente(nombre="María Alejandra López", documento="0987654321", historia_clinica="HC-2025-002", alergias="Aspirina, AINEs"),
            Paciente(nombre="Carlos Andrés García", documento="1102938475", historia_clinica="HC-2025-003", alergias="Látex"),
            Paciente(nombre="Ana Lucía Martínez", documento="1847294029", historia_clinica="HC-2025-004", alergias="Ninguna"),
        ]
        db.add_all(pacientes)
        db.commit()
        print("Database seeded with sample patients.")
seed_db()

# Pydantic Schemas
class NotaClinicaRequest(BaseModel):
    paciente_id: int
    diagnostico: str
    nota_evolucion: str
    rol_usuario: str
    sede: str

class RecetaRequest(BaseModel):
    paciente_id: int
    medicamento: str
    dosis: str
    indicaciones: str
    rol_usuario: str
    sede: str

class CitaRequest(BaseModel):
    paciente_id: int
    especialidad: str
    medico: str
    fecha_hora: str
    rol_usuario: str
    sede: str
    intentos: int = 1

class PagoRequest(BaseModel):
    paciente_id: int
    monto: float
    tarjeta: str
    reintento: bool = False
    rol_usuario: str
    sede: str

class TeleConsultaRequest(BaseModel):
    paciente_id: int
    medico: str
    rol_usuario: str
    sede: str

# Helper to log quality incidents in Postgres
def log_incidente(db: Session, modulo: str, descripcion: str, rol: str, sede: str, caracteristica: str, justificacion: str, rnf: str = None):
    log = IncidenteLog(
        modulo=modulo,
        descripcion=descripcion,
        rol_usuario=rol,
        sede=sede,
        caracteristica_iso_25022=caracteristica,
        justificacion_tecnica=justificacion,
        violacion_rnf=rnf
    )
    db.add(log)
    db.commit()
    return log

# RabbitMQ Helper to simulate async messaging for Lab/Imaging
def send_rabbitmq_message(queue_name: str, message: str):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq', socket_timeout=2))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        connection.close()
        return True
    except Exception as e:
        print(f"RabbitMQ connection failed: {e}")
        return False

# REST ENDPOINTS

@app.get("/api/pacientes", response_model=List[dict])
def get_pacientes(db: Session = Depends(get_db)):
    pacientes = db.query(Paciente).all()
    return [{"id": p.id, "nombre": p.nombre, "documento": p.documento, "historia_clinica": p.historia_clinica, "alergias": p.alergias} for p in pacientes]

@app.get("/api/pacientes/{paciente_id}/alergias")
def get_alergias(paciente_id: int, simulate_error: bool = False, rol_usuario: str = "Medico", sede: str = "Quito", db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
        
    if simulate_error:
        # Simulate Allergy Load failure (Libertad de Riesgo - Salud)
        log_incidente(
            db=db,
            modulo="HCE",
            descripcion="Historial de alergias no carga al abrir la ficha del paciente",
            rol=rol_usuario,
            sede=sede,
            caracteristica="Libertad de Riesgo",
            justificacion="Falla crítica que expone la seguridad del paciente al omitir información vital de alergias en HCE, con un alto riesgo de shock anafiláctico o mala praxis en consulta.",
            rnf="Seguridad Clínica"
        )
        return {"alergias": "Error al cargar. Reintente.", "error": True}
        
    return {"alergias": paciente.alergias, "error": False}

@app.post("/api/hce/nota")
async def guardar_nota(req: NotaClinicaRequest, simulate_error: bool = False, db: Session = Depends(get_db)):
    start_time = time.time()
    
    if simulate_error:
        # Deliberately sleep for 10-12 seconds to violate RNF-01
        delay = random.choice([10, 11, 12, 14, 15])
        await asyncio.sleep(delay)
        elapsed = time.time() - start_time
        
        log_incidente(
            db=db,
            modulo="HCE",
            descripcion=f"Nota de evolucion tarda {int(elapsed)}s en guardarse",
            rol=req.rol_usuario,
            sede=req.sede,
            caracteristica="Eficiencia",
            justificacion="El tiempo de guardado supera los 8 segundos especificados, violando directamente el requerimiento no funcional RNF-01 de rendimiento del sistema para notas clínicas.",
            rnf="RNF-01"
        )
        return {"status": "Guardado con retraso", "tiempo_segundos": elapsed, "violacion_rnf": True}
    
    # Normal behavior (takes < 1s)
    await asyncio.sleep(0.5)
    return {"status": "Guardado exitosamente", "tiempo_segundos": time.time() - start_time, "violacion_rnf": False}

@app.post("/api/hce/receta")
def guardar_receta(req: RecetaRequest, simulate_error: bool = False, db: Session = Depends(get_db)):
    dosis_final = req.dosis
    
    if simulate_error:
        # Modify the dosage to a dangerous level after saving (Libertad de Riesgo - Salud)
        dosis_final = "5000 mg (DOSIS INCORRECTA MODIFICADA POR EL SISTEMA)"
        receta = Receta(paciente_id=req.paciente_id, medicamento=req.medicamento, dosis=dosis_final, indicaciones=req.indicaciones)
        db.add(receta)
        db.commit()
        
        log_incidente(
            db=db,
            modulo="HCE",
            descripcion="Receta electronica se genera con la dosis incorrecta tras guardar",
            rol=req.rol_usuario,
            sede=req.sede,
            caracteristica="Libertad de Riesgo",
            justificacion="Riesgo extremo de salud para el paciente al guardar dosis farmacológicas erróneas en la receta electrónica, pudiendo causar sobredosis o inefectividad clínica.",
            rnf="Seguridad Clínica"
        )
        return {"receta_id": receta.id, "medicamento": receta.medicamento, "dosis": receta.dosis, "error": True}

    receta = Receta(paciente_id=req.paciente_id, medicamento=req.medicamento, dosis=dosis_final, indicaciones=req.indicaciones)
    db.add(receta)
    db.commit()
    return {"receta_id": receta.id, "medicamento": receta.medicamento, "dosis": receta.dosis, "error": False}

@app.post("/api/citas/agendar")
def agendar_cita(req: CitaRequest, simulate_error: bool = False, db: Session = Depends(get_db)):
    if simulate_error:
        # 1. Simulate confused form and high number of attempts (RNF-02 / Usability / Satisfaction)
        if req.intentos >= 4:
            log_incidente(
                db=db,
                modulo="Portal Citas",
                descripcion=f"Usuario no logra agendar tras {req.intentos} intentos",
                rol=req.rol_usuario,
                sede=req.sede,
                caracteristica="Satisfacción",
                justificacion="Incapacidad del usuario de lograr su meta de reserva tras múltiples intentos, violando el RNF-02 de portal de citas y provocando un alto nivel de frustración.",
                rnf="RNF-02"
            )
            # 2. Also simulate double booking when it finally succeeds
            cita = Cita(paciente_id=req.paciente_id, especialidad=req.especialidad, medico=req.medico, fecha_hora=req.fecha_hora, sede=req.sede, estado="Reservado (Duplicado)")
            db.add(cita)
            db.commit()
            
            log_incidente(
                db=db,
                modulo="Portal Citas",
                descripcion="Doble reserva de un mismo cupo por dos pacientes distintos",
                rol=req.rol_usuario,
                sede=req.sede,
                caracteristica="Libertad de Riesgo",
                justificacion="Doble agendamiento de un mismo cupo que genera sobreventa de citas, colapso de agenda de especialistas y multas o insatisfacción comercial.",
                rnf="Riesgo de Negocio"
            )
            return {"status": "Cita agendada con conflicto de doble reserva", "intentos": req.intentos, "error_duplicidad": True}
        
        # Simula abandono/confusión en pasos previos
        log_incidente(
            db=db,
            modulo="Portal Citas",
            descripcion="Formulario confuso, abandono de registro antes de completar la cita",
            rol=req.rol_usuario,
            sede=req.sede,
            caracteristica="Satisfacción",
            justificacion="Diseño de interfaz de usuario confuso que provoca el abandono del registro, afectando la métrica de satisfacción y facilidad de uso percibida (violando el RNF-02).",
            rnf="RNF-02"
        )
        return {"status": "Intento fallido: Formulario confuso / Sesión expirada", "intentos": req.intentos, "error_pasos": True}

    # Normal booking
    cita = Cita(paciente_id=req.paciente_id, especialidad=req.especialidad, medico=req.medico, fecha_hora=req.fecha_hora, sede=req.sede)
    db.add(cita)
    db.commit()
    return {"status": "Cita agendada exitosamente", "cita_id": cita.id, "intentos": req.intentos, "error": False}

@app.post("/api/facturacion/pagar")
def procesar_pago(req: PagoRequest, simulate_error: bool = False, db: Session = Depends(get_db)):
    if simulate_error:
        # Simulate delay and double charging (Libertad de Riesgo - Financiero, violating RNF-03)
        if req.reintento:
            log_incidente(
                db=db,
                modulo="Facturacion",
                descripcion="Factura duplicada al reintentar pago",
                rol=req.rol_usuario,
                sede=req.sede,
                caracteristica="Libertad de Riesgo",
                justificacion="Violación del requerimiento no funcional RNF-03 de facturación; genera cobros y facturas duplicadas en la tarjeta del cliente al reintentar un pago demorado.",
                rnf="RNF-03"
            )
            return {"status": "Cobro procesado (DUPLICADO DETECTADO)", "monto": req.monto, "doble_cobro": True}
            
        # Simula retraso de procesamiento del primer intento
        log_incidente(
            db=db,
            modulo="Facturacion",
            descripcion="Retraso de 15s al procesar el pago con tarjeta de credito",
            rol=req.rol_usuario,
            sede=req.sede,
            caracteristica="Eficiencia",
            justificacion="Retraso excesivo en el procesamiento de pasarelas de pago, induciendo al usuario a reintentar y provocar dobles cobros.",
            rnf="RNF-03"
        )
        return {"status": "Pago en proceso (demorando)...", "reintento_requerido": True}
        
    return {"status": "Pago procesado exitosamente", "monto": req.monto, "doble_cobro": False}

@app.post("/api/telemedicina/iniciar")
def iniciar_telemedicina(req: TeleConsultaRequest, simulate_error: bool = False, db: Session = Depends(get_db)):
    if simulate_error:
        # Simulate video and connection drop / desync (Satisfacción & Efectividad, violating RNF-05)
        log_incidente(
            db=db,
            modulo="Telemedicina",
            descripcion="Videollamada se corta a los 2 minutos",
            rol=req.rol_usuario,
            sede=req.sede,
            caracteristica="Cobertura de Contexto",
            justificacion="Falta de resiliencia del canal ante variaciones de red, interrumpiendo la sesión de teleconsulta en producción y violando el RNF-05.",
            rnf="RNF-05"
        )
        log_incidente(
            db=db,
            modulo="Telemedicina",
            descripcion="Audio desincronizado durante la teleconsulta",
            rol=req.rol_usuario,
            sede=req.sede,
            caracteristica="Satisfacción",
            justificacion="La mala calidad de sincronización en videollamadas genera frustración e incomodidad clínica para el médico y el paciente.",
            rnf="RNF-05"
        )
        return {"status": "Conexión Inestable", "error_conexion": True}
        
    return {"status": "Teleconsulta iniciada con éxito", "error_conexion": False}

# Context Coverage Endpoint (specific devices / browsers)
@app.post("/api/auditoria/contexto")
def log_contexto_error(modulo: str, error_type: str, device: str, rol: str, sede: str, db: Session = Depends(get_db)):
    if error_type == "tablet":
        desc = "El sistema no permite adjuntar imagenes de heridas desde la tablet"
        just = "El sistema presenta limitaciones de compatibilidad al operar en el contexto específico de tablets de enfermería."
    else:
        desc = "Boton de confirmar cita no responde en dispositivos moviles"
        just = "Falla de adaptabilidad en pantallas móviles, bloqueando al usuario en este contexto de hardware."
        
    log_incidente(
        db=db,
        modulo=modulo,
        descripcion=desc,
        rol=rol,
        sede=sede,
        caracteristica="Cobertura de Contexto",
        justificacion=just,
        rnf="Portabilidad"
    )
    return {"status": "Logueado"}

# Lab / Image Integration (RabbitMQ logs)
@app.post("/api/integraciones/orden")
def enviar_orden(modulo: str, tipo: str, simulate_error: bool = False, rol: str = "Enfermeria", sede: str = "Quito", db: Session = Depends(get_db)):
    msg = f"Orden de {tipo} generada"
    success = False
    
    if not simulate_error:
        success = send_rabbitmq_message("medi_citas", msg)
        
    if not success or simulate_error:
        desc = "Orden de laboratorio duplicada tras reintentar el envio" if tipo == "Lab" else "El informe radiologico no se adjunta automaticamente a la HCE"
        just = "Error de comunicación asíncrona mediante mensajería RabbitMQ que trunca la integración del flujo de resultados."
        
        log_incidente(
            db=db,
            modulo=modulo,
            descripcion=desc,
            rol=rol,
            sede=sede,
            caracteristica="Efectividad",
            justificacion=just
        )
        return {"status": "Fallo de integración asíncrona", "rabbitmq_status": "OFFLINE", "error": True}
        
    return {"status": "Mensaje enviado a RabbitMQ", "rabbitmq_status": "ONLINE", "error": False}

# Retrieve live audit logs
@app.get("/api/auditoria/logs", response_model=List[dict])
def get_audit_logs(db: Session = Depends(get_db)):
    logs = db.query(IncidenteLog).order_by(IncidenteLog.fecha.desc()).all()
    return [
        {
            "id": l.id,
            "fecha": l.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "modulo": l.modulo,
            "descripcion": l.descripcion,
            "rol_usuario": l.rol_usuario,
            "sede": l.sede,
            "caracteristica_iso_25022": l.caracteristica_iso_25022,
            "justificacion_tecnica": l.justificacion_tecnica,
            "violacion_rnf": l.violacion_rnf
        } for l in logs
    ]

# Stats for Live Dashboard
@app.get("/api/auditoria/stats")
def get_audit_stats(db: Session = Depends(get_db)):
    logs = db.query(IncidenteLog).all()
    total = len(logs)
    
    counts = {}
    modules = {}
    rnf_violations = 0
    
    for l in logs:
        counts[l.caracteristica_iso_25022] = counts.get(l.caracteristica_iso_25022, 0) + 1
        modules[l.modulo] = modules.get(l.modulo, 0) + 1
        if l.violacion_rnf:
            rnf_violations += 1
            
    return {
        "total_incidentes": total,
        "caracteristicas": counts,
        "modulos": modules,
        "violaciones_rnf": rnf_violations
    }
