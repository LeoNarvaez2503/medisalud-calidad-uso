"""
Validacion basica de calidad de datos para el taller ISO/IEC 25022.
"""
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def cargar_csv(ruta: Path) -> list[dict[str, str]]:
    with ruta.open(newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def contar_nulos(filas: list[dict[str, str]]) -> dict[str, int]:
    if not filas:
        return {}
    columnas = filas[0].keys()
    return {columna: sum(1 for fila in filas if fila[columna] == "") for columna in columnas}


def validar_logs() -> dict[str, object]:
    filas = cargar_csv(ROOT / "data" / "logs_hce.csv")
    ids = [fila["evento_id"] for fila in filas]
    tiempos = [float(fila["tiempo_segundos"]) for fila in filas]
    completadas = [int(fila["completada"]) for fila in filas]

    return {
        "archivo": "data/logs_hce.csv",
        "filas": len(filas),
        "nulos": contar_nulos(filas),
        "duplicados_evento_id": len(ids) - len(set(ids)),
        "tiempos_fuera_rango": sum(1 for valor in tiempos if valor < 0 or valor > 120),
        "completada_fuera_rango": sum(1 for valor in completadas if valor not in (0, 1)),
        "tiempo_min": round(min(tiempos), 2),
        "tiempo_max": round(max(tiempos), 2),
        "tiempo_promedio": round(sum(tiempos) / len(tiempos), 2),
    }


def validar_encuesta() -> dict[str, object]:
    filas = cargar_csv(ROOT / "data" / "encuesta_satisfaccion.csv")
    ids = [fila["respuesta_id"] for fila in filas]
    puntajes = [int(fila["puntaje_csat"]) for fila in filas]

    return {
        "archivo": "data/encuesta_satisfaccion.csv",
        "filas": len(filas),
        "nulos": contar_nulos(filas),
        "duplicados_respuesta_id": len(ids) - len(set(ids)),
        "puntajes_fuera_rango": sum(1 for valor in puntajes if valor < 1 or valor > 5),
        "csat_promedio": round(sum(puntajes) / len(puntajes), 2),
    }


def validar_incidentes() -> dict[str, object]:
    filas = cargar_csv(ROOT / "data" / "incidentes_2025.csv")
    ids = [fila["id"] for fila in filas]

    return {
        "archivo": "data/incidentes_2025.csv",
        "filas": len(filas),
        "nulos": contar_nulos(filas),
        "duplicados_id": len(ids) - len(set(ids)),
    }


def main() -> None:
    for resultado in (validar_logs(), validar_encuesta(), validar_incidentes()):
        print(f"\n== {resultado['archivo']} ==")
        for clave, valor in resultado.items():
            if clave != "archivo":
                print(f"{clave}: {valor}")


if __name__ == "__main__":
    main()
