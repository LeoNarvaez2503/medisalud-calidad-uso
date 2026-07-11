#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nbformat as nbf
import os

def crear_notebook():
    nb = nbf.v4.new_notebook()
    
    # Title and Introduction
    intro_md = """# Dashboard de Análisis de Calidad en Uso - MediSalud HIS
Este cuaderno de Jupyter presenta un análisis estadístico y visual del conjunto de datos `incidentes_2025.csv` conteniendo los 3,000 reportes de fallas clasificados bajo la norma **ISO/IEC 25022**.

## Librerías Requeridas
Asegúrese de ejecutar este cuaderno dentro del entorno virtual configurado donde están instaladas las librerías `pandas`, `plotly` y `openpyxl`."""

    # Cell 1: Load Libraries and Data
    code_load = """import pandas as pd
import plotly.express as px
import plotly.io as pio

# Configuración de renderizado de Plotly
pio.templates.default = "plotly_white"

# Cargar el dataset clasificado
df = pd.read_csv('../data/incidentes_2025.csv')
df.head(5)"""

    # Cell 2: General Summary Markdown
    summary_md = """## 1. Estadísticas Descriptivas Generales
A continuación, se presenta un resumen de la cantidad de registros por sede, rol de usuario, módulo e incidentes totales."""

    # Cell 3: General Summary Code
    code_summary = """print(f"Total de Incidentes Registrados: {len(df)}")
print("\\nDistribución por Sede:")
print(df['sede'].value_counts())
print("\\nDistribución por Módulo (Top 5):")
print(df['modulo'].value_counts().head(5))
print("\\nDistribución por Rol de Usuario:")
print(df['rol_usuario'].value_counts())"""

    # Cell 4: Chart 1 Markdown
    chart1_md = """## 2. Distribución de Incidentes por Característica ISO/IEC 25022
Este gráfico de barras interactivo muestra el número total de quejas asociadas a cada una de las 5 características de Calidad en Uso de la norma ISO/IEC 25022."""

    # Cell 5: Chart 1 Code
    code_chart1 = """df_caract = df['caracteristica_iso_25022'].value_counts().reset_index()
df_caract.columns = ['Característica ISO 25022', 'Cantidad']

fig_bar = px.bar(
    df_caract, 
    x='Característica ISO 25022', 
    y='Cantidad',
    color='Característica ISO 25022',
    text_auto=True,
    title='Incidentes en MediSalud por Característica ISO/IEC 25022',
    color_discrete_sequence=px.colors.qualitative.Pastel
)
fig_bar.update_layout(showlegend=False, xaxis_title="", yaxis_title="Número de Reportes")
fig_bar.show()"""

    # Cell 6: Chart 2 Markdown
    chart2_md = """## 3. Porcentaje de Incidentes por Módulo del Sistema
Visualización del impacto relativo de los fallos en cada módulo principal de MediSalud HIS."""

    # Cell 7: Chart 2 Code
    code_chart2 = """df_modulo = df['modulo'].value_counts().reset_index()
df_modulo.columns = ['Módulo', 'Cantidad']

fig_pie = px.pie(
    df_modulo, 
    names='Módulo', 
    values='Cantidad',
    title='Distribución de Fallos por Módulo del Sistema MediSalud HIS',
    color_discrete_sequence=px.colors.qualitative.Safe,
    hole=0.4
)
fig_pie.update_traces(textposition='inside', textinfo='percent+label')
fig_pie.show()"""

    # Cell 8: Chart 3 Markdown
    chart3_md = """## 4. Distribución Geográfica de Calidad por Sede
Comparativa de incidentes clasificados por ciudad (sede) para identificar cuellos de botella geográficos."""

    # Cell 9: Chart 3 Code
    code_chart3 = """df_sede = df.groupby(['sede', 'caracteristica_iso_25022']).size().reset_index(name='Cantidad')

fig_sede = px.bar(
    df_sede, 
    x='sede', 
    y='Cantidad', 
    color='caracteristica_iso_25022',
    title='Incidentes de Calidad en Uso por Sede Hospitalaria',
    barmode='group',
    labels={'sede': 'Sede Hospitalaria', 'Cantidad': 'Reportes', 'caracteristica_iso_25022': 'Característica ISO'},
    color_discrete_sequence=px.colors.qualitative.Bold
)
fig_sede.update_layout(xaxis_title="Ciudad / Sede", yaxis_title="Número de Reportes")
fig_sede.show()"""

    # Cell 10: Conclusion Markdown
    conclusion_md = """## Conclusiones del Dashboard
1.  **Efectividad** es la categoría con más reportes (cercano al 50%), reflejando que los usuarios se enfrentan a impedimentos funcionales para terminar sus tareas clínicas o administrativas.
2.  **Libertad de Riesgo** representa un volumen muy alto (24%), lo que significa que 1 de cada 4 incidentes pone en riesgo la salud de un paciente o la estabilidad financiera del hospital. Esto exige atención correctiva inmediata.
3.  **Eficiencia** y **Satisfacción** revelan cuellos de botella en el rendimiento del servidor y frustraciones en el flujo del portal de citas, requiriendo optimización de base de datos e interfaces UI."""

    # Append cells to notebook
    nb.cells = [
        nbf.v4.new_markdown_cell(intro_md),
        nbf.v4.new_code_cell(code_load),
        nbf.v4.new_markdown_cell(summary_md),
        nbf.v4.new_code_cell(code_summary),
        nbf.v4.new_markdown_cell(chart1_md),
        nbf.v4.new_code_cell(code_chart1),
        nbf.v4.new_markdown_cell(chart2_md),
        nbf.v4.new_code_cell(code_chart2),
        nbf.v4.new_markdown_cell(chart3_md),
        nbf.v4.new_code_cell(code_chart3),
        nbf.v4.new_markdown_cell(conclusion_md)
    ]
    
    # Save path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dash_dir = os.path.join(base_dir, 'dashboards')
    os.makedirs(dash_dir, exist_ok=True)
    nb_path = os.path.join(dash_dir, 'analisis_dashboards.ipynb')
    
    with open(nb_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
        
    print(f"Notebook created successfully at: {os.path.abspath(nb_path)}")

if __name__ == "__main__":
    crear_notebook()
