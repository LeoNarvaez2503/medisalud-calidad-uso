# Escenario 2: Clasificación de Incidentes - ISO/IEC 25022

Este documento presenta la clasificación y el análisis técnico de los 3,000 incidentes reportados en el sistema **MediSalud HIS** durante el año 2025. Las incidencias han sido analizadas y catalogadas bajo las cinco (5) características principales de la norma **ISO/IEC 25022 (Calidad en Uso)**.

---

## 1. Resumen de Clasificación del Dataset

La ejecución del script de procesamiento de datos (`scripts/clasificar_incidentes.py`) sobre los 3,000 registros arrojó la siguiente distribución de incidentes por característica de Calidad en Uso:

| Característica ISO/IEC 25022 | Cantidad de Incidentes | Porcentaje (%) | Impacto en el Ecosistema |
| :--- | :---: | :---: | :--- |
| **Efectividad** | 1,493 | 49.77% | Fallas funcionales generales que impiden completar tareas. |
| **Libertad de Riesgo** | 721 | 24.03% | Incidentes de alto riesgo clínico (salud) o financiero (facturación). |
| **Eficiencia** | 323 | 10.77% | Latencias y retrasos que degradan el tiempo de operación. |
| **Satisfacción** | 280 | 9.33% | Problemas de usabilidad, frustración de usuario y mala calidad visual/de audio. |
| **Cobertura de Contexto** | 183 | 6.10% | Limitaciones del sistema bajo dispositivos o condiciones específicas. |
| **Total** | **3,000** | **100.00%** | |

---

## 2. Tabla 2.2: Clasificación Detallada de Incidentes (Muestra Representativa)

A continuación, se detalla una muestra representativa con justificaciones técnicas exhaustivas que correlacionan los incidentes con los **Requerimientos No Funcionales (RNF)** prioritarios del sistema:

| ID Incidente | Módulo | Descripción de la Queja / Incidente | Característica Asignada | RNF Relacionado | Justificación Técnica de Clasificación |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **1210** | HCE | Historial de alergias no carga al abrir la ficha del paciente | **Libertad de Riesgo** (Salud y Seguridad) | *Seguridad Clínica* | **Crítico para la salud:** La omisión de las alergias del paciente durante la consulta médica introduce un peligro inminente de shock anafiláctico o reacciones adversas graves al recetar fármacos. Representa una falla en la mitigación de riesgos para la salud humana. |
| **3980** | HCE | Receta electronica se genera con la dosis incorrecta tras guardar | **Libertad de Riesgo** (Salud y Seguridad) | *Seguridad Clínica* | **Riesgo farmacológico directo:** Guardar dosificaciones distintas a las prescritas por el médico puede provocar sobredosis, toxicidad severa o ineficacia del tratamiento, amenazando directamente la integridad física del paciente. |
| **2020** | Facturación | El sistema no reconoce el convenio con la aseguradora | **Libertad de Riesgo** (Riesgo Económico) | **RNF-03** (Errores de Facturación) | **Impacto financiero y legal:** Al no reconocer el convenio, se cobra el monto completo de forma indebida o se frena el servicio. Esto expone al hospital a glosas, pérdidas económicas por no cobro de coaseguros o demandas legales por cobros indebidos. |
| **14** (ejemplo) | Facturación | Factura duplicada al reintentar pago | **Libertad de Riesgo** (Riesgo Económico) | **RNF-03** (Errores de Facturación) | **Transacción errónea:** Viola el límite de transacciones fallidas de facturación (< 1%). Genera cobros bancarios repetidos que afectan directamente la liquidez del paciente y comprometen la reputación y confianza comercial del hospital. |
| **1134** | Imagenología | Tiempo de carga de estudios de imagen supera los 18s | **Eficiencia** (Comportamiento Temporal) | *Eficiencia Operativa* | **Consumo de recursos de tiempo:** La demora de 18 segundos en el visor DICOM para cargar radiografías ralentiza el flujo clínico del especialista, impidiendo diagnosticar con agilidad y consumir tiempo laboral excesivo en la espera del sistema. |
| **73** (ejemplo) | HCE | Nota de evolucion tarda 10s en guardarse | **Eficiencia** (Comportamiento Temporal) | **RNF-01** (Latencia HCE) | **Violación de latencia máxima:** El RNF-01 exige que el registro clínico no supere los 8 segundos en el 90% de los casos. Una latencia de 10 segundos representa una ineficiencia en el rendimiento temporal que ralentiza la consulta del médico. |
| **2017** | Portal Citas | Formulario confuso, abandono de registro antes de completar la cita | **Satisfacción** (Usabilidad y Confianza) | **RNF-02** (Pasos del Portal) | **Fricción cognitiva y abandono:** Una interfaz confusa atenta contra el placer de uso y la comodidad. El abandono de la reserva antes de completarla demuestra que el sistema no genera confianza ni facilidad, frustrando la meta del usuario. |
| **3262** | Telemedicina | Audio desincronizado durante la teleconsulta | **Satisfacción** (Placer / Usabilidad) | **RNF-05** (Disponibilidad de llamada) | **Mala experiencia de servicio:** Aunque la llamada no se caiga por completo, la falta de sincronización del audio degrada severamente la comunicación interactiva y la percepción de calidad del paciente y el médico, reduciendo la satisfacción de uso. |
| **3846** (ejemplo) | HCE | El sistema no permite adjuntar imagenes de heridas desde la tablet | **Cobertura de Contexto** (Especificidad de Hardware) | *Flexibilidad de Dispositivo* | **Limitación en contexto físico móvil:** El sistema falla al interactuar con el hardware de cámaras de tablets usadas por enfermería en rondas. Es una deficiencia de Calidad en Uso al no dar cobertura efectiva a un contexto operativo móvil específico del hospital. |
| **166** (ejemplo) | Portal Citas | Boton de confirmar cita no responde en dispositivos moviles | **Cobertura de Contexto** (Entorno de Software/Pantalla) | *Portabilidad* | **Incompatibilidad móvil:** La funcionalidad opera correctamente en web de escritorio pero falla en el navegador de smartphones, limitando el uso del sistema bajo el contexto de dispositivos personales del paciente. |
| **1075** (ejemplo) | HCE | Orden medica no se sincroniza con el modulo de farmacia | **Efectividad** (Precisión y Completitud) | *Integración Funcional* | **Falla funcional de integración:** Impide que la prescripción médica llegue a farmacia de manera completa y precisa. La tarea clínica de recetar queda trunca y requiere intervención manual, reduciendo la efectividad operacional del sistema. |
| **1509** | Portal Citas | El sistema no envia la confirmacion por correo electronico | **Efectividad** (Completitud Funcional) | *Funcionalidad* | **Incompletitud en el resultado de la tarea:** El proceso de agendamiento se realiza pero el sistema falla en disparar el comprobante electrónico. Al no cerrarse el flujo con precisión, el usuario carece de confirmación de su cita médica. |
| **2416** | HCE | Signos vitales registrados por enfermeria no aparecen en la HCE del medico | **Efectividad** (Precisión y Sincronización) | *Integración de Datos* | **Inconsistencia de datos:** La falla de sincronización interna del HIS impide que la información registrada por enfermería esté disponible para el médico tratante, impidiendo que la HCE sea una fuente precisa de información en tiempo real. |
