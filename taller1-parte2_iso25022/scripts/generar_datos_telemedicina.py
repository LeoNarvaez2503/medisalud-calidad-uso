"""
Reto Final Integrador — Generador de datos sinteticos de Telemedicina 2.0
Simula sesiones de teleconsulta para el modulo de Telemedicina de MediSalud HIS.
"""
from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "data" / "logs_telemedicina.csv"

random.seed(2025)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
DISPOSITIVOS = ["Web", "App Android", "App iOS"]
TIPOS_CONEXION = ["WiFi", "4G", "3G", "Fibra"]
ESPECIALIDADES = ["Medicina General", "Pediatria", "Cardiologia", "Dermatologia", "Psicologia"]


def generar_filas(total_dias: int = 10) -> list[dict[str, object]]:
    filas: list[dict[str, object]] = []
    sesion_id = 1
    fecha_inicio = datetime(2025, 11, 3, 7, 0, 0)

    for dia in range(total_dias):
        fecha_dia = fecha_inicio + timedelta(days=dia)
        for sede in SEDES:
            # Mas teleconsultas en ciudades grandes
            n_sesiones = 35 if sede in ("Quito", "Guayaquil") else 18
            for _ in range(n_sesiones):
                hora = random.randint(8, 19)
                minuto = random.randint(0, 59)
                timestamp = fecha_dia.replace(hour=hora, minute=minuto)

                dispositivo = random.choice(DISPOSITIVOS)
                tipo_conexion = random.choice(TIPOS_CONEXION)
                especialidad = random.choice(ESPECIALIDADES)

                paciente_id = f"PAC-{sede[:3].upper()}-{random.randint(1, 500):04d}"
                medico_id = f"MED-{sede[:3].upper()}-{random.randint(1, 12):02d}"

                # Duracion esperada: 15-30 minutos
                duracion_min = max(1, round(random.gauss(22, 8), 1))

                # Probabilidad de completar depende de conexion y dispositivo
                prob_completar = 0.95
                if tipo_conexion == "3G":
                    prob_completar -= 0.15
                if tipo_conexion == "4G":
                    prob_completar -= 0.05
                if dispositivo in ("App Android", "App iOS"):
                    prob_completar -= 0.03

                completada = random.random() < prob_completar

                # Si no completo, registrar motivo
                if not completada:
                    motivo_abandono = random.choice([
                        "Caida de conexion",
                        "Error de audio/video",
                        "Timeout de sesion",
                        "Paciente abandono",
                        "Error de autenticacion",
                    ])
                else:
                    motivo_abandono = ""

                # Satisfaccion del paciente (1-5), peor si no se completo
                if completada:
                    satisfaccion = min(5, max(1, round(random.gauss(4.0, 0.8))))
                else:
                    satisfaccion = min(5, max(1, round(random.gauss(2.0, 0.7))))

                # Datos del paciente expuestos brevemente (riesgo de privacidad)
                incidente_privacidad = random.random() < 0.008  # 0.8% de sesiones

                filas.append({
                    "sesion_id": sesion_id,
                    "timestamp": timestamp.isoformat(),
                    "sede": sede,
                    "paciente_id": paciente_id,
                    "medico_id": medico_id,
                    "especialidad": especialidad,
                    "dispositivo": dispositivo,
                    "tipo_conexion": tipo_conexion,
                    "duracion_minutos": duracion_min,
                    "completada": int(completada),
                    "motivo_abandono": motivo_abandono,
                    "satisfaccion_paciente": satisfaccion,
                    "incidente_privacidad": int(incidente_privacidad),
                })
                sesion_id += 1

    return filas


def main() -> None:
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    filas = generar_filas()

    with SALIDA.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        writer.writeheader()
        writer.writerows(filas)

    completadas = sum(1 for f in filas if f["completada"])
    print(f"Se generaron {len(filas)} sesiones de telemedicina en {SALIDA.relative_to(ROOT)}")
    print(f"  Completadas: {completadas} ({completadas/len(filas)*100:.1f}%)")
    print(f"  Abandonadas: {len(filas) - completadas}")


if __name__ == "__main__":
    main()
