# Explicación del Taller: Medición de Calidad en Uso (Parte 2)

Este documento explica de forma detallada los objetivos, la estructura y el flujo de ejecución de la **Parte 2** del taller de Aseguramiento de la Calidad del Software, centrado en la norma **ISO/IEC 25022 (Calidad en Uso)** para la Red Hospitalaria **MediSalud Ecuador**.

---

## 🎯 Objetivos de la Parte 2

La segunda parte del taller traslada la teoría del modelo de calidad en uso a la práctica técnica real, logrando:
1. **Identificar atributos** de calidad basados en el modelo *Usuario-Tarea-Contexto* (Escenario 4).
2. **Priorizar y mapear** procesos de negocio según impacto y frecuencia de uso (Escenario 5).
3. **Diseñar métricas formales** que den soporte a los Requerimientos No Funcionales (RNF) (Escenario 6).
4. **Recolectar y validar datos** técnicos y de usabilidad simulados en producción (Escenario 7).
5. **Automatizar el pipeline de medición** en Python e integrarlo con flujos de Integración Continua (Escenario 8).
6. **Construir tableros visuales de indicadores (KPIs)** con semáforos, perfiles de radar y análisis temporal (Escenario 9).
7. **Analizar la causa raíz** de métricas críticas incumplidas empleando los *5 Por Qué* (Escenario 10).
8. **Planificar la mejora continua** y proponer la gobernanza técnica del software bajo el ciclo PDCA (Escenarios 11 y 12).
9. **Resolver el Reto Final Integrador** aplicando todo el flujo de medición al nuevo módulo de **Telemedicina 2.0**.

---

## 📂 Arquitectura de Archivos y Componentes

La solución técnica está distribuida en las siguientes carpetas dentro del directorio `taller1-parte2_iso25022/`:

```text
taller1-parte2_iso25022/
├── .github/workflows/
│   └── medicion_calidad.yml       # Integración Continua en GitHub Actions (Escenario 8)
├── dashboards/
│   ├── csat_por_rol.png           # CSAT agrupado por rol de usuario (Escenario 9)
│   ├── csat_por_sede.png          # CSAT promedio por sede (Escenario 9)
│   ├── eficiencia_por_sede.png    # Eficiencia temporal de HCE por sede (Escenario 9)
│   ├── histograma_tiempos_hce.png # Histograma de latencias del guardado HCE (Escenario 9)
│   ├── indicadores.json           # Salida del pipeline principal en formato JSON (Escenario 8)
│   ├── indicadores_telemedicina.json # Salida del reto final en JSON (Reto Final)
│   ├── pico_vs_valle.png          # Comparativo de latencia HCE en horas pico vs valle (Escenario 9)
│   ├── radar_iso25022.png         # Perfil de araña de las 5 dimensiones (Escenario 9)
│   └── semaforo_metricas.png      # Estado semáforo de cumplimiento vs umbrales (Escenario 9)
├── data/                          # Carpeta con los conjuntos de datos CSV generados
│   ├── encuesta_satisfaccion.csv  # 150 encuestas con puntuación CSAT (Escenario 7)
│   ├── incidentes_2025.csv        # 3,000 incidentes clasificados bajo ISO 25022 (Escenario 2-7)
│   ├── logs_hce.csv               # 3,150 registros de latencias en HCE (Escenario 7)
│   └── logs_telemedicina.csv      # 1,240 registros de teleconsultas (Reto Final)
├── docs/                          # Documentación detallada en Markdown de cada entregable
│   ├── escenario_04_atributos_calidad_uso.md
│   ├── escenario_05_mapeo_priorizacion.md
│   ├── escenario_06_catalogo_metricas.md
│   ├── escenario_07_obtencion_datos.md
│   ├── escenario_08_automatizacion_medicion.md
│   ├── escenario_09_indicadores_kpi.md
│   ├── escenario_10_interpretacion_resultados.md
│   └── reto_final_telemedicina.md
├── latex/                         # Código fuente y compilaciones en LaTeX de los informes
├── pdfs/                          # Reportes exportados a formato PDF listos para entrega
├── reportes/
│   ├── informe_ejecutivo.md       # Escenario 11: Resumen ejecutivo para directores
│   └── plan_mejora_continua.md    # Escenario 12: Ciclo PDCA y gobernanza
├── scripts/                       # Módulos y utilidades de Python
│   ├── convertir_incidentes_markdown.py # Convierte incidentes Markdown de la Parte 1 a CSV
│   ├── exportar_reporte.py        # Orquesta y exporta las métricas principales a JSON
│   ├── generar_dashboard.py       # Generador de las 7 visualizaciones del dashboard
│   ├── generar_datos_telemedicina.py    # Generador sintético de teleconsultas
│   ├── generar_encuesta_satisfaccion.py # Generador de encuestas CSAT
│   ├── generar_logs_hce.py        # Generador de registros de latencia en HCE
│   ├── generar_pdfs_latex.py      # Utilidad para automatizar la compilación de LaTeX a PDF
│   ├── metricas_iso25022.py       # Motor principal de cálculo para MediSalud HIS
│   ├── metricas_telemedicina.py   # Motor de cálculo para Telemedicina 2.0
│   └── validar_datos.py           # Validador de calidad del dato (nulos, rangos)
└── tests/
    └── test_metricas_iso25022.py  # Pruebas unitarias en Python
```

---

## ⚙️ Flujo de Ejecución del Taller

Para reproducir o actualizar los resultados de la Parte 2 del taller, se sigue este pipeline secuencial:

### Paso 1: Generación y Validación de Datos (Escenario 7)
El primer paso genera los datasets simulados con los que operan los motores de cálculo:
```bash
# Extrae y genera los 3,000 incidentes en formato CSV
python scripts/convertir_incidentes_markdown.py

# Genera los logs de latencia HCE y respuestas CSAT
python scripts/generar_logs_hce.py
python scripts/generar_encuesta_satisfaccion.py

# Ejecuta el script de validación para asegurar la consistencia física
python scripts/validar_datos.py
```

### Paso 2: Cálculo Automatizado de Métricas (Escenario 8)
Se procesan las métricas principales y se exportan para la capa de presentación:
```bash
# Calcula métricas principales del HIS
python scripts/metricas_iso25022.py

# Exporta los indicadores a un archivo JSON para consumo visual
python scripts/exportar_reporte.py
```

### Paso 3: Generación del Dashboard Visual (Escenario 9)
Se renderizan los indicadores gráficos para reportes ejecutivos:
```bash
# Genera las visualizaciones PNG en dashboards/
python scripts/generar_dashboard.py
```

### Paso 4: Ejecución del Módulo de Telemedicina 2.0 (Reto Final)
Se repite el pipeline para el caso de estudio de telemedicina:
```bash
# Genera los datos sintéticos de teleconsulta
python scripts/generar_datos_telemedicina.py

# Calcula los indicadores de telemedicina y exporta a JSON
python scripts/metricas_telemedicina.py
```

### Paso 5: Verificación del Entorno y Pruebas Unitarias
Se ejecutan los tests unitarios para verificar la integridad del código:
```bash
python -m unittest tests.test_metricas_iso25022 -v
```

---

## 📈 Conclusiones Clave del Análisis de Calidad en Uso
* **El promedio enmascara problemas:** Aunque la latencia de HCE promedio es de 7.43s, el **32.13% supera el límite de 8s (incumpliendo el RNF-01)**, especialmente en horas pico de consulta externa ($10:00-12:00$).
* **Fallas del sistema causan insatisfacción:** La baja satisfacción de médicos y pacientes (CSAT normalizado de 72.27%) está fuertemente correlacionada con demoras de guardado y micro-caídas.
* **El módulo financiero requiere segregación:** La tasa de error del 3.01% en facturación (incumpliendo el RNF-03) se debe a colisiones de base de datos compartida entre cierres de ventanilla e informes contables síncronos en SQL Server heredado.
* **Telemedicina expone retos de conectividad y privacidad:** En el Reto Final se evidenció que la cobertura de red (3G) disminuye la tasa de éxito al 88% y genera fallos temporales de tokens (exponiendo datos personales a un riesgo de privacidad de 0.65%).
