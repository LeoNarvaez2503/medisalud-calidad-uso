# Escenario 9: Construcción de Indicadores (KPI) y Visualizaciones

Para facilitar la interpretación rápida del estado de calidad de **MediSalud HIS** por parte de directores y jefes de área, se implementó el módulo `generar_dashboard.py`. Este script genera visualizaciones avanzadas basadas en las métricas calculadas, aplicando buenas prácticas de diseño y contraste.

Los gráficos generados se almacenan como imágenes en el directorio `dashboards/` para su incorporación en informes mensuales.

---

## Visualizaciones del Dashboard de Calidad en Uso

### 1. Semáforo General de Métricas (`dashboards/semaforo_metricas.png`)
* **Propósito:** Ofrecer un resumen rápido "Pasa/No Pasa" de las 6 métricas clave de Calidad en Uso.
* **Descripción:** Gráfico de barras horizontales con colores de estado: **verde** para las métricas que superan o igualan el umbral establecido, y **rojo** para aquellas que no lo alcanzan. Los umbrales de referencia se representan como marcadores de diamante naranja.
* **Resultado Visual:** Evidencia visual clara de que, a pesar de que el *Tiempo promedio* y la *Completitud* de la HCE están dentro de los márgenes, tres de las métricas clave (Cumplimiento de RNF-01 de latencia en HCE, Satisfacción CSAT y Errores de Facturación) se encuentran en zona roja de incumplimiento.

### 2. Perfil de Calidad en Uso Radar (`dashboards/radar_iso25022.png`)
* **Propósito:** Mostrar visualmente el equilibrio del sistema en las cinco características de la norma ISO/IEC 25022.
* **Descripción:** Gráfico radial donde cada vértice representa una característica normalizada de 0.0 a 1.0 (en Eficiencia y Libertad de Riesgo se invirtieron o normalizaron los valores para que el extremo exterior siempre represente "mejor calidad").
* **Resultado Visual:** Muestra un polígono distorsionado. La Cobertura de Contexto y la Efectividad están bien balanceadas cerca del borde exterior, mientras que la Satisfacción y la Eficiencia (P90) jalan el polígono hacia el centro, revelando asimetría de calidad.

### 3. Distribución de Latencias en Consulta (`dashboards/histograma_tiempos_hce.png`)
* **Propósito:** Diagnosticar la experiencia temporal real más allá de promedios simples.
* **Descripción:** Histograma de frecuencias de los 3,150 registros de tiempo HCE con una línea de corte discontinua en el límite físico del RNF-01 (8.0 segundos) y una línea continua en la media (7.43 s).
* **Resultado Visual:** Revela una distribución bimodal. La gran mayoría de registros se acumulan en un pico de usabilidad de 5 a 7 segundos, pero existe una cola pesada a la derecha que supera los 8 segundos (llegando hasta 17 segundos), lo que explica que un **32.13% de los casos incumplan el RNF-01**.

### 4. Análisis de Rendimiento Geográfico (`dashboards/eficiencia_por_sede.png`)
* **Propósito:** Evaluar la homogeneidad del desempeño técnico e infraestructura de la red hospitalaria (Cobertura de Contexto).
* **Descripción:** Gráfico de barras verticales por sede hospitalaria, comparando sus tiempos promedios contra el límite de 8s del RNF-01.
* **Resultado Visual:** Demuestra alta consistencia. Todas las sedes (Quito, Guayaquil, Cuenca, Ambato y Manta) mantienen promedios estables de 7.37 a 7.52 segundos. Esto prueba que el problema de lentitud es sistémico (del software o base de datos central) y no se debe a infraestructura de una ciudad en particular.

### 5. Satisfacción CSAT por Sede y Rol (`dashboards/csat_por_sede.png` y `csat_por_rol.png`)
* **Propósito:** Identificar focos geográficos u organizacionales de insatisfacción.
* **Descripción:** Gráficos comparativos de puntajes promedio CSAT (escala 1 a 5) desglosados por ubicación geográfica y rol en el hospital.
* **Resultado Visual:** 
  * Por sede, Guayaquil y Quito muestran los niveles más bajos de satisfacción (promedios de 3.3 y 3.4), correlacionándose directamente con la mayor carga de transacciones y pacientes atendidos.
  * Por rol, los Médicos y los Pacientes son los más insatisfechos (CSAT < 3.5), mientras que el personal administrativo y de farmacia muestra niveles aceptables de aceptación.

### 6. Comportamiento en Horas Críticas (`dashboards/pico_vs_valle.png`)
* **Propósito:** Confirmar científicamente si la lentitud está asociada a picos de concurrencia.
* **Descripción:** Histograma superpuesto comparando la distribución de tiempos en hora valle vs hora pico (10:00–12:00).
* **Resultado Visual:** El histograma confirma un desplazamiento drástico hacia la derecha en horas pico: la media del tiempo de registro clínico sube a **10.5 segundos** (superando el umbral de 8s) debido a degradación de base de datos o APIs bajo carga alta de concurrencia, mientras que en hora valle la experiencia es óptima (media de 6.5s).

---

## Conclusión

Las representaciones gráficas del dashboard permiten pasar del dato abstracto a la evidencia accionable: el sistema HIS es rápido y estable en horas valle, pero colapsa temporalmente bajo concurrencia matutina (horas pico), afectando la satisfacción de médicos y pacientes. Esto guía directamente la priorización técnica de base de datos.
