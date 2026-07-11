# MediSalud Calidad en Uso - Taller 3

Este repositorio contiene los entregables prácticos y teóricos correspondientes a los tres primeros escenarios del Taller 3 sobre la calidad de software en la red hospitalaria **MediSalud**, enfocándose en la norma **ISO/IEC 25022 (Calidad en Uso)** y la familia de normas **ISO/IEC 25000 (SQuaRE)**.

---

## 📂 Estructura del Repositorio

El proyecto está organizado bajo la siguiente estructura de directorios:

```text
medisalud-calidad-uso/
├── .venv/                  # Entorno virtual de Python (excluido en .gitignore)
├── data/
│   └── incidentes_2025.csv # Conjunto de datos de 3,000 incidentes clasificados
├── dashboards/
│   └── analisis_dashboards.ipynb # Cuaderno de Jupyter interactivo con visualizaciones Plotly
├── docs/
│   ├── analisis_inicial.md       # Escenario 1: Análisis del caso empresarial y preguntas de negocio
│   ├── clasificacion_incidentes.md # Escenario 2: Clasificación e incidentes ISO 25022 (Tabla 2.2)
│   └── modelo_square.md          # Escenario 3: Resumen teórico de SQuaRE y mapa conceptual Mermaid
├── reportes/               # Carpeta para compilación de reportes adicionales
├── scripts/
│   ├── clasificar_incidentes.py  # Script en Python que automatiza la clasificación del dataset
│   └── generar_notebook.py       # Script en Python que crea el cuaderno de Jupyter
├── README.md               # Guía del proyecto e instrucciones
└── requirements.txt        # Dependencias del entorno de Python
```

---

## 🛠️ Configuración y Uso

### Requisitos Previos
*   Python 3.11 o superior instalado.
*   Git configurado.

### Instalación del Entorno
1.  **Clonar u organizar el repositorio localmente:**
    ```bash
    git clone https://github.com/tu-usuario/medisalud-calidad-uso.git
    cd medisalud-calidad-uso
    ```

2.  **Crear e instalar dependencias en el entorno virtual:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

### Ejecución de los Scripts
*   **Clasificar el dataset:**
    El script procesa los 3,000 incidentes originales y los guarda clasificados con justificaciones técnicas y correlación de Requerimientos No Funcionales (RNF):
    ```bash
    python scripts/clasificar_incidentes.py
    ```
    *Output:* `data/incidentes_2025.csv`

*   **Generar el Cuaderno de Jupyter:**
    Reconstruye el cuaderno interactivo de análisis:
    ```bash
    python scripts/generar_notebook.py
    ```
    *Output:* `dashboards/analisis_dashboards.ipynb`

*   **Visualizar el Dashboard:**
    Inicie Jupyter Notebook para visualizar los gráficos interactivos de Plotly:
    ```bash
    jupyter notebook dashboards/analisis_dashboards.ipynb
    ```

---

## 📝 Resumen de Entregables por Escenario

### 🔹 Escenario 1: Introducción al Caso Empresarial
*   Ubicación: [docs/analisis_inicial.md](docs/analisis_inicial.md)
*   **Contenido:** Definición fundamentada de los 3 procesos más críticos del negocio (HCE, Farmacia y Agendamiento), usuarios afectados por fallas en el HIS y el inventario de la evidencia de calidad disponible y faltante.

### 🔹 Escenario 2: Comprensión de ISO/IEC 25022
*   Ubicación: [docs/clasificacion_incidentes.md](docs/clasificacion_incidentes.md) y [data/incidentes_2025.csv](data/incidentes_2025.csv)
*   **Contenido:** Tabla de clasificación de incidentes en producción (Tabla 2.2). Cada incidente incluye su justificación técnica basada en la norma y su relación con los requerimientos no funcionales (ej. RNF-01 de latencia clínica y RNF-03 de tasa de error de facturación).
*   **Métricas del Dataset Clasificado (3,000 incidentes):**
    *   *Efectividad:* 49.77%
    *   *Libertad de Riesgo:* 24.03%
    *   *Eficiencia:* 10.77%
    *   *Satisfacción:* 9.33%
    *   *Cobertura de Contexto:* 6.10%

### 🔹 Escenario 3: Comprensión del Modelo SQuaRE
*   Ubicación: [docs/modelo_square.md](docs/modelo_square.md)
*   **Contenido:** Explicación y contraste de los tres niveles de calidad (Interna, Externa y en Uso), Tabla 3.2 con ejemplos en el módulo de receta médica del HIS, y un mapa conceptual interactivo detallado en sintaxis Mermaid que explica la organización de la familia ISO/IEC 25000 (normas 25000, 25010, 25022 y 25040).
