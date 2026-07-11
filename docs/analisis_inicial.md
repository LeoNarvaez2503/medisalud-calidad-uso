# Escenario 1: Análisis Inicial - MediSalud HIS

Este documento presenta el análisis inicial sobre el caso de estudio de la red hospitalaria **MediSalud** y su sistema de información hospitalaria **MediSalud HIS**. El objetivo es comprender los procesos más críticos, identificar a los usuarios afectados y diagnosticar el estado de la evidencia sobre la calidad de su software.

---

## 1. Procesos Críticos del Negocio

De los seis procesos de negocio identificados en la red hospitalaria MediSalud, se han seleccionado los **tres (3) más críticos** debido a su impacto directo sobre la seguridad del paciente, la continuidad de la atención clínica y la salud financiera de la institución:

### A. Atención Médica y Registro de Historia Clínica (HCE)
*   **Descripción:** Es el núcleo operativo de la red hospitalaria. Permite a los médicos y enfermeros registrar notas de evolución, consultar antecedentes clínicos, verificar alertas de alergias y emitir recetas electrónicas.
*   **Criticidad:** Un fallo o retraso en este proceso compromete directamente la toma de decisiones clínicas y puede poner en riesgo la vida del paciente (por ejemplo, si no se despliega una alerta de alergia o de interacción medicamentosa, o si se genera una receta con una dosis incorrecta).

### B. Prescripción y Dispensación de Medicamentos (Farmacia e Inventario)
*   **Descripción:** Integra la emisión de recetas electrónicas en la HCE con la preparación y entrega física del fármaco en el módulo de Farmacia, controlando el inventario clínico.
*   **Criticidad:** Errores de sincronización entre la orden del médico y la farmacia, duplicidades en presentaciones de fármacos o la falta de visualización de vencimiento de lotes impiden que el paciente reciba el tratamiento correcto a tiempo. Además, fallos en este flujo generan pérdidas económicas e inconsistencias graves en el stock clínico de medicamentos controlados.

### C. Agendamiento y Admisión de Pacientes (Portal del Paciente / Portal Citas)
*   **Descripción:** Representa la puerta de entrada de los usuarios a los servicios médicos de MediSalud, abarcando desde que el paciente reserva un cupo web/móvil hasta su recepción física (admisión) en la sede.
*   **Selección:** La insatisfacción del cliente comienza aquí. Errores como reservas duplicadas, tiempos de espera que superan los límites tolerables o caídas del portal bloquean el flujo de ingresos de la red hospitalaria y reducen drásicamente la capacidad operativa de los especialistas médicos.

---

## 2. Usuarios Afectados

El impacto de las deficiencias de calidad en el sistema MediSalud HIS repercute de distintas formas sobre tres grupos clave de usuarios:

| Grupo de Usuarios | Impacto Clínico y Operativo | Principales Síntomas Experimentados |
| :--- | :--- | :--- |
| **Personal Médico y de Enfermería** | Operan bajo alta presión. La lentitud del sistema o la pérdida de información degradan la calidad del diagnóstico y aumentan el tiempo dedicado a tareas administrativas en lugar del cuidado del paciente. | - Demoras en el guardado de notas de evolución (incumplimiento del RNF-01).<br>- Ausencia de alertas críticas de alergias y medicamentos en la HCE.<br>- Imposibilidad de validar firmas electrónicas para cerrar consultas. |
| **Pacientes** | Son los destinatarios finales del servicio de salud. Experimentan frustración ante barreras tecnológicas, lo que daña su confianza en la institución. | - Sesiones expiradas y bloqueos en el portal de citas (violación del RNF-02).<br>- Caídas en videoconsultas de telemedicina (violación del RNF-05).<br>- Cobros y facturas duplicadas en sus estados de cuenta. |
| **Personal de Admisión, Farmacia y Facturación** | Encargados del flujo administrativo y el control financiero. El fallo del sistema ralentiza los procesos de salida y auditoría. | - Caídas del módulo de facturación durante los cierres de caja.<br>- Discrepancias entre stock físico e inventario registrado en el sistema.<br>- Retrasos en el procesamiento de tarjetas de crédito y aprobación de reembolsos. |

---

## 3. Evidencia sobre la Calidad en MediSalud

### Evidencia Disponible
Actualmente, MediSalud cuenta con una base empírica sólida representada en el conjunto de datos de incidentes registrados en el periodo 2025 (`incidentes_2025.csv`). Esta evidencia contiene:
1.  **3,000 registros de incidentes reales** clasificados por ID, fecha, módulo del sistema, descripción detallada del error, rol del usuario que reportó y la sede hospitalaria respectiva (Quito, Guayaquil, Manta, Ambato, Cuenca).
2.  **Identificación de cuellos de botella geográficos y por módulo**, permitiendo mapear qué sedes y qué funcionalidades del HIS (como HCE o Portal de Citas) acumulan mayor fricción de usuario.
3.  **Registro cualitativo de la experiencia de usuario**, capturando quejas específicas que reflejan directamente brechas en la usabilidad, latencia y disponibilidad en producción.

### Evidencia Faltante
A pesar de contar con el registro de incidentes, MediSalud carece de datos técnicos cuantitativos de infraestructura y desarrollo para tomar acciones correctivas de raíz. Falta recolectar:
*   **Métricas de Infraestructura y Servidor:** Trazabilidad de latencia de red, uso de CPU y memoria de servidores de bases de datos, y rendimiento de los endpoints de la API en el momento en que ocurren los retrasos (indispensable para resolver la lentitud en el guardado de notas e imágenes DICOM).
*   **Logs y Trazas de Interacción de Usuario (Clickstream):** Datos que registren el flujo exacto de pasos que sigue un usuario en el portal de citas (necesario para verificar científicamente el cumplimiento del **RNF-02** de máximo 3 pasos).
*   **Métricas de Calidad Interna (Código Estático):** Análisis de deuda técnica, duplicación de código, complejidad ciclomática de los componentes del HIS y porcentaje de cobertura de pruebas unitarias/integración (para evaluar mantenibilidad bajo el modelo SQuaRE).
*   **Auditorías Clínicas y Financieras Formales:** Registros oficiales de incidentes de seguridad del paciente (eventos adversos por dosis erróneas) y auditorías contables para contrastar con el **RNF-03** (tasa de error de facturación < 1%).
