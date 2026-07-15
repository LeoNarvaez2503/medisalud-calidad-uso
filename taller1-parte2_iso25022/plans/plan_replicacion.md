# Plan de Replicacion del Proyecto (MediSalud Ecuador - Taller ISO/IEC 25022)

Este plan de implementacion describe la secuencia de pasos tecnicos necesarios para replicar y reconstruir de principio a fin el entorno, los conjuntos de datos, los pipelines de calculo de metricas y los dashboards graficos de calidad en uso, partiendo unicamente de los scripts de codigo y las fuentes de especificaciones iniciales.

---

## Prerrequisitos y Configuracion Inicial

Para replicar este proyecto, se requiere contar con un entorno local que disponga de:
* **Sistema Operativo:** Windows, macOS o GNU/Linux.
* **Interprete de Python:** Version 3.11 o superior.
* **Sistema de control de versiones:** Git.

### 1. Clonar u Organizar la Estructura de Trabajo
Cree un directorio de trabajo limpio para la Parte 2 y situe los scripts fuentes en las rutas correspondientes:
```bash
mkdir -p medisalud-calidad-uso/taller1-parte2_iso25022/scripts
mkdir -p medisalud-calidad-uso/taller1-parte2_iso25022/tests
mkdir -p medisalud-calidad-uso/taller1-parte2_iso25022/docs
mkdir -p medisalud-calidad-uso/taller1-parte2_iso25022/reportes
```

### 2. Configurar el Entorno Virtual de Python
Se recomienda el uso de un entorno virtual aislado para evitar colisiones de dependencias:
```bash
cd medisalud-calidad-uso/taller1-parte2_iso25022

# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate
# Activar en macOS / Linux
source venv/bin/activate

# Actualizar gestor de paquetes pip
python -m pip install --upgrade pip
```

### 3. Instalar Dependencias
Instale los paquetes requeridos para el analisis de datos, visualizacion matematica y pruebas unitarias:
```bash
pip install pandas numpy matplotlib
```

---

## Fase de Ejecucion y Generacion de Datos (Paso a Paso)

Siga el orden secuencial estricto para evitar errores de referencias a archivos faltantes:

### Paso 1: Copiar el archivo origen de incidentes
Asegurese de copiar el archivo `clasificacion_incidentes.md` (que contiene la clasificacion inicial realizada en el taller) al directorio raiz de `taller1-parte2_iso25022/` para que pueda ser parseado.

### Paso 2: Ejecucion de scripts generadores
Genere los conjuntos de datos de logs clinicos HCE, encuestas CSAT de satisfaccion y convierta la tabla Markdown a formato CSV estructurado:
```bash
# Convertir incidentes clasificados en Markdown a CSV estructurado
python scripts/convertir_incidentes_markdown.py

# Generar logs de interaccion de historia clinica HCE
python scripts/generar_logs_hce.py

# Generar respuestas a encuestas de satisfaccion del cliente (CSAT)
python scripts/generar_encuesta_satisfaccion.py
```
*Evidencia:* Se crearan los archivos `logs_hce.csv`, `encuesta_satisfaccion.csv` e `incidentes_2025.csv` en el directorio `data/`.

### Paso 3: Validacion formal de datos
Ejecute la verificacion de calidad del dato para descartar duplicados, nulos y valores fuera de rango fisico:
```bash
python scripts/validar_datos.py
```
*Resultado esperado:* La salida en consola debe confirmar 0 valores nulos y 0 duplicados en los identificadores principales.

### Paso 4: Ejecucion del motor de metricas del HIS
Calcule los indicadores de calidad en uso de MediSalud HIS y exportelos en formato JSON para el consumo visual:
```bash
# Calcular y mostrar las metricas de calidad en uso en la consola
python scripts/metricas_iso25022.py

# Exportar las metricas calculadas a JSON para dashboards
python scripts/exportar_reporte.py
```
*Evidencia:* Se generara el archivo `dashboards/indicadores.json`.

### Paso 5: Generacion del Dashboard Visual
Genere las 7 visualizaciones graficas del dashboard de calidad en formato PNG:
```bash
python scripts/generar_dashboard.py
```
*Evidencia:* Se generaran los archivos `.png` en la carpeta `dashboards/` (Semaforo de metricas, Perfil de radar, Eficiencia por sede, CSAT por rol/sede, Histograma y Pico vs Valle).

### Paso 6: Ejecucion del Reto Final de Telemedicina 2.0
Corra la simulacion de teleconsultas virtuales y calcule sus metricas especificas de finalizacion, calidad de red 3G/4G y riesgos de privacidad:
```bash
# Generar logs transaccionales de teleconsulta
python scripts/generar_datos_telemedicina.py

# Calcular metricas de telemedicina e incidentes
python scripts/metricas_telemedicina.py
```
*Evidencia:* Se crearan `data/logs_telemedicina.csv` y `dashboards/indicadores_telemedicina.json`.

### Paso 7: Ejecucion de Pruebas Unitarias
Ejecute la validacion de correctitud matematica de las funciones del motor principal:
```bash
python -m unittest tests.test_metricas_iso25022 -v
```
*Resultado esperado:* `test_metrica_eficiencia_promedia_tiempos ... ok`

---

## Despliegue en Integracion Continua (GitHub Actions)

Para mantener los reportes actualizados automaticamente sin intervencion manual:
1. Cree la carpeta de workflows en su repositorio Git:
   ```bash
   mkdir -p .github/workflows
   ```
2. Mueva el archivo `medicion_calidad.yml` a la ruta `.github/workflows/medicion_calidad.yml`.
3. Suba los cambios a su repositorio remoto en GitHub:
   ```bash
   git add .
   git commit -m "docs: add pipeline CI/CD de medicion"
   git push origin main
   ```
4. El pipeline se ejecutara de forma automatica cada lunes a las 06:00 UTC, o bien de manera manual desde la pestaña **Actions** en su repositorio de GitHub.
