#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
import re

def clasificar_incidente(modulo, descripcion):
    desc = descripcion.lower().strip()
    
    # 1. EFICIENCIA (Efficiency)
    # Tiempos de respuesta lentos, latencias y demoras de rendimiento
    if (re.search(r"tarda \d+s en guardarse", desc) or
        re.search(r"tiempo de carga.*supera los \d+s", desc) or
        re.search(r"tiempo de respuesta.*supera los \d+s", desc) or
        re.search(r"retraso de \d+s", desc) or
        re.search(r"tiempo de espera.*supera los \d+s", desc) or
        re.search(r"tiempo de generacion.*supera los \d+ minutos", desc) or
        re.search(r"retraso de \d+ minutos", desc) or
        re.search(r"llega con retraso de \d+s", desc)):
        
        if "nota de evolucion" in desc:
            return "Eficiencia", "El tiempo de guardado supera los 8 segundos tolerables, violando directamente el requerimiento no funcional RNF-01 de rendimiento del sistema para notas clínicas."
        elif "reporte mensual" in desc:
            return "Eficiencia", "Demoras severas en la generación de reportes mensuales de inteligencia de negocio, penalizando la eficiencia en el tiempo de procesamiento y toma de decisiones."
        elif "estudios de imagen" in desc or "rayos x" in desc:
            return "Eficiencia", "La lentitud en la carga y transferencia de archivos DICOM pesados degrada la eficiencia del flujo de trabajo clínico en imagenología."
        elif "pago con tarjeta" in desc:
            return "Eficiencia", "El procesamiento lento del cobro con tarjeta retrasa el flujo de caja y la atención administrativa de admisión."
        elif "ficha clinica" in desc:
            return "Eficiencia", "La latencia en horas pico para abrir la ficha clínica perjudica la productividad del médico durante la consulta."
        else:
            return "Eficiencia", "El sistema presenta tiempos de respuesta elevados que consumen recursos de tiempo innecesarios, degradando la eficiencia del usuario en sus tareas."

    # 2. LIBERTAD DE RIESGO (Freedom from Risk)
    # Mitigación de riesgos de salud (paciente) y riesgos económicos (facturación/negocio)
    
    # RIESGOS DE SALUD Y SEGURIDAD CLÍNICA
    if ("alergia" in desc or 
        "dosis incorrecta" in desc or 
        "datos de otro paciente" in desc or 
        "interaccion medicamentosa" in desc or 
        "duplicado de historia clinica" in desc or 
        ("duplicidad de codigos" in desc and "farmaco" in desc) or
        "medicamento controlado" in desc or
        "vencimiento de lote" in desc):
        
        if "alergia" in desc:
            return "Libertad de Riesgo", "Falla crítica que expone la seguridad del paciente al omitir información vital de alergias, con un alto riesgo de shock anafiláctico o mala praxis."
        elif "dosis incorrecta" in desc:
            return "Libertad de Riesgo", "Riesgo extremo de salud para el paciente al guardar dosis farmacológicas erróneas en la receta electrónica, pudiendo causar sobredosis o inefectividad clínica."
        elif "datos de otro paciente" in desc:
            return "Libertad de Riesgo", "Fuga de información y violación de la confidencialidad médica (HIPAA/Ley de Protección de Datos), exponiendo datos de otros pacientes."
        elif "interaccion medicamentosa" in desc:
            return "Libertad de Riesgo", "El fallo en el despliegue de alertas de interacción farmacológica pone en riesgo inminente la salud del paciente ante combinaciones letales."
        elif "duplicado de historia clinica" in desc:
            return "Libertad de Riesgo", "Riesgo de seguridad clínica debido a la fragmentación de la información de salud del paciente, lo que puede inducir a diagnósticos y tratamientos erróneos."
        elif "duplicidad de codigos" in desc:
            return "Libertad de Riesgo", "La duplicación de códigos de fármacos introduce un riesgo de dispensación errónea en farmacia, comprometiendo la seguridad terapéutica del paciente."
        elif "medicamento controlado" in desc:
            return "Libertad de Riesgo", "Error en el registro de medicamentos regulados, lo que genera riesgos legales, regulatorios y de seguridad en el control de sustancias psicotrópicas."
        elif "vencimiento de lote" in desc:
            return "Libertad de Riesgo", "Omitir la alerta de vencimiento de lotes farmacéuticos puede llevar a la administración de medicamentos caducados a los pacientes."
        else:
            return "Libertad de Riesgo", "Falla crítica con el potencial de comprometer la salud y seguridad de los pacientes o el cumplimiento legal de la institución."

    # RIESGOS ECONÓMICOS / FINANCIEROS Y COMERCIALES
    if ("factura duplicada" in desc or 
        "doble cobro" in desc or 
        "monto facturado" in desc or 
        "copago" in desc or 
        "aseguradora" in desc or 
        "doble reserva" in desc or 
        "reporte financiero" in desc or 
        "nota de credito no se aplica" in desc or 
        "reembolso aprobado no se refleja" in desc or 
        "bono de consulta" in desc):
        
        if "factura duplicada" in desc or "doble cobro" in desc:
            return "Libertad de Riesgo", "Violación del requerimiento no funcional RNF-03 de facturación; genera cobros indebidos en las tarjetas del cliente, comprometiendo la confianza y el riesgo financiero."
        elif "copago" in desc or "monto facturado" in desc:
            return "Libertad de Riesgo", "Errores en el cálculo del copago de seguros o discrepancias de montos facturados, induciendo a pérdidas financieras o reclamaciones legales."
        elif "aseguradora" in desc:
            return "Libertad de Riesgo", "El no reconocimiento de convenios de aseguradoras genera fricción de cobro y riesgo de pérdidas económicas por servicios no cubiertos correctamente."
        elif "doble reserva" in desc:
            return "Libertad de Riesgo", "Doble agendamiento de un mismo cupo que genera sobreventa de citas, colapso de agenda de especialistas y multas o insatisfacción comercial."
        elif "reporte financiero" in desc:
            return "Libertad de Riesgo", "Discrepancia contable entre reportes directivos y facturación real, afectando las decisiones del negocio y la integridad de las auditorías."
        elif "nota de credito" in desc or "reembolso" in desc:
            return "Libertad de Riesgo", "Fallas en la aplicación de notas de crédito o reembolsos que distorsionan los estados de cuenta, arriesgando multas tributarias e inconformidad legal."
        else:
            return "Libertad de Riesgo", "Inconsistencia financiera en los cobros o transacciones del sistema que infringe las normativas contables y expone al hospital a pérdidas económicas."

    # 3. COBERTURA DE CONTEXTO (Context Coverage)
    # Problemas que ocurren bajo contextos de uso específicos (dispositivos, conectividad, sistemas operativos específicos)
    if ("tablet" in desc or 
        "dispositivos moviles" in desc or "dispositivos móviles" in desc or
        "version desactualizada" in desc or
        "datos moviles" in desc or "datos móviles" in desc or
        "videollamada se corta a los" in desc):
        
        if "tablet" in desc:
            return "Cobertura de Contexto", "El sistema presenta limitaciones de portabilidad y compatibilidad al operar en el contexto físico específico de tablets para adjuntar imágenes de heridas."
        elif "dispositivos moviles" in desc:
            return "Cobertura de Contexto", "Falla de adaptabilidad de la interfaz en el contexto de dispositivos móviles, impidiendo confirmar citas desde pantallas de formatos pequeños."
        elif "version desactualizada" in desc:
            return "Cobertura de Contexto", "Incompatibilidad y falta de robustez del sistema cuando se ejecuta en el contexto de sistemas cliente que no cuentan con la última versión de software."
        elif "datos moviles" in desc:
            return "Cobertura de Contexto", "Consumo excesivo de ancho de banda móvil, lo que restringe el uso eficiente del sistema en redes celulares de datos (fuera de la intranet del hospital)."
        elif "videollamada se corta" in desc:
            return "Cobertura de Contexto", "Falta de resiliencia del canal de comunicación ante variaciones en la conectividad del usuario, interrumpiendo la sesión de teleconsulta en producción."
        else:
            return "Cobertura de Contexto", "Falla de operación que se manifiesta bajo condiciones específicas de hardware, software cliente o red, limitando el alcance operativo de la aplicación."

    # 4. SATISFACCIÓN (Satisfaction)
    # Fricciones de usabilidad, frustración de usuario, problemas de percepción visual/auditiva
    if ("biometria" in desc or 
        "confuso" in desc or 
        "sesion expira antes" in desc or 
        "no logra agendar tras" in desc or 
        "calidad de video muy baja" in desc or 
        "audio desincronizado" in desc or 
        "perdida de calidad en las imagenes" in desc or 
        "bloquea la dispensacion sin mostrar el motivo" in desc):
        
        if "biometria" in desc:
            return "Satisfacción", "La inestabilidad en el inicio biométrico genera frustración y reduce la confianza y comodidad del usuario al acceder al aplicativo móvil."
        elif "confuso" in desc:
            return "Satisfacción", "Diseño de interfaz de usuario confuso que provoca el abandono del registro, afectando la métrica de satisfacción y facilidad de uso percibida."
        elif "no logra agendar" in desc:
            return "Satisfacción", "Incapacidad del usuario de lograr su meta tras múltiples intentos, violando el RNF-02 y provocando un alto nivel de frustración."
        elif "sesion expira" in desc:
            return "Satisfacción", "Mala experiencia de usuario que interrumpe de forma prematura el proceso de compra/agendamiento, forzando a repetir pasos."
        elif "video muy baja" in desc or "audio desincronizado" in desc:
            return "Satisfacción", "Mala experiencia sensorial e interactiva durante la teleconsulta que impacta el RNF-05 y la percepción de calidad del servicio."
        elif "perdida de calidad en las imagenes" in desc:
            return "Satisfacción", "Degradación visual que afecta la comodidad y confianza de los médicos al visualizar estudios clínicos desde la app móvil."
        elif "sin mostrar el motivo" in desc:
            return "Satisfacción", "La falta de mensajes informativos claros y feedback del sistema incrementa la incertidumbre y frustración del operario farmacéutico."
        else:
            return "Satisfacción", "Problemas de diseño y usabilidad que atentan contra la comodidad, confianza y placer de uso del sistema MediSalud HIS."

    # 5. EFECTIVIDAD (Effectiveness)
    # Errores funcionales generales que impiden la consecución correcta de tareas del usuario sin riesgos inminentes
    justificacion_efectividad = f"Falla de funcionalidad en el módulo {modulo} que impide al usuario completar sus tareas de manera precisa y completa."
    
    if "no envia la confirmacion" in desc:
        justificacion_efectividad = "Falla funcional que impide completar la tarea de confirmación de cita al paciente por canal de correo electrónico."
    elif "no se sincroniza" in desc or "no se sincronizan" in desc:
        justificacion_efectividad = "Error de integración funcional que impide la sincronización y actualización del registro médico entre módulos del HIS."
    elif "cierra inesperadamente" in desc:
        justificacion_efectividad = "Interrupción abrupta del sistema que impide que el usuario termine el registro de datos, reduciendo la efectividad operativa."
    elif "no responde" in desc:
        justificacion_efectividad = "Bloqueo de botón interactivo que interrumpe la efectividad del proceso de confirmación de tareas."
    elif "no permite" in desc:
        justificacion_efectividad = "Restricción de funcionalidad que impide al usuario realizar una acción requerida para completar su tarea."
    elif "no se actualiza" in desc or "no refleja" in desc:
        justificacion_efectividad = "Inconsistencia en la actualización de datos que impide la visualización correcta de información operativa reciente."
    elif "falla de forma intermitente" in desc or "falla" in desc:
        justificacion_efectividad = "Falla intermitente en las exportaciones o ejecuciones de procesos del sistema que reduce la fiabilidad de las operaciones."
    
    return "Efectividad", justificacion_efectividad

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(base_dir, '..', 'Dataset', 'incidentes_2025_iso_25022.csv')
    output_path = os.path.join(base_dir, 'data', 'incidentes_2025.csv')
    
    print(f"Reading original dataset from: {os.path.abspath(input_path)}")
    print(f"Writing classified dataset to: {os.path.abspath(output_path)}")
    
    if not os.path.exists(input_path):
        # Fallback to workspace absolute path just in case
        input_path = '/home/meatpuppets/Escritorio/University/Taller-3/Dataset/incidentes_2025_iso_25022.csv'
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
    # Create target directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(input_path, mode='r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['caracteristica_iso_25022', 'justificacion_tecnica']
        
        records = []
        counts = {}
        for row in reader:
            caract, just = clasificar_incidente(row['modulo'], row['descripcion'])
            row['caracteristica_iso_25022'] = caract
            row['justificacion_tecnica'] = just
            records.append(row)
            counts[caract] = counts.get(caract, 0) + 1
            
    with open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        
    print("\nClassification summary:")
    for caract, cnt in sorted(counts.items()):
        pct = (cnt / len(records)) * 100
        print(f"- {caract}: {cnt} incidents ({pct:.2f}%)")
        
    print(f"\nProcessing complete. Processed {len(records)} incidents.")

if __name__ == "__main__":
    main()
