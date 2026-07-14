"""
Genera respuestas CSAT simuladas para usuarios de MediSalud HIS.
"""
from __future__ import annotations

import csv
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SALIDA = ROOT / "data" / "encuesta_satisfaccion.csv"

random.seed(25022)

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
ROLES = ["Medico", "Enfermeria", "Paciente", "Admision", "Farmacia", "Gerencia"]
COMENTARIOS = {
    1: "Flujo lento y confuso; no pude terminar la tarea sin ayuda.",
    2: "La tarea se completo, pero con errores o demasiada espera.",
    3: "Experiencia aceptable, aunque requiere mejoras en claridad y tiempos.",
    4: "El sistema permitio completar la tarea con pocas fricciones.",
    5: "Experiencia fluida, clara y confiable durante la tarea.",
}


def generar_filas(total: int = 150) -> list[dict[str, object]]:
    filas: list[dict[str, object]] = []

    for respuesta_id in range(1, total + 1):
        sede = random.choice(SEDES)
        rol = random.choice(ROLES)

        media = 3.8
        if sede in ("Quito", "Guayaquil"):
            media -= 0.35
        if rol in ("Medico", "Paciente"):
            media -= 0.25

        puntaje = round(random.gauss(media, 0.9))
        puntaje = min(5, max(1, puntaje))

        filas.append(
            {
                "respuesta_id": respuesta_id,
                "sede": sede,
                "rol": rol,
                "puntaje_csat": puntaje,
                "comentario": COMENTARIOS[puntaje],
            }
        )

    return filas


def main() -> None:
    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    filas = generar_filas()

    with SALIDA.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=list(filas[0].keys()))
        writer.writeheader()
        writer.writerows(filas)

    print(f"Se generaron {len(filas)} respuestas en {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
