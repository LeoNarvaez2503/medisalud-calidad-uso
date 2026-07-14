"""
Exporta los indicadores calculados a JSON para dashboards.
"""
from __future__ import annotations

import json
from pathlib import Path

from metricas_iso25022 import ROOT, generar_reporte


SALIDA = ROOT / "dashboards" / "indicadores.json"


def main() -> None:
    reporte, eficiencia_sede = generar_reporte()
    salida = {
        "sistema": "MediSalud HIS",
        "norma": "ISO/IEC 25022",
        "periodo": "2025",
        "metricas": reporte,
        "eficiencia_por_sede": eficiencia_sede,
    }

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    with SALIDA.open("w", encoding="utf-8") as archivo:
        json.dump(salida, archivo, indent=2, ensure_ascii=False)

    print(f"Reporte exportado a {SALIDA.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
