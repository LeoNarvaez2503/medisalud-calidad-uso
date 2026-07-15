# Escenario 6: Catálogo de Métricas de Calidad en Uso

Este catálogo presenta el diseño formal de las cinco métricas fundamentales de Calidad en Uso según la norma **ISO/IEC 25022**, adaptadas específicamente a las necesidades críticas y Requerimientos No Funcionales (RNF) del sistema **MediSalud HIS**.

---

## Catálogo de Métricas ISO/IEC 25022

### 1. Completitud de Registro de HCE
* **Nombre de la métrica:** Tasa de completitud del registro clínico.
* **Característica ISO/IEC 25022:** Efectividad.
* **Propósito:** Medir si los médicos logran completar con éxito sus notas de evolución clínica sin cancelaciones o errores que fuercen a reiniciar el proceso.
* **Fórmula:** 
  $$X = \frac{A}{B}$$
  * $A = \text{Notas clínicas guardadas con éxito en producción (completada = 1)}$
  * $B = \text{Intentos totales de registro clínico (abertura del formulario)}$
* **Unidad de medida:** Proporción (0.0 a 1.0).
* **Rango deseado:** $X \ge 0.95$ (95% de completitud mínima esperada).
* **Fuente de datos:** Tabla `logs_hce.csv`, evento de guardado exitoso vs evento de carga de formulario.
* **Interpretación:** Valores por debajo del 95% indican alta fricción de usabilidad (campos complejos, timeouts, etc.) o pérdida accidental de datos durante el guardado.

### 2. Tiempo Promedio de Registro de HCE (Eficiencia)
* **Nombre de la métrica:** Tiempo de tarea del registro clínico.
* **Característica ISO/IEC 25022:** Eficiencia.
* **Propósito:** Medir el esfuerzo temporal promedio de los médicos al registrar la evolución de un paciente, contrastando contra el **RNF-01**.
* **Fórmula:**
  $$X = \frac{\sum_{i=1}^{n} t_i}{n}$$
  * $t_i = \text{Tiempo empleado en segundos para la nota } i$
  * $n = \text{Número total de notas clínicas guardadas con éxito}$
* **Unidad de medida:** Segundos (s).
* **Rango deseado:** $X \le 8.0\text{ s}$ (Promedio menor o igual a 8 segundos).
* **Fuente de datos:** Marcas de tiempo de inicio y fin en `logs_hce.csv`.
* **Interpretación:** Promedios superiores a 8 segundos confirman quejas de lentitud clínica.
* **Métrica asociada RNF-01 (P90):** Porcentaje de notas registradas en $\le 8$ segundos. Deseado $\ge 90\%$.

### 3. Índice de Satisfacción del Usuario (CSAT)
* **Nombre de la métrica:** Nivel de satisfacción de usuario con la tarea.
* **Característica ISO/IEC 25022:** Satisfacción.
* **Propósito:** Evaluar cuantitativamente la percepción subjetiva de utilidad, confianza y fluidez de los usuarios reales.
* **Fórmula:**
  $$X = \frac{\sum_{i=1}^{m} \text{Puntaje}_i}{5 \times m}$$
  * $\text{Puntaje}_i = \text{Respuesta a la pregunta CSAT (escala 1 a 5) del usuario } i$
  * $m = \text{Número de usuarios encuestados}$
* **Unidad de medida:** Proporción (0.0 a 1.0) normalizada.
* **Rango deseado:** $X \ge 0.80$ (Equivalente a una calificación CSAT promedio de 4.0 sobre 5.0).
* **Fuente de datos:** Encuestas post-tarea (`encuesta_satisfaccion.csv`).
* **Interpretación:** Puntuaciones inferiores a 0.80 reflejan malestar y rechazo al cambio por parte del personal de salud o frustración del paciente.

### 4. Tasa de Errores de Facturación (Libertad de Riesgo)
* **Nombre de la métrica:** Incidencia de cobros duplicados o incorrectos.
* **Característica ISO/IEC 25022:** Libertad de Riesgo (Riesgos Económicos).
* **Propósito:** Cuantificar el porcentaje de transacciones que generan reclamos financieros directos del paciente o la aseguradora, contrastando contra el **RNF-03**.
* **Fórmula:**
  $$X = \frac{\text{Facturas con error registradas en el periodo}}{\text{Total de transacciones de facturación procesadas}}$$
* **Unidad de medida:** Proporción.
* **Rango deseado:** $X \le 0.01$ (Tasa de error menor o igual a 1% de las transacciones del mes).
* **Fuente de datos:** Dataset de incidentes (`incidentes_2025.csv`) clasificados en el módulo de Facturación / Libertad de Riesgo.
* **Interpretación:** Un indicador superior al 1% demuestra problemas de sincronía con pasarelas de pago o inconsistencias de base de datos transaccionales, impactando el flujo de caja.

### 5. Consistencia de Eficiencia entre Sedes (Cobertura de Contexto)
* **Nombre de la métrica:** Índice de consistencia operativa multisede.
* **Característica ISO/IEC 25022:** Cobertura de Contexto.
* **Propósito:** Determinar si el sistema ofrece un rendimiento temporal homogéneo a través de los diversos entornos geográficos e infraestructuras locales de la red.
* **Fórmula:**
  $$X = \frac{\text{Tiempo promedio de registro HCE en la sede más rápida}}{\text{Tiempo promedio de registro HCE en la sede más lenta}}$$
* **Unidad de medida:** Proporción (0.0 a 1.0).
* **Rango deseado:** $X \ge 0.85$ (Diferencia de eficiencia geográfica no mayor al 15%).
* **Fuente de datos:** Agrupación por sede de la columna `tiempo_segundos` de `logs_hce.csv`.
* **Interpretación:** Un índice menor a 0.85 indica que el rendimiento del sistema está fuertemente influenciado por factores del entorno local (ancho de banda regional, servidores locales de imágenes DICOM deficientes, etc.), revelando problemas de cobertura.
