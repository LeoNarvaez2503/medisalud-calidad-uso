# Guia de Entregables, Resoluciones y Evidencias: Taller Parte 2

Este documento explica de forma detallada que exige la guia del taller (la orden), como se resolvio tecnicamente (la resolucion) y en que archivos o directorios especificos se puede constatar (las evidencias) para cada uno de los escenarios de la Parte 2 (Escenarios 4 al 12 + Reto Final).

---

## Escenario 4: Identificacion de Atributos de Calidad en Uso

### Que dice la orden?
* **Instruccion:** Seleccionar 3 de los 6 procesos criticos de la Red Hospitalaria MediSalud Ecuador y construir fichas tecnicas bajo el modelo **Usuario-Tarea-Contexto**, identificando atributos de calidad en uso (Eficiencia, Efectividad, Satisfaccion, Libertad de Riesgo y Cobertura de Contexto).

### Como se resolvio?
* **Resolucion:** Se seleccionaron los procesos de:
  1. *Atencion medica y registro de HCE* (Medico tratante, guardar nota clinica, consulta externa en hora pico).
  2. *Agendamiento de citas* (Paciente, agendar turno con especialista, portal web/app en red movil).
  3. *Facturacion con seguro medico* (Personal de admision, generar liquidacion y cobro, cierre de jornada en red interna).
* Para cada uno se documentaron las condiciones de entorno de alta concurrencia y los atributos metricos especificos de usabilidad y rendimiento.

### Donde puedo evidenciarlo en el proyecto?
* **Documentacion en Markdown:** [escenario_04_atributos_calidad_uso.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_04_atributos_calidad_uso.md)
* **Codigo LaTeX y Reporte PDF:** [01_escenario_4_atributos_calidad_uso.tex](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/latex/01_escenario_4_atributos_calidad_uso.tex) y su compilado [01_escenario_4_atributos_calidad_uso.pdf](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/pdfs/01_escenario_4_atributos_calidad_uso.pdf).

---

## Escenario 5: Mapeo de Caracteristicas de Calidad

### Que dice la orden?
* **Instruccion:** Elaborar una matriz de doble entrada que vincule las tareas de usuario con las cinco caracteristicas de la norma ISO/IEC 25022, priorizandolas segun su impacto de negocio (alto, medio, bajo) y frecuencia de ejecucion (alta, media, baja) para definir el alcance del programa de calidad.

### Como se resolvio?
* **Resolucion:** Se construyo una matriz de mapeo para 8 tareas de usuario representativas del HIS. Se determino que los procesos prioritarios (Prioridad 1 y 2) para ser evaluados inmediatamente en la Fase 1 son: *HCE, Portal de Citas, Facturacion, Teleconsulta y Dispensacion de Farmacia*, postergando reportes gerenciales y consultas secundarias.

### Donde puedo evidenciarlo en el proyecto?
* **Documentacion en Markdown:** [escenario_05_mapeo_priorizacion.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_05_mapeo_priorizacion.md)
* **Codigo LaTeX y Reporte PDF:** [02_escenario_5_mapeo_priorizacion.tex](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/latex/02_escenario_5_mapeo_priorizacion.tex) y su compilado [02_escenario_5_mapeo_priorizacion.pdf](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/pdfs/02_escenario_5_mapeo_priorizacion.pdf).

---

## Escenario 6: Diseno de Metricas

### Que dice la orden?
* **Instruccion:** Disenar formalmente un catalogo de al menos 5 metricas de Calidad en Uso (una por cada caracteristica de ISO/IEC 25022), documentando nombre, formula matematica, variables, unidad de medida, rango deseado (umbral) y fuentes de datos.

### Como se resolvio?
* **Resolucion:** Se diseno el catalogo de 5 metricas alineado con los RNF de MediSalud:
  1. *Completitud del registro HCE* (Efectividad).
  2. *Tiempo promedio de guardado HCE* (Eficiencia) - alineado al **RNF-01** (<= 8 segundos).
  3. *CSAT normalizado* (Satisfaccion) - umbral >= 0.80.
  4. *Tasa de errores de facturacion* (Libertad de Riesgo) - alineado al **RNF-03** (<= 1%).
  5. *Consistencia de eficiencia entre sedes* (Cobertura de Contexto) - umbral >= 0.85.

### Donde puedo evidenciarlo en el proyecto?
* **Documentacion en Markdown:** [escenario_06_catalogo_metricas.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_06_catalogo_metricas.md)
* **Codigo LaTeX y Reporte PDF:** [03_escenario_6_catalogo_metricas.tex](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/latex/03_escenario_6_catalogo_metricas.tex) y su compilado [03_escenario_6_catalogo_metricas.pdf](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/pdfs/03_escenario_6_catalogo_metricas.pdf).

---

## Escenario 7: Obtencion de Datos

### Que dice la orden?
* **Instruccion:** Desarrollar scripts de generacion de datos para logs HCE con distorsion en horas pico y respuestas CSAT. Validar que no existan valores nulos, duplicados o rangos logicos fuera de limites utilizando Pandas/Python.

### Como se resolvio?
* **Resolucion:** Se crearon y ejecutaron los scripts generadores:
  * [generar_logs_hce.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/generar_logs_hce.py): Crea 3,150 eventos con latencias mayores en horas pico (10:00-12:00).
  * [generar_encuesta_satisfaccion.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/generar_encuesta_satisfaccion.py): Crea 150 respuestas CSAT con sesgo negativo para medicos y pacientes.
  * [convertir_incidentes_markdown.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/convertir_incidentes_markdown.py): Extrae los 3,000 incidentes de la Parte 1 del taller a CSV.
  * [validar_datos.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/validar_datos.py): Comprueba que no haya nulos, duplicados ni latencias imposibles.

### Donde puedo evidenciarlo en el proyecto?
* **Archivos de Datos Generados:** Carpeta [data/](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/data) con los archivos `logs_hce.csv`, `encuesta_satisfaccion.csv` e `incidentes_2025.csv`.
* **Documentacion en Markdown:** [escenario_07_obtencion_datos.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_07_obtencion_datos.md)
* **Codigo LaTeX y Reporte PDF:** [04_escenario_7_obtencion_datos.tex](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/latex/04_escenario_7_obtencion_datos.tex) y su compilado [04_escenario_7_obtencion_datos.pdf](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/pdfs/04_escenario_7_obtencion_datos.pdf).

---

## Escenario 8: Automatizacion de la Medicion

### Que dice la orden?
* **Instruccion:** Construir un pipeline en Python que automatice el calculo de las metricas ISO/IEC 25022, exporte los resultados en JSON y cree un flujo de Integracion Continua (CI/CD) para programar la ejecucion periodica de la medicion.

### Como se resolvio?
* **Resolucion:**
  * Se implemento el motor de calculo [metricas_iso25022.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/metricas_iso25022.py) y el orquestador [exportar_reporte.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/exportar_reporte.py).
  * Se genero la prueba unitaria en [test_metricas_iso25022.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/tests/test_metricas_iso25022.py) para validar la exactitud de las formulas.
  * Se implemento el workflow de GitHub Actions [medicion_calidad.yml](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/.github/workflows/medicion_calidad.yml) para ejecutar el pipeline de datos, calculo y tests cada lunes.

### Donde puedo evidenciarlo en el proyecto?
* **Reporte JSON Exportado:** [indicadores.json](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/dashboards/indicadores.json).
* **Documentacion en Markdown:** [escenario_08_automatizacion_medicion.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_08_automatizacion_medicion.md)
* **Codigo LaTeX y Reporte PDF:** [05_escenario_8_automatizacion_medicion.tex](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/latex/05_escenario_8_automatizacion_medicion.tex) y su compilado [05_escenario_8_automatizacion_medicion.pdf](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/pdfs/05_escenario_8_automatizacion_medicion.pdf).

---

## Escenario 9: Construccion de Indicadores KPI (Dashboard)

### Que dice la orden?
* **Instruccion:** Crear un dashboard visual que represente las metricas a traves de indicadores graficos claros, aplicando principios de diseno y contraste cromatico.

### Como se resolvio?
* **Resolucion:** Se implemento [generar_dashboard.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/generar_dashboard.py), que procesa `indicadores.json` y genera los graficos usando un estilo visual oscuro premium:
  * Semaforo de cumplimiento vs umbral.
  * Perfil radial de arana (Radar chart).
  * Histogramas de distribucion bimodal e histograma de latencias en horas pico vs valle.
  * Eficiencia e insatisfaccion CSAT desglosada por sedes y roles.

### Donde puedo evidenciarlo en el proyecto?
* **Graficos Generados:** Carpeta [dashboards/](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/dashboards) (`semaforo_metricas.png`, `radar_iso25022.png`, `histograma_tiempos_hce.png`, `pico_vs_valle.png`, `csat_por_rol.png`, `csat_por_sede.png`).
* **Documentacion en Markdown:** [escenario_09_indicadores_kpi.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_09_indicadores_kpi.md).

---

## Escenario 10: Interpretacion de Resultados y Causa Raiz

### Que dice la orden?
* **Instruccion:** Analizar criticamente las metricas que no cumplen con los umbrales exigidos, detectando y documentando sus causas tecnicas mediante la tecnica de analisis de los **5 Por Que**.

### Como se resolvio?
* **Resolucion:** Se diagnosticaron las tres metricas con alerta roja:
  1. *Latencia HCE (RNF-01):* Se determino que se debe a bloqueos transaccionales por consultas sincronas al modulo de farmacia durante el guardado.
  2. *Satisfaccion (CSAT):* Expiracion excesiva de tokens y micro-caidas por falta de pool de conexiones.
  3. *Errores de Facturacion (RNF-03):* Congestion por compartir el servidor SQL Server transaccional con reportes analiticos masivos de finanzas.

### Donde puedo evidenciarlo en el proyecto?
* **Documentacion en Markdown:** [escenario_10_interpretacion_resultados.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/escenario_10_interpretacion_resultados.md).

---

## Escenarios 11 y 12: Informe Ejecutivo y Mejora Continua

### Que dice la orden?
* **Instruccion:** Elaborar un informe formal resumido para la Direccion General y trazar un plan de mejora continua bajo el ciclo PDCA (Plan, Do, Check, Act) y gobernanza tecnica.

### Como se resolvio?
* **Resolucion:** Se redactaron los documentos ejecutivos:
  * El informe ejecutivo prioriza un ciclo de estabilizacion de 90 dias enfocado en HCE y facturacion.
  * El plan PDCA asigna responsabilidades a la Gerencia de Calidad (Check), TI (Do/Act) y Direccion Medica (Plan).

### Donde puedo evidenciarlo en el proyecto?
* **Documentos Markdown:** [informe_ejecutivo.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/reportes/informe_ejecutivo.md) y [plan_mejora_continua.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/reportes/plan_mejora_continua.md).
* **Codigo LaTeX y Reporte PDF:** [06_informe_ejecutivo_plan_mejora.tex](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/latex/06_informe_ejecutivo_plan_mejora.tex) y su compilado [06_informe_ejecutivo_plan_mejora.pdf](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/pdfs/06_informe_ejecutivo_plan_mejora.pdf).

---

## Reto Final Integrador: Telemedicina 2.0

### Que dice la orden?
* **Instruccion:** Resolver de manera autonoma e integradora el caso de **Telemedicina 2.0**, definiendo la ficha Usuario-Tarea-Contexto, disenando sus 5 metricas bajo ISO/IEC 25022, implementando sus scripts en Python y analizando sus resultados en produccion.

### Como se resolvio?
* **Resolucion:** 
  * Se implemento el generador [generar_datos_telemedicina.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/generar_datos_telemedicina.py) que simula 1,240 teleconsultas con cortes por tipo de conexion (3G/4G/WiFi) e incidentes de privacidad.
  * Se implemento el motor de calculo [metricas_telemedicina.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/metricas_telemedicina.py).
  * Se diagnosticaron los incumplimientos en *Efectividad (88.31%)* y *Privacidad (0.65%)* proponiendo compresion dinamica adaptativa y WebRTC.

### Donde puedo evidenciarlo en el proyecto?
* **Codigo Python:** [generar_datos_telemedicina.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/generar_datos_telemedicina.py) y [metricas_telemedicina.py](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/scripts/metricas_telemedicina.py).
* **Salida de Datos y JSON:** `data/logs_telemedicina.csv` e [indicadores_telemedicina.json](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/dashboards/indicadores_telemedicina.json).
* **Documentacion en Markdown:** [reto_final_telemedicina.md](file:///c:/Users/Jordan/Desktop/medisalud-calidad-uso/taller1-parte2_iso25022/docs/reto_final_telemedicina.md).
