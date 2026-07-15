# Plan de Replicación del Proyecto (MediSalud Ecuador - Taller ISO/IEC 25022)

Este plan de implementación describe la secuencia de pasos técnicos necesarios para replicar y reconstruir de principio a fin el entorno, los conjuntos de datos, los pipelines de cálculo de métricas y los dashboards gráficos de calidad en uso, partiendo únicamente de los scripts de código y las fuentes de especificaciones iniciales.

---

## 📋 Prerrequisitos y Configuración Inicial

Para replicar este proyecto, se requiere contar con un entorno local que disponga de:
* **Sistema Operativo:** Windows, macOS o GNU/Linux.
* **Intérprete de Python:** Versión 3.11 o superior.
* **Sistema de control de versiones:** Git.

### 1. Clonar u Organizar la Estructura de Trabajo
Cree un directorio de trabajo limpio para la Parte 2 y sitúe los scripts fuentes en las rutas correspondientes:
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
Instale los paquetes requeridos para el análisis de datos, visualización matemática y pruebas unitarias:
```bash
pip install pandas numpy matplotlib
```

---

## 🛠️ Fase de Ejecución y Generación de Datos (Paso a Paso)

Siga el orden secuencial estricto para evitar errores de referencias a archivos faltantes:

### Paso 1: Copiar el archivo origen de incidentes
Asegúrese de copiar el archivo `clasificacion_incidentes.md` (que contiene la clasificación inicial realizada en el taller) al directorio raíz de `taller1-parte2_iso25022/` para que pueda ser parseado.

### Paso 2: Ejecución de scripts generadores
Genere los conjuntos de datos de logs clínicos HCE, encuestas CSAT de satisfacción y convierta la tabla Markdown a formato CSV estructurado:
```bash
# Convertir incidentes clasificados en Markdown a CSV estructurado
python scripts/convertir_incidentes_markdown.py

# Generar logs de interacción de historia clínica HCE
python scripts/generar_logs_hce.py

# Generar respuestas a encuestas de satisfacción del cliente (CSAT)
python scripts/generar_encuesta_satisfaccion.py
```
*Evidencia:* Se crearán los archivos `logs_hce.csv`, `encuesta_satisfaccion.csv` e `incidentes_2025.csv` en el directorio `data/`.

### Paso 3: Validación formal de datos
Ejecute la verificación de calidad del dato para descartar duplicados, nulos y valores fuera de rango físico:
```bash
python scripts/validar_datos.py
```
*Resultado esperado:* La salida en consola debe confirmar 0 valores nulos y 0 duplicados en los identificadores principales.

### Paso 4: Ejecución del motor de métricas del HIS
Calcule los indicadores de calidad en uso de MediSalud HIS y expórtelos en formato JSON para el consumo visual:
```bash
# Calcular y mostrar las métricas de calidad en uso en la consola
python scripts/metricas_iso25022.py

# Exportar las métricas calculadas a JSON para dashboards
python scripts/exportar_reporte.py
```
*Evidencia:* Se generará el archivo `dashboards/indicadores.json`.

### Paso 5: Generación del Dashboard Visual
Genere las 7 visualizaciones gráficas del dashboard de calidad en formato PNG:
```bash
python scripts/generar_dashboard.py
```
*Evidencia:* Se generarán los archivos `.png` en la carpeta `dashboards/` (Semáforo de métricas, Perfil de radar, Eficiencia por sede, CSAT por rol/sede, Histograma y Pico vs Valle).

### Paso 6: Ejecución del Reto Final de Telemedicina 2.0
Corra la simulación de teleconsultas virtuales y calcule sus métricas específicas de finalización, calidad de red 3G/4G y riesgos de privacidad:
```bash
# Generar logs transaccionales de teleconsulta
python scripts/generar_datos_telemedicina.py

# Calcular métricas de telemedicina e incidentes
python scripts/metricas_telemedicina.py
```
*Evidencia:* Se crearán `data/logs_telemedicina.csv` y `dashboards/indicadores_telemedicina.json`.

### Paso 7: Ejecución de Pruebas Unitarias
Ejecute la validación de correctitud matemática de las funciones del motor principal:
```bash
python -m unittest tests.test_metricas_iso25022 -v
```
*Resultado esperado:* `test_metrica_eficiencia_promedia_tiempos ... ok`

---

## 🚀 Despliegue en Integración Continua (GitHub Actions)

Para mantener los reportes actualizados automáticamente sin intervención manual:
1. Cree la carpeta de workflows en su repositorio Git:
   ```bash
   mkdir -p .github/workflows
   ```
2. Mueva el archivo `medicion_calidad.yml` a la ruta `.github/workflows/medicion_calidad.yml`.
3. Suba los cambios a su repositorio remoto en GitHub:
   ```bash
   git add .
   git commit -m "docs: add pipeline CI/CD de medición"
   git push origin main
   ```
4. El pipeline se ejecutará de forma automática cada lunes a las 06:00 UTC, o bien de manera manual desde la pestaña **Actions** en su repositorio de GitHub.
