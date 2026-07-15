# Escenario 4: Identificación de Atributos de Calidad en Uso

Este documento detalla la identificación de atributos de calidad en uso basados en el modelo **Usuario-Tarea-Contexto** de la norma ISO/IEC 25022 para los procesos más críticos del sistema **MediSalud HIS**.

---

## Fichas de Usuario-Tarea-Contexto

### 1. Proceso: Atención Médica y Registro de Historia Clínica (HCE)
* **Usuario Primario:** Médico tratante (640 usuarios activos).
* **Tarea Representativa:** Registrar una nota de evolución clínica completa de un paciente en consulta externa, incluyendo diagnóstico, órdenes, recetas y firma electrónica.
* **Contexto de Uso:** Consulta externa presencial en el Hospital General de Quito en horas pico (10:00–12:00), con alta concurrencia de médicos conectados de forma simultánea a la red LAN interna del hospital.
* **Atributos de Calidad en Uso:**
  * **Tiempo de Tarea (Eficiencia):** Tiempo en segundos transcurrido desde que se abre el formulario de nota clínica hasta que se guarda correctamente. (Umbral RNF-01: 90% en $\le$ 8 segundos).
  * **Completitud de la Tarea (Efectividad):** Proporción de notas guardadas sin errores ni pérdida de campos obligatorios.
  * **Percepción de Fluidez (Satisfacción):** Calificación del médico sobre la agilidad de la interacción física con la interfaz de guardado.
  * **Integridad Clínica (Libertad de Riesgo):** Mitigación del riesgo de registrar información en el paciente equivocado o de no visualizar alertas de alergias/interacciones.

### 2. Proceso: Agendamiento de Citas Médicas
* **Usuario Primario:** Paciente (38,000+ usuarios registrados en el portal).
* **Tarea Representativa:** Agendar una cita médica de especialidad seleccionando médico, fecha, horario y confirmando la reserva en el portal.
* **Contexto de Uso:** Acceso web desde un dispositivo móvil o navegador de escritorio, utilizando redes móviles comerciales (4G/5G) o conexiones domésticas, típicamente en horario nocturno (18:00–21:00) en ciudades con mayor volumen de pacientes (Guayaquil y Quito).
* **Atributos de Calidad en Uso:**
  * **Tasa de éxito de la tarea (Efectividad):** Proporción de intentos de reserva que finalizan con una cita confirmada en la agenda del especialista.
  * **Tiempo y pasos de agendamiento (Eficiencia):** Número de pasos necesarios para confirmar la cita (Umbral RNF-02: máximo 3 pasos) y tiempo de sesión empleado.
  * **Confianza percibida (Satisfacción):** Sensación de seguridad de que el turno quedó efectivamente asignado sin sobre-reserva o conflicto.
  * **Consistencia de interfaz (Cobertura de Contexto):** Capacidad del flujo para operar de manera uniforme entre el portal web (React) y la app móvil (Flutter).

### 3. Proceso: Facturación de Consulta con Seguro Médico
* **Usuario Primario:** Personal de admisión y facturación (210 usuarios activos).
* **Tarea Representativa:** Generar la pre-factura de una consulta externa, aplicar el deducible/coaseguro de la aseguradora del paciente, procesar el pago del copago y emitir el comprobante electrónico válido.
* **Contexto de Uso:** Computadora de escritorio en la recepción física del centro de salud al cierre de la jornada (17:00–19:00), integrándose con la pasarela de pagos web de las aseguradoras privadas y el sistema financiero de base de datos SQL Server heredado.
* **Atributos de Calidad en Uso:**
  * **Tasa de errores económicos (Libertad de Riesgo):** Proporción de facturas emitidas que presentan duplicidades o montos incorrectos (Umbral RNF-03: menos del 1%).
  * **Exactitud de la liquidación (Efectividad):** Grado en que el descuento por póliza de seguro se aplica correctamente en la primera transacción sin intervención manual.
  * **Tiempo de atención por paciente (Eficiencia):** Segundos empleados para facturar y despachar al paciente de la ventanilla de atención.

---

## Conclusiones
El análisis revela que la calidad en uso es un concepto multidimensional y contextual:
1. Una nota de HCE rápida (eficiente) pero guardada en el paciente incorrecto (incompleta/ineficaz) representa un fallo crítico de calidad.
2. La definición previa de los perfiles de usuario, tareas clave y los contextos extremos de carga (horas pico) nos dota del marco empírico necesario para construir métricas objetivas y reproducibles.
