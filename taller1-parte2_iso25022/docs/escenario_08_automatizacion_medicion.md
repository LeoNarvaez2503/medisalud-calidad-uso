# Escenario 8: Automatización de la Medición

Este escenario presenta el diseño, la implementación y la ejecución del pipeline automatizado en Python para calcular periódicamente las métricas de Calidad en Uso de **MediSalud HIS**.

---

## 1. Arquitectura del Pipeline

El pipeline de medición automatizada se diseñó con una estructura modular en tres fases:

```
[ Datos Crudos (.csv) ] 
       │
       ▼ (Fase 1: ETL y Validación)
[ validar_datos.py ] 
       │
       ▼ (Fase 2: Motor de Cálculo)
[ metricas_iso25022.py ] ───► [ tests/test_metricas_iso25022.py ]
       │
       ▼ (Fase 3: Publicación y Consumo)
[ exportar_reporte.py ] ───► [ dashboards/indicadores.json ]
```

### Componentes del Repositorio
* **`generar_logs_hce.py` / `generar_encuesta_satisfaccion.py` / `convertir_incidentes_markdown.py`:** Generadores sintéticos y extractores que preparan los datasets simulando la realidad hospitalaria de MediSalud.
* **`validar_datos.py`:** Módulo de validación de calidad de datos que analiza duplicidad, nulos y consistencia física de rangos.
* **`metricas_iso25022.py`:** El motor principal de la norma que lee los datasets, calcula las fórmulas definidas para las cinco características ISO/IEC 25022 y contrasta los resultados con los umbrales de los Requerimientos No Funcionales.
* **`exportar_reporte.py`:** Orquestador de salida que ejecuta el cálculo y exporta un documento JSON consolidado para los dashboards.
* **`tests/test_metricas_iso25022.py`:** Módulo de pruebas unitarias (`unittest`) que valida la integridad matemática del motor sobre conjuntos de prueba mínimos.

---

## 2. Resultados Ejecutados en el Entorno Virtual

Se ejecutó el pipeline completo a través del script principal, obteniendo el siguiente reporte oficial:

| Característica ISO/IEC 25022 | Nombre de la Métrica | Valor Calculado | Unidad | Rango / Umbral | Estado |
|:---|:---|:---:|:---:|:---:|:---:|
| **Efectividad** | Completitud de registro de HCE | **0.9651** | Proporción | $\ge 0.95$ | **CUMPLE** |
| **Eficiencia** | Tiempo promedio de registro de HCE | **7.43** | Segundos | $\le 8.0\text{ s}$ | **CUMPLE** |
| **Eficiencia (RNF-01)** | Notas registradas en $\le 8\text{ s}$ | **0.6787** | Proporción | $\ge 0.90$ | **NO CUMPLE** |
| **Satisfacción** | Índice de satisfacción CSAT normalizado | **0.7227** | Proporción (0-1) | $\ge 0.80$ | **NO CUMPLE** |
| **Libertad de Riesgo** | Tasa de errores de facturación (riesgo económico) | **0.0301** | Proporción | $\le 0.01$ | **NO CUMPLE** |
| **Cobertura de Contexto** | Consistencia de eficiencia entre sedes | **0.9801** | Proporción | $\ge 0.85$ | **CUMPLE** |

---

## 3. Integración Continua (CI/CD) con GitHub Actions

Para asegurar la ejecución semanal del pipeline y evitar que el cálculo de métricas sea un esfuerzo manual, se implementó el workflow `.github/workflows/medicion_calidad.yml`. 

### Configuración del Workflow
* **Disparadores (Triggers):**
  * Ejecución programada cron: cada lunes a las 06:00 UTC.
  * Disparador manual: `workflow_dispatch` para pruebas y auditorías ad-hoc.
* **Pasos del Trabajo:**
  1. Descarga del código fuente mediante `checkout`.
  2. Inicialización de Python 3.11.
  3. Instalación de dependencias básicas (`pandas` y `numpy`).
  4. Ejecución del pipeline de datos y cálculo de métricas.
  5. Verificación de calidad mediante la ejecución del suite de pruebas unitarias (`unittest`).
  6. Publicación del archivo de salida `indicadores.json` como un artefacto de compilación.

---

## Conclusiones
La automatización permite a la Gerencia de Calidad disponer de evidencia actualizada cada lunes. El pipeline automatizado no solo reduce el esfuerzo operativo, sino que asegura que la red hospitalaria tome decisiones basadas en mediciones matemáticas robustas y no en la percepción de uptime de los servidores.
