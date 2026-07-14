"""
Genera entregables en PDF usando LaTeX.

Los PDFs se enfocan en informacion para exposicion: caratula, tablas y
conclusiones breves. No incluyen diagramas ni imagenes.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX_DIR = ROOT / "latex"
PDF_DIR = ROOT / "pdfs"


def esc(texto: object) -> str:
    valor = str(texto)
    reemplazos = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(reemplazos.get(caracter, caracter) for caracter in valor)


def filas_tabla(filas: list[list[object]]) -> str:
    return "\n".join(" & ".join(esc(celda) for celda in fila) + r" \\" for fila in filas)


def documento(titulo: str, contenido: str) -> str:
    return rf"""
\documentclass[11pt]{{article}}
\usepackage[utf8]{{inputenc}}
\usepackage[T1]{{fontenc}}
\usepackage[a4paper,margin=1.8cm]{{geometry}}
\usepackage{{array}}
\usepackage{{booktabs}}
\usepackage{{longtable}}
\usepackage{{tabularx}}

\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{6pt}}
\renewcommand{{\arraystretch}}{{1.18}}

\begin{{document}}

\begin{{titlepage}}
\centering
{{\Large Universidad de las Fuerzas Armadas\par}}
{{\LARGE \textbf{{ESPE}}\par}}
\vspace{{0.35cm}}
{{\large Departamento de Ciencias de la Computación\par}}
\vspace{{1.5cm}}
{{\Large \textbf{{Aseguramiento de la Calidad de Software}}\par}}
\vspace{{0.5cm}}
{{\large \textbf{{Grupo: 6}}\par}}
\vspace{{1.2cm}}
{{\Large \textbf{{{esc(titulo)}}}\par}}
\vfill
\begin{{tabular}}{{rl}}
\textbf{{Integrantes:}} & Caetano Flores, Jordan Guamán,\\
& Anthony Morales, Leonardo Narváez\\
\textbf{{NRC:}} & 30733\\
\textbf{{Docente:}} & Ing. Diego Gamboa\\
\end{{tabular}}
\vfill
{{\large 2026\par}}
\end{{titlepage}}

{contenido}

\end{{document}}
"""


def tabla(headers: list[str], rows: list[list[object]], widths: list[str] | None = None) -> str:
    if widths is None:
        spec = " ".join(["p{0.22\\textwidth}"] * len(headers))
    else:
        spec = " ".join([f"p{{{w}}}" for w in widths])
    head = " & ".join(r"\textbf{" + esc(h) + "}" for h in headers) + r" \\"
    return rf"""
\small
\begin{{longtable}}{{{spec}}}
\toprule
{head}
\midrule
\endfirsthead
\toprule
{head}
\midrule
\endhead
{filas_tabla(rows)}
\bottomrule
\end{{longtable}}
\normalsize
"""


def escenario_4() -> str:
    contenido = r"\section*{Escenario 4: Identificación de Atributos de Calidad en Uso}"
    contenido += "\n" + tabla(
        ["Proceso", "Usuario", "Tarea representativa", "Contexto de uso", "Atributos"],
        [
            [
                "Atención médica y registro de HCE",
                "Médico tratante",
                "Registrar una nota de evolución clínica completa con diagnóstico, indicaciones y firma electrónica.",
                "Consulta externa, 10:00-12:00, red interna de Quito, alta concurrencia.",
                "Eficiencia: tiempo de tarea. Efectividad: completitud. Satisfacción: fluidez. Libertad de Riesgo: información clínica correcta.",
            ],
            [
                "Agendamiento de citas",
                "Paciente",
                "Agendar una cita con especialista seleccionando sede, fecha, horario y confirmación.",
                "Portal web o app móvil, red celular, 18:00-21:00, sedes de alta demanda.",
                "Efectividad: tasa de éxito. Eficiencia: pasos y tiempo. Satisfacción: confianza. Cobertura: web y móvil.",
            ],
            [
                "Facturación con seguro médico",
                "Personal de admisión/facturación",
                "Generar factura, validar convenio, procesar pago/copago y emitir comprobante correcto.",
                "Punto de admisión, cierre de jornada, integración con sistema financiero heredado.",
                "Libertad de Riesgo: errores financieros. Efectividad: exactitud. Eficiencia: tiempo de proceso. Cobertura: sede y rol.",
            ],
        ],
        ["0.16\\textwidth", "0.13\\textwidth", "0.23\\textwidth", "0.21\\textwidth", "0.21\\textwidth"],
    )
    contenido += r"""
\subsection*{Conclusión}
La calidad en uso debe medirse sobre tareas concretas, no sobre módulos abstractos. Estas fichas permiten convertir procesos críticos en métricas comparables y accionables.
"""
    return contenido


def escenario_5() -> str:
    contenido = r"\section*{Escenario 5: Mapeo de Características de Calidad}"
    contenido += "\n" + tabla(
        ["Tarea", "Impacto", "Frecuencia", "Características ISO/IEC 25022", "Prioridad"],
        [
            ["Registrar nota de evolución clínica", "Alto", "Alta", "Eficiencia, Efectividad, Satisfacción, Libertad de Riesgo", 1],
            ["Agendar cita en portal", "Alto", "Alta", "Efectividad, Eficiencia, Satisfacción, Cobertura de Contexto", 1],
            ["Facturar consulta con seguro", "Alto", "Media", "Libertad de Riesgo, Efectividad, Eficiencia", 2],
            ["Completar teleconsulta", "Alto", "Media", "Efectividad, Cobertura de Contexto, Satisfacción", 2],
            ["Dispensar medicamento desde receta electrónica", "Alto", "Media", "Libertad de Riesgo, Efectividad", 2],
            ["Consultar historial de laboratorio", "Medio", "Alta", "Efectividad, Satisfacción", 3],
            ["Generar reporte gerencial mensual", "Medio", "Baja", "Eficiencia, Efectividad", 3],
            ["Actualizar datos personales desde app móvil", "Bajo", "Media", "Cobertura de Contexto, Satisfacción", 4],
        ],
        ["0.25\\textwidth", "0.10\\textwidth", "0.12\\textwidth", "0.35\\textwidth", "0.08\\textwidth"],
    )
    contenido += r"""
\subsection*{Alcance inicial}
Se recomiendan para medición inmediata las prioridades 1 y 2: HCE, portal de citas, facturación, teleconsulta y dispensación de medicamentos.

\subsection*{Conclusión}
La priorización evita medir todo sin foco y concentra recursos en los procesos con mayor riesgo clínico, financiero y reputacional.
"""
    return contenido


def escenario_6() -> str:
    contenido = r"\section*{Escenario 6: Catálogo de Métricas ISO/IEC 25022}"
    contenido += "\n" + tabla(
        ["Métrica", "Característica", "Fórmula", "Unidad", "Umbral", "Fuente"],
        [
            ["Completitud de registro de HCE", "Efectividad", "Notas completadas / notas intentadas", "Proporción", ">= 0.95", "logs_hce.csv"],
            ["Tiempo promedio de registro de HCE", "Eficiencia", "Suma de tiempos / número de notas", "Segundos", "<= 8 s", "logs_hce.csv"],
            ["CSAT normalizado", "Satisfacción", "Promedio CSAT / 5", "Proporción", ">= 0.80", "encuesta_satisfaccion.csv"],
            ["Tasa de errores de facturación", "Libertad de Riesgo", "Errores de facturación / transacciones", "Proporción", "<= 0.01", "incidentes_2025.csv"],
            ["Consistencia entre sedes", "Cobertura de Contexto", "Mejor tiempo promedio / peor tiempo promedio", "Proporción", ">= 0.85", "logs_hce.csv"],
        ],
        ["0.23\\textwidth", "0.16\\textwidth", "0.24\\textwidth", "0.11\\textwidth", "0.10\\textwidth", "0.12\\textwidth"],
    )
    contenido += r"""
\subsection*{Interpretación}
Los umbrales se fijan antes del cálculo para evitar interpretaciones subjetivas. Cada métrica tiene fuente, unidad y responsable, por lo que puede automatizarse.
"""
    return contenido


def escenario_7() -> str:
    contenido = r"\section*{Escenario 7: Obtención y Validación de Datos}"
    contenido += "\n" + tabla(
        ["Archivo", "Registros", "Origen", "Uso"],
        [
            ["data/logs_hce.csv", 3150, "Generador de logs HCE", "Efectividad, Eficiencia y Cobertura de Contexto"],
            ["data/encuesta_satisfaccion.csv", 150, "Encuesta CSAT simulada", "Satisfacción por sede y rol"],
            ["data/incidentes_2025.csv", 3000, "Conversión desde clasificación Markdown", "Libertad de Riesgo y análisis de incidentes"],
        ],
        ["0.26\\textwidth", "0.12\\textwidth", "0.28\\textwidth", "0.28\\textwidth"],
    )
    contenido += "\n" + tabla(
        ["Archivo", "Nulos", "Duplicados", "Rangos inválidos", "Resultado"],
        [
            ["logs_hce.csv", 0, 0, "0 tiempos fuera de 0-120 s; 0 valores inválidos en completada", "Válido"],
            ["encuesta_satisfaccion.csv", 0, 0, "0 puntajes fuera de 1-5", "Válido"],
            ["incidentes_2025.csv", 0, 0, "No aplica", "Válido"],
        ],
        ["0.24\\textwidth", "0.10\\textwidth", "0.13\\textwidth", "0.35\\textwidth", "0.10\\textwidth"],
    )
    contenido += r"""
\subsection*{Resumen}
El tiempo promedio HCE fue 7.43 s y el CSAT promedio fue 3.61/5. Los datos quedaron listos para automatización.
"""
    return contenido


def escenario_8() -> str:
    indicadores = json.loads((ROOT / "dashboards" / "indicadores.json").read_text(encoding="utf-8"))
    rows = []
    for item in indicadores["metricas"].values():
        rows.append(
            [
                item["caracteristica"],
                item["nombre"],
                item["valor"],
                item["umbral"],
                "Cumple" if item["cumple"] else "No cumple",
            ]
        )

    contenido = r"\section*{Escenario 8: Automatización de la Medición}"
    contenido += "\n" + tabla(
        ["Componente", "Archivo", "Función"],
        [
            ["Conversión de incidentes", "convertir_incidentes_markdown.py", "Reconstruye incidentes_2025.csv desde el material local."],
            ["Generación de logs", "generar_logs_hce.py", "Simula eventos de registro clínico por sede."],
            ["Generación CSAT", "generar_encuesta_satisfaccion.py", "Crea encuesta de satisfacción por sede y rol."],
            ["Validación", "validar_datos.py", "Verifica nulos, duplicados y rangos."],
            ["Cálculo de métricas", "metricas_iso25022.py", "Calcula indicadores ISO/IEC 25022."],
            ["Exportación", "exportar_reporte.py", "Genera indicadores.json para dashboards."],
        ],
        ["0.22\\textwidth", "0.30\\textwidth", "0.38\\textwidth"],
    )
    contenido += "\n" + tabla(
        ["Característica", "Métrica", "Valor", "Umbral", "Estado"],
        rows,
        ["0.17\\textwidth", "0.38\\textwidth", "0.12\\textwidth", "0.12\\textwidth", "0.12\\textwidth"],
    )
    contenido += r"""
\subsection*{Interpretación}
Aunque el promedio de HCE cumple 8 s, el RNF-01 no cumple porque solo 67.87\% de notas se registran dentro del umbral. También no cumplen satisfacción y riesgo de facturación.
"""
    return contenido


def informe_cierre() -> str:
    contenido = r"\section*{Informe Ejecutivo y Plan de Mejora Continua}"
    contenido += "\n" + tabla(
        ["Hallazgo", "Evidencia", "Impacto"],
        [
            ["Incidentes de efectividad concentrados", "1.493 de 3.000 incidentes", "Usuarios no completan tareas o las completan con errores."],
            ["Riesgo clínico y financiero", "721 incidentes de Libertad de Riesgo", "Posibles errores de medicación, exposición de datos y problemas de facturación."],
            ["RNF-01 incumplido", "67.87% de notas en <= 8 s frente a umbral de 90%", "Lentitud en consulta externa y menor productividad médica."],
            ["RNF-03 incumplido", "3.01% de errores de facturación frente a umbral de 1%", "Riesgo financiero y pérdida de confianza."],
            ["Satisfacción baja", "CSAT normalizado de 0.7227 frente a 0.80", "Experiencia percibida insuficiente."],
        ],
        ["0.25\\textwidth", "0.30\\textwidth", "0.35\\textwidth"],
    )
    contenido += "\n" + tabla(
        ["Fase PDCA", "Acciones", "Responsable", "Evidencia"],
        [
            ["Planificar", "Definir umbrales, tareas prioritarias y fuentes oficiales.", "Calidad, TI, Dirección Médica", "Catálogo de métricas."],
            ["Hacer", "Ejecutar pipeline semanal y generar indicadores.", "TI y Calidad", "indicadores.json."],
            ["Verificar", "Comparar resultados contra RNF-01, RNF-03 y CSAT.", "Calidad y Auditoría", "Informe mensual."],
            ["Actuar", "Optimizar HCE, facturación, UX e integraciones críticas.", "TI, Producto, Operaciones", "Backlog de mejoras."],
        ],
        ["0.14\\textwidth", "0.34\\textwidth", "0.22\\textwidth", "0.20\\textwidth"],
    )
    contenido += r"""
\subsection*{Recomendación}
Aprobar un ciclo de mejora de 90 días centrado en HCE y facturación, con seguimiento quincenal de indicadores y reporte ejecutivo mensual.
"""
    return contenido


DOCUMENTOS = [
    ("01_escenario_4_atributos_calidad_uso", "Escenario 4: Atributos de Calidad en Uso", escenario_4),
    ("02_escenario_5_mapeo_priorizacion", "Escenario 5: Mapeo y Priorización", escenario_5),
    ("03_escenario_6_catalogo_metricas", "Escenario 6: Catálogo de Métricas", escenario_6),
    ("04_escenario_7_obtencion_datos", "Escenario 7: Obtención de Datos", escenario_7),
    ("05_escenario_8_automatizacion_medicion", "Escenario 8: Automatización de la Medición", escenario_8),
    ("06_informe_ejecutivo_plan_mejora", "Informe Ejecutivo y Plan de Mejora", informe_cierre),
]


def informe_completo() -> str:
    contenido = r"""
\section*{Introducción}
El presente informe consolida los entregables del taller de medición de Calidad en Uso mediante ISO/IEC 25022 para el caso MediSalud HIS. Se incluyen las fichas de usuario-tarea-contexto, la matriz de priorización, el catálogo de métricas, la obtención de datos, la automatización de indicadores y el plan de mejora continua.

\newpage
"""
    contenido += escenario_4()
    contenido += r"\newpage" + "\n"
    contenido += escenario_5()
    contenido += r"\newpage" + "\n"
    contenido += escenario_6()
    contenido += r"\newpage" + "\n"
    contenido += escenario_7()
    contenido += r"\newpage" + "\n"
    contenido += escenario_8()
    contenido += r"\newpage" + "\n"
    contenido += informe_cierre()
    contenido += r"""

\section*{Conclusión General}
El programa propuesto permite pasar de percepciones aisladas sobre el funcionamiento de MediSalud HIS a evidencia objetiva, repetible y accionable. Los resultados muestran que la organización debe priorizar tres frentes: cumplimiento real del RNF-01 en HCE, reducción de errores de facturación asociados al RNF-03 y mejora de la satisfacción de usuarios clínicos y pacientes.
"""
    return contenido


def compilar(nombre: str, tex: str) -> None:
    TEX_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    ruta_tex = TEX_DIR / f"{nombre}.tex"
    ruta_tex.write_text(tex, encoding="utf-8")

    for _ in range(2):
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", ruta_tex.name],
            cwd=TEX_DIR,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    pdf_origen = TEX_DIR / f"{nombre}.pdf"
    pdf_destino = PDF_DIR / f"{nombre}.pdf"
    pdf_destino.write_bytes(pdf_origen.read_bytes())
    print(f"Generado {pdf_destino.relative_to(ROOT)}")


def main() -> None:
    for nombre, titulo, constructor in DOCUMENTOS:
        compilar(nombre, documento(titulo, constructor()))
    compilar(
        "00_informe_completo_entregables_iso25022_grupo6",
        documento("Informe Completo de Entregables ISO/IEC 25022", informe_completo()),
    )


if __name__ == "__main__":
    main()
