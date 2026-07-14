"""
Modulo de calculo de metricas de Calidad en Uso (ISO/IEC 25022)
para el sistema MediSalud HIS.
"""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]

UMBRAL_TIEMPO_TAREA = 8.0
UMBRAL_P90_TIEMPO_TAREA = 0.90
UMBRAL_TASA_ERROR_FACT = 0.01
UMBRAL_EFECTIVIDAD = 0.95
UMBRAL_SATISFACCION = 0.80
UMBRAL_COBERTURA_CONTEXTO = 0.85


def cargar_csv(nombre: str) -> list[dict[str, str]]:
    with (ROOT / "data" / nombre).open(newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def cargar_datos() -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    logs = cargar_csv("logs_hce.csv")
    encuesta = cargar_csv("encuesta_satisfaccion.csv")
    incidentes = cargar_csv("incidentes_2025.csv")
    return logs, encuesta, incidentes


def metrica_efectividad(logs: list[dict[str, str]]) -> dict[str, object]:
    total = len(logs)
    completadas = sum(int(fila["completada"]) for fila in logs)
    valor = round(completadas / total, 4) if total else 0.0
    return {
        "nombre": "Completitud de registro de HCE",
        "caracteristica": "Efectividad",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_EFECTIVIDAD,
        "cumple": valor >= UMBRAL_EFECTIVIDAD,
    }


def metrica_eficiencia(logs: list[dict[str, str]]) -> dict[str, object]:
    tiempos = [float(fila["tiempo_segundos"]) for fila in logs]
    valor = round(mean(tiempos), 2)
    return {
        "nombre": "Tiempo promedio de registro de HCE",
        "caracteristica": "Eficiencia",
        "valor": valor,
        "unidad": "segundos",
        "umbral": UMBRAL_TIEMPO_TAREA,
        "cumple": valor <= UMBRAL_TIEMPO_TAREA,
    }


def metrica_rnf_01(logs: list[dict[str, str]]) -> dict[str, object]:
    total = len(logs)
    en_umbral = sum(1 for fila in logs if float(fila["tiempo_segundos"]) <= UMBRAL_TIEMPO_TAREA)
    valor = round(en_umbral / total, 4) if total else 0.0
    return {
        "nombre": "Notas HCE registradas en 8 segundos o menos",
        "caracteristica": "Eficiencia",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_P90_TIEMPO_TAREA,
        "cumple": valor >= UMBRAL_P90_TIEMPO_TAREA,
    }


def metrica_satisfaccion(encuesta: list[dict[str, str]]) -> dict[str, object]:
    puntajes = [int(fila["puntaje_csat"]) for fila in encuesta]
    valor = round(mean(puntajes) / 5, 4)
    return {
        "nombre": "Indice de satisfaccion CSAT normalizado",
        "caracteristica": "Satisfaccion",
        "valor": valor,
        "unidad": "proporcion (0-1)",
        "umbral": UMBRAL_SATISFACCION,
        "cumple": valor >= UMBRAL_SATISFACCION,
    }


def metrica_libertad_riesgo(incidentes: list[dict[str, str]], total_transacciones: int) -> dict[str, object]:
    errores_facturacion = [
        fila
        for fila in incidentes
        if fila["modulo"] == "Facturacion" and fila["caracteristica_iso"] == "Libertad de Riesgo"
    ]
    valor = round(len(errores_facturacion) / total_transacciones, 4)
    return {
        "nombre": "Tasa de errores de facturacion con riesgo economico",
        "caracteristica": "Libertad de Riesgo",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_TASA_ERROR_FACT,
        "cumple": valor <= UMBRAL_TASA_ERROR_FACT,
    }


def metrica_cobertura_contexto(logs: list[dict[str, str]]) -> dict[str, object]:
    promedios = metrica_eficiencia_por_sede(logs)
    valores = [fila["tiempo_promedio_segundos"] for fila in promedios]
    mejor = min(valores)
    peor = max(valores)
    valor = round(mejor / peor, 4) if peor else 0.0
    return {
        "nombre": "Consistencia de eficiencia entre sedes",
        "caracteristica": "Cobertura de Contexto",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_COBERTURA_CONTEXTO,
        "cumple": valor >= UMBRAL_COBERTURA_CONTEXTO,
    }


def metrica_eficiencia_por_sede(logs: list[dict[str, str]]) -> list[dict[str, object]]:
    tiempos_por_sede: dict[str, list[float]] = defaultdict(list)
    for fila in logs:
        tiempos_por_sede[fila["sede"]].append(float(fila["tiempo_segundos"]))

    return [
        {
            "sede": sede,
            "tiempo_promedio_segundos": round(mean(tiempos), 2),
            "eventos": len(tiempos),
        }
        for sede, tiempos in sorted(tiempos_por_sede.items())
    ]


def generar_reporte() -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    logs, encuesta, incidentes = cargar_datos()

    reporte = {
        "efectividad": metrica_efectividad(logs),
        "eficiencia": metrica_eficiencia(logs),
        "rnf_01": metrica_rnf_01(logs),
        "satisfaccion": metrica_satisfaccion(encuesta),
        "libertad_riesgo": metrica_libertad_riesgo(incidentes, total_transacciones=8500),
        "cobertura_contexto": metrica_cobertura_contexto(logs),
    }

    return reporte, metrica_eficiencia_por_sede(logs)


def main() -> None:
    reporte, eficiencia_sede = generar_reporte()

    print("=== Reporte de Calidad en Uso - MediSalud HIS ===\n")
    for metrica in reporte.values():
        estado = "CUMPLE" if metrica["cumple"] else "NO CUMPLE"
        print(
            f"{metrica['nombre']}: {metrica['valor']} {metrica['unidad']} "
            f"(umbral: {metrica['umbral']}) -> {estado}"
        )

    print("\n=== Eficiencia por sede (Cobertura de Contexto) ===")
    for fila in eficiencia_sede:
        print(f"{fila['sede']}: {fila['tiempo_promedio_segundos']} s ({fila['eventos']} eventos)")


if __name__ == "__main__":
    main()
