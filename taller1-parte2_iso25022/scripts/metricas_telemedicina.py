"""
Reto Final Integrador — Calculo de Metricas de Calidad en Uso (ISO/IEC 25022)
especificas para el modulo de Telemedicina 2.0 de MediSalud HIS.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DASH = ROOT / "dashboards"
LOGS_TELEMEDICINA = DATA / "logs_telemedicina.csv"
SALIDA_JSON = DASH / "indicadores_telemedicina.json"

UMBRAL_EFECTIVIDAD_TELE = 0.95  # 95% de exito (RNF-05)
UMBRAL_SATISFACCION_TELE = 0.80  # 4.0 de CSAT
UMBRAL_RIESGO_PRIVACIDAD = 0.005  # < 0.5% de exposicion incidental


def cargar_datos() -> list[dict[str, str]]:
    with LOGS_TELEMEDICINA.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def calcular_metricas(logs: list[dict[str, str]]) -> tuple[dict[str, dict], list[dict]]:
    total = len(logs)
    completadas = sum(1 for f in logs if int(f["completada"]) == 1)
    satisfacciones = [int(f["satisfaccion_paciente"]) for f in logs]
    incidentes_privacidad = sum(1 for f in logs if int(f["incidente_privacidad"]) == 1)

    # 1. Efectividad (Tasa de completacion)
    tasa_exito = round(completadas / total, 4) if total else 0.0

    # 2. Eficiencia (Duracion promedio de teleconsultas completadas)
    duraciones = [float(f["duracion_minutos"]) for f in logs if int(f["completada"]) == 1]
    duracion_promedio = round(mean(duraciones), 1) if duraciones else 0.0

    # 3. Satisfaccion (CSAT normalizado)
    csat_promedio = mean(satisfacciones) if satisfacciones else 0.0
    csat_normalizado = round(csat_promedio / 5, 4)

    # 4. Libertad de Riesgo (Tasa de incidentes de privacidad)
    tasa_privacidad = round(incidentes_privacidad / total, 4) if total else 0.0

    # 5. Cobertura de Contexto (Consistencia de exito entre conexiones)
    exito_por_conexion: dict[str, list[int]] = {}
    for f in logs:
        conn = f["tipo_conexion"]
        if conn not in exito_por_conexion:
            exito_por_conexion[conn] = []
        exito_por_conexion[conn].append(int(f["completada"]))

    tasa_por_conexion = {}
    for conn, vals in exito_por_conexion.items():
        tasa_por_conexion[conn] = round(sum(vals) / len(vals), 4)

    mejor_conn = max(tasa_por_conexion.values())
    peor_conn = min(tasa_por_conexion.values())
    consistencia_conexion = round(peor_conn / mejor_conn, 4) if mejor_conn else 0.0

    # Desglose por sede
    exito_por_sede: dict[str, list[int]] = {}
    for f in logs:
        sede = f["sede"]
        if sede not in exito_por_sede:
            exito_por_sede[sede] = []
        exito_por_sede[sede].append(int(f["completada"]))

    desglose_sedes = []
    for sede, vals in sorted(exito_por_sede.items()):
        desglose_sedes.append({
            "sede": sede,
            "total_intentos": len(vals),
            "completadas": sum(vals),
            "tasa_exito": round(sum(vals) / len(vals), 4),
        })

    reporte = {
        "efectividad": {
            "nombre": "Tasa de exito de teleconsulta",
            "caracteristica": "Efectividad",
            "valor": tasa_exito,
            "unidad": "proporcion",
            "umbral": UMBRAL_EFECTIVIDAD_TELE,
            "cumple": tasa_exito >= UMBRAL_EFECTIVIDAD_TELE,
        },
        "eficiencia": {
            "nombre": "Duracion promedio de teleconsulta",
            "caracteristica": "Eficiencia",
            "valor": duracion_promedio,
            "unidad": "minutos",
            "umbral": 30.0,
            "cumple": duracion_promedio <= 30.0,
        },
        "satisfaccion": {
            "nombre": "CSAT normalizado del paciente",
            "caracteristica": "Satisfaccion",
            "valor": csat_normalizado,
            "unidad": "proporcion (0-1)",
            "umbral": UMBRAL_SATISFACCION_TELE,
            "cumple": csat_normalizado >= UMBRAL_SATISFACCION_TELE,
        },
        "libertad_riesgo": {
            "nombre": "Tasa de incidentes de privacidad de datos",
            "caracteristica": "Libertad de Riesgo",
            "valor": tasa_privacidad,
            "unidad": "proporcion",
            "umbral": UMBRAL_RIESGO_PRIVACIDAD,
            "cumple": tasa_privacidad <= UMBRAL_RIESGO_PRIVACIDAD,
        },
        "cobertura_contexto": {
            "nombre": "Consistencia de exito por conexion",
            "caracteristica": "Cobertura de Contexto",
            "valor": consistencia_conexion,
            "unidad": "proporcion",
            "umbral": 0.85,
            "cumple": consistencia_conexion >= 0.85,
        }
    }

    return reporte, desglose_sedes


def exportar_dashboard(reporte: dict, desglose_sedes: list) -> None:
    salida = {
        "sistema": "MediSalud Telemedicina 2.0",
        "norma": "ISO/IEC 25022",
        "metricas": reporte,
        "desglose_por_sede": desglose_sedes,
    }
    DASH.mkdir(parents=True, exist_ok=True)
    with SALIDA_JSON.open("w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False)


def main() -> None:
    logs = cargar_datos()
    reporte, desglose_sedes = calcular_metricas(logs)

    print("=== Reto Final: Reporte Telemedicina 2.0 ===")
    for metrica in reporte.values():
        estado = "CUMPLE" if metrica["cumple"] else "NO CUMPLE"
        print(
            f"{metrica['nombre']}: {metrica['valor']} {metrica['unidad']} "
            f"(umbral: {metrica['umbral']}) -> {estado}"
        )

    print("\nTasa de exito por Sede:")
    for sede in desglose_sedes:
        print(f"  {sede['sede']}: {sede['tasa_exito'] * 100:.1f}% ({sede['completadas']}/{sede['total_intentos']} completadas)")

    exportar_dashboard(reporte, desglose_sedes)
    print(f"\nIndicadores guardados en {SALIDA_JSON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
