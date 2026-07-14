import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from metricas_iso25022 import metrica_eficiencia


class TestMetricasISO25022(unittest.TestCase):
    def test_metrica_eficiencia_promedia_tiempos(self):
        logs = [
            {"tiempo_segundos": "4", "completada": "1"},
            {"tiempo_segundos": "6", "completada": "1"},
            {"tiempo_segundos": "8", "completada": "0"},
        ]

        resultado = metrica_eficiencia(logs)

        self.assertEqual(resultado["valor"], 6.0)
        self.assertIs(resultado["cumple"], True)


if __name__ == "__main__":
    unittest.main()
