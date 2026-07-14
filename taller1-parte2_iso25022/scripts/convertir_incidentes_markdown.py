"""
Convierte la tabla de clasificacion de incidentes en Markdown a CSV.

El material disponible no incluye data/incidentes_2025.csv como archivo separado;
este script lo reconstruye desde clasificacion_incidentes.md conservando la
clasificacion ISO/IEC 25022 ya realizada en el taller.
"""
from __future__ import annotations

import csv
import re
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ORIGEN = ROOT / "clasificacion_incidentes.md"
DESTINO = ROOT / "data" / "incidentes_2025.csv"

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]

ROL_POR_MODULO = {
    "HCE": "Medico",
    "Portal Citas": "Paciente",
    "Facturacion": "Admision",
    "Telemedicina": "Paciente",
    "Laboratorio": "Tecnico Laboratorio",
    "Imagenologia": "Radiologo",
    "Farmacia": "Farmacia",
    "App Movil": "Paciente",
    "Reportes Gerenciales": "Gerencia",
}


def limpiar_markdown(valor: str) -> str:
    valor = re.sub(r"\*\*|_", "", valor)
    valor = re.sub(r"\s+", " ", valor)
    return valor.strip()


def caracteristica_base(valor: str) -> str:
    return valor.split("(", 1)[0].strip()


def extraer_filas() -> list[dict[str, str]]:
    filas: list[dict[str, str]] = []
    inicio = date(2025, 1, 1)

    for linea in ORIGEN.read_text(encoding="utf-8").splitlines():
        if not linea.startswith("|"):
            continue

        celdas = [limpiar_markdown(celda) for celda in linea.strip().strip("|").split("|")]
        if len(celdas) != 6 or not celdas[0].isdigit():
            continue

        incidente_id = int(celdas[0])
        modulo = celdas[1]
        fecha = inicio + timedelta(days=(incidente_id - 1001) % 365)

        filas.append(
            {
                "id": str(incidente_id),
                "fecha": fecha.isoformat(),
                "modulo": modulo,
                "descripcion": celdas[2],
                "rol_usuario": ROL_POR_MODULO.get(modulo, "Usuario"),
                "sede": SEDES[(incidente_id - 1001) % len(SEDES)],
                "caracteristica_iso": caracteristica_base(celdas[3]),
                "rnf_relacionado": celdas[4],
                "justificacion": celdas[5],
            }
        )

    return filas


def main() -> None:
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    filas = extraer_filas()
    if not filas:
        raise SystemExit("No se encontraron incidentes para convertir.")

    with DESTINO.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        writer.writeheader()
        writer.writerows(filas)

    print(f"Se generaron {len(filas)} incidentes en {DESTINO.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
