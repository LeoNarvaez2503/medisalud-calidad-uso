"""
Escenario 9 — Construccion de Indicadores (KPI)
Genera dashboards visuales de Calidad en Uso basados en ISO/IEC 25022
para el sistema MediSalud HIS.

Produce:
  dashboards/semaforo_metricas.png
  dashboards/eficiencia_por_sede.png
  dashboards/radar_iso25022.png
  dashboards/histograma_tiempos_hce.png
  dashboards/csat_por_sede.png
  dashboards/csat_por_rol.png
"""
from __future__ import annotations

import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DASH = ROOT / "dashboards"
INDICADORES = DASH / "indicadores.json"

COLORES = {
    "cumple": "#2ecc71",
    "no_cumple": "#e74c3c",
    "umbral": "#f39c12",
    "fondo": "#1a1a2e",
    "texto": "#e0e0e0",
    "barra": "#3498db",
    "acento": "#9b59b6",
}


def cargar_indicadores() -> dict:
    with INDICADORES.open(encoding="utf-8") as f:
        return json.load(f)


def cargar_csv(nombre: str) -> list[dict[str, str]]:
    with (DATA / nombre).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def estilo_oscuro(ax: plt.Axes) -> None:
    ax.set_facecolor(COLORES["fondo"])
    ax.tick_params(colors=COLORES["texto"])
    for spine in ax.spines.values():
        spine.set_color(COLORES["texto"])
    ax.title.set_color(COLORES["texto"])
    ax.xaxis.label.set_color(COLORES["texto"])
    ax.yaxis.label.set_color(COLORES["texto"])


# ---------- 1. Semáforo de métricas ----------
def generar_semaforo(datos: dict) -> None:
    metricas = datos["metricas"]
    nombres = []
    valores = []
    umbrales = []
    cumple = []

    for clave, m in metricas.items():
        nombres.append(m["nombre"])
        valores.append(m["valor"])
        umbrales.append(m["umbral"])
        cumple.append(m["cumple"])

    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor(COLORES["fondo"])
    estilo_oscuro(ax)

    y = range(len(nombres))
    colores_barra = [COLORES["cumple"] if c else COLORES["no_cumple"] for c in cumple]
    barras = ax.barh(y, valores, color=colores_barra, edgecolor="white", linewidth=0.5, height=0.6)

    for i, u in enumerate(umbrales):
        ax.plot(u, i, marker="D", color=COLORES["umbral"], markersize=10, zorder=5)

    ax.set_yticks(y)
    ax.set_yticklabels(nombres, fontsize=9)
    ax.set_xlabel("Valor de la métrica")
    ax.set_title("Semáforo de Métricas ISO/IEC 25022 — MediSalud HIS", fontsize=13, fontweight="bold")
    ax.invert_yaxis()

    leyenda = [
        mpatches.Patch(color=COLORES["cumple"], label="Cumple umbral"),
        mpatches.Patch(color=COLORES["no_cumple"], label="No cumple umbral"),
        plt.Line2D([0], [0], marker="D", color="w", markerfacecolor=COLORES["umbral"],
                   markersize=8, label="Umbral definido"),
    ]
    ax.legend(handles=leyenda, loc="lower right", fontsize=8,
              facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    for barra, val in zip(barras, valores):
        ax.text(barra.get_width() + 0.01, barra.get_y() + barra.get_height() / 2,
                f"{val}", va="center", fontsize=9, color=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "semaforo_metricas.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] semaforo_metricas.png")



# ---------- 2. Eficiencia por sede ----------
def generar_eficiencia_sede(datos: dict) -> None:
    sedes_data = datos["eficiencia_por_sede"]
    sedes = [s["sede"] for s in sedes_data]
    tiempos = [s["tiempo_promedio_segundos"] for s in sedes_data]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(COLORES["fondo"])
    estilo_oscuro(ax)

    colores = [COLORES["no_cumple"] if t > 8.0 else COLORES["cumple"] for t in tiempos]
    ax.bar(sedes, tiempos, color=colores, edgecolor="white", linewidth=0.5)
    ax.axhline(y=8.0, color=COLORES["umbral"], linestyle="--", linewidth=2, label="Umbral RNF-01 (8 s)")

    for i, t in enumerate(tiempos):
        ax.text(i, t + 0.1, f"{t} s", ha="center", fontsize=10, color=COLORES["texto"])

    ax.set_ylabel("Tiempo promedio (segundos)")
    ax.set_title("Eficiencia de Registro HCE por Sede — Cobertura de Contexto", fontsize=12, fontweight="bold")
    ax.legend(facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "eficiencia_por_sede.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] eficiencia_por_sede.png")


# ---------- 3. Radar ISO/IEC 25022 ----------
def generar_radar(datos: dict) -> None:
    metricas = datos["metricas"]
    mapa = {
        "Efectividad": metricas["efectividad"]["valor"],
        "Eficiencia": min(metricas["eficiencia"]["valor"] / 8.0, 1.0),  # normalizar: menor es mejor
        "Satisfacción": metricas["satisfaccion"]["valor"],
        "Libertad de Riesgo": max(0, 1 - metricas["libertad_riesgo"]["valor"]),  # invertir: menor tasa = mejor
        "Cobertura de Contexto": metricas["cobertura_contexto"]["valor"],
    }

    categorias = list(mapa.keys())
    valores = list(mapa.values())
    n = len(categorias)

    angulos = [i / float(n) * 2 * math.pi for i in range(n)]
    valores += valores[:1]
    angulos += angulos[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor(COLORES["fondo"])
    ax.set_facecolor(COLORES["fondo"])

    ax.plot(angulos, valores, "o-", linewidth=2, color="#3498db")
    ax.fill(angulos, valores, alpha=0.25, color="#3498db")

    # Línea de umbral a 0.85
    umbral_vals = [0.85] * (n + 1)
    ax.plot(angulos, umbral_vals, "--", linewidth=1.5, color=COLORES["umbral"], label="Umbral 85%")

    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(categorias, fontsize=9, color=COLORES["texto"])
    ax.set_ylim(0, 1.05)
    ax.set_title("Perfil de Calidad en Uso — ISO/IEC 25022", fontsize=12, fontweight="bold",
                 color=COLORES["texto"], pad=20)
    ax.tick_params(colors=COLORES["texto"])
    ax.spines["polar"].set_color(COLORES["texto"])
    ax.yaxis.grid(color=COLORES["texto"], alpha=0.3)
    ax.xaxis.grid(color=COLORES["texto"], alpha=0.3)
    ax.legend(loc="upper right", fontsize=8,
              facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "radar_iso25022.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] radar_iso25022.png")


# ---------- 4. Histograma de tiempos HCE ----------
def generar_histograma_tiempos() -> None:
    logs = cargar_csv("logs_hce.csv")
    tiempos = [float(f["tiempo_segundos"]) for f in logs]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(COLORES["fondo"])
    estilo_oscuro(ax)

    ax.hist(tiempos, bins=40, color=COLORES["barra"], edgecolor="white", linewidth=0.5, alpha=0.85)
    ax.axvline(x=8.0, color=COLORES["umbral"], linestyle="--", linewidth=2, label="Umbral RNF-01 (8 s)")

    pct_cumple = sum(1 for t in tiempos if t <= 8.0) / len(tiempos) * 100
    ax.axvline(x=mean(tiempos), color=COLORES["acento"], linestyle="-.", linewidth=1.5,
               label=f"Promedio ({mean(tiempos):.2f} s)")

    ax.set_xlabel("Tiempo de registro (segundos)")
    ax.set_ylabel("Frecuencia")
    ax.set_title(
        f"Distribución de Tiempos de Registro HCE — {pct_cumple:.1f}% dentro del umbral",
        fontsize=12, fontweight="bold",
    )
    ax.legend(facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "histograma_tiempos_hce.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] histograma_tiempos_hce.png")


# ---------- 5. CSAT por sede ----------
def generar_csat_sede() -> None:
    encuesta = cargar_csv("encuesta_satisfaccion.csv")
    por_sede: dict[str, list[int]] = defaultdict(list)
    for f in encuesta:
        por_sede[f["sede"]].append(int(f["puntaje_csat"]))

    sedes = sorted(por_sede.keys())
    promedios = [mean(por_sede[s]) for s in sedes]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(COLORES["fondo"])
    estilo_oscuro(ax)

    colores = [COLORES["no_cumple"] if p < 4.0 else COLORES["cumple"] for p in promedios]
    ax.bar(sedes, promedios, color=colores, edgecolor="white", linewidth=0.5)
    ax.axhline(y=4.0, color=COLORES["umbral"], linestyle="--", linewidth=2,
               label="Umbral CSAT (4.0 / 5 = 0.80 normalizado)")

    for i, p in enumerate(promedios):
        ax.text(i, p + 0.05, f"{p:.2f}", ha="center", fontsize=10, color=COLORES["texto"])

    ax.set_ylabel("Puntaje CSAT promedio (1-5)")
    ax.set_title("Satisfacción (CSAT) por Sede — MediSalud HIS", fontsize=12, fontweight="bold")
    ax.set_ylim(0, 5.5)
    ax.legend(facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "csat_por_sede.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] csat_por_sede.png")


# ---------- 6. CSAT por rol ----------
def generar_csat_rol() -> None:
    encuesta = cargar_csv("encuesta_satisfaccion.csv")
    por_rol: dict[str, list[int]] = defaultdict(list)
    for f in encuesta:
        por_rol[f["rol"]].append(int(f["puntaje_csat"]))

    roles = sorted(por_rol.keys())
    promedios = [mean(por_rol[r]) for r in roles]

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(COLORES["fondo"])
    estilo_oscuro(ax)

    colores = [COLORES["no_cumple"] if p < 4.0 else COLORES["cumple"] for p in promedios]
    ax.barh(roles, promedios, color=colores, edgecolor="white", linewidth=0.5, height=0.6)
    ax.axvline(x=4.0, color=COLORES["umbral"], linestyle="--", linewidth=2,
               label="Umbral CSAT (4.0 / 5)")

    for i, p in enumerate(promedios):
        ax.text(p + 0.05, i, f"{p:.2f}", va="center", fontsize=10, color=COLORES["texto"])

    ax.set_xlabel("Puntaje CSAT promedio (1-5)")
    ax.set_title("Satisfacción (CSAT) por Rol de Usuario — MediSalud HIS", fontsize=12, fontweight="bold")
    ax.set_xlim(0, 5.5)
    ax.legend(facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "csat_por_rol.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] csat_por_rol.png")


# ---------- 7. Tiempos hora pico vs hora valle ----------
def generar_pico_vs_valle() -> None:
    logs = cargar_csv("logs_hce.csv")
    pico = []
    valle = []
    for f in logs:
        hora = int(f["timestamp"].split("T")[1].split(":")[0])
        t = float(f["tiempo_segundos"])
        if 10 <= hora <= 12:
            pico.append(t)
        else:
            valle.append(t)

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(COLORES["fondo"])
    estilo_oscuro(ax)

    ax.hist(valle, bins=30, alpha=0.7, color=COLORES["cumple"], edgecolor="white",
            linewidth=0.3, label=f"Hora valle (n={len(valle)}, μ={mean(valle):.2f}s)")
    ax.hist(pico, bins=30, alpha=0.7, color=COLORES["no_cumple"], edgecolor="white",
            linewidth=0.3, label=f"Hora pico 10-12h (n={len(pico)}, μ={mean(pico):.2f}s)")
    ax.axvline(x=8.0, color=COLORES["umbral"], linestyle="--", linewidth=2, label="Umbral 8 s")

    ax.set_xlabel("Tiempo de registro (segundos)")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Comparación Hora Pico vs Hora Valle — Registro HCE", fontsize=12, fontweight="bold")
    ax.legend(facecolor=COLORES["fondo"], edgecolor=COLORES["texto"], labelcolor=COLORES["texto"])

    fig.tight_layout()
    fig.savefig(DASH / "pico_vs_valle.png", dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print("  [OK] pico_vs_valle.png")


def main() -> None:
    DASH.mkdir(parents=True, exist_ok=True)
    datos = cargar_indicadores()

    print("Generando dashboards de Calidad en Uso...")
    generar_semaforo(datos)
    generar_eficiencia_sede(datos)
    generar_radar(datos)
    generar_histograma_tiempos()
    generar_csat_sede()
    generar_csat_rol()
    generar_pico_vs_valle()
    print(f"\nDashboards generados en {DASH.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
