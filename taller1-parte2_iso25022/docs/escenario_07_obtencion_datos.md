# Escenario 7: Obtención y Validación de Datos

Este escenario detalla el proceso de recolección, generación sintética controlada y validación formal de los tres conjuntos de datos principales que sustentan el programa de medición de Calidad en Uso de **MediSalud HIS**.

---

## 1. Fuentes de Datos de Calidad en Uso

Para alimentar las métricas diseñadas en el Escenario 6, se definieron tres orígenes de datos específicos:

* **Logs de interacción clínica (`data/logs_hce.csv`):**
  * **Uso:** Cálculo de Eficiencia y Efectividad en el registro de HCE.
  * **Campos:** `evento_id` (Identificador único), `timestamp` (Marca temporal ISO-8601), `sede` (Ubicación física), `medico_id` (Identificador del profesional), `tiempo_segundos` (Latencia de registro), `completada` (Bandera binaria: 1 = éxito, 0 = abandono/error).
  * **Tamaño:** 3,150 registros correspondientes a 5 días de consulta externa.
* **Encuestas de Satisfacción CSAT (`data/encuesta_satisfaccion.csv`):**
  * **Uso:** Medición de Satisfacción cualitativa y cuantitativa.
  * **Campos:** `respuesta_id` (Identificador), `sede` (Ubicación), `rol` (Rol de usuario), `puntaje_csat` (Entero de 1 a 5), `comentario` (Texto libre).
  * **Tamaño:** 150 encuestas contestadas tras finalizar tareas críticas.
* **Historial de Incidentes de Producción (`data/incidentes_2025.csv`):**
  * **Uso:** Medición de Libertad de Riesgo (financiero y clínico) e incidentes.
  * **Campos:** `id` (Identificador), `fecha` (Fecha ISO), `modulo` (Módulo del HIS), `descripcion` (Detalle del error), `rol_usuario` (Rol del afectado), `sede` (Ubicación), `caracteristica_iso` (Clasificación ISO/IEC 25022), `rnf_relacionado` (RNF vulnerado), `justificacion` (Sustento de clasificación).
  * **Tamaño:** 3,000 incidentes operativos reales clasificados e integrados.

---

## 2. Reporte de Validación de Datos (Pandas/Python)

Antes de proceder a la automatización de la medición, se ejecutó el validador `validar_datos.py` para asegurar que los datos crudos estén libres de inconsistencias. Los resultados obtenidos son:

### A. Resultados `data/logs_hce.csv`
* **Total de Filas:** 3,150.
* **Valores Nulos:** 0 en todas las columnas.
* **Duplicados (`evento_id`):** 0 duplicados encontrados.
* **Errores de Rango Temporal:** 0 registros con tiempos negativos o superiores al límite físico razonable de 120 segundos. Rango real: $[1.5\text{ s}, 17.31\text{ s}]$.
* **Errores en Bandera Binaria:** 0 registros con valores de `completada` distintos a 0 o 1.
* **Tiempo Promedio de Nota:** 7.43 segundos.

### B. Resultados `data/encuesta_satisfaccion.csv`
* **Total de Filas:** 150.
* **Valores Nulos:** 0 en todas las columnas.
* **Duplicados (`respuesta_id`):** 0 duplicados.
* **Errores de Rango CSAT:** 0 registros con puntajes fuera del rango $[1, 5]$.
* **Puntaje CSAT Promedio:** 3.61 / 5.0.

### C. Resultados `data/incidentes_2025.csv`
* **Total de Filas:** 3,000.
* **Valores Nulos:** 0 en todas las columnas.
* **Duplicados (`id`):** 0 duplicados.

---

## Conclusión

El proceso de control de calidad del dato fue exitoso. La ausencia de valores nulos, la integridad referencial y la inexistencia de anomalías en los rangos garantizan que las métricas calculadas reflejan con precisión matemática y empírica el estado de operación de **MediSalud HIS**.
