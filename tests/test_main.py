"""Prueba real por subprocess; no reemplaza main con un stub."""

from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "integration"
# Calculado a mano: ABA comienza en 2 en ambas; DEF comienza en 6;
# 123 está ausente. ABA es el mayor palíndromo en ambas (2..4).
# ABA y DEF empatan como substring común; gana ABA (2..4 en t1).
EXPECTED_STDOUT = "true 2\ntrue 6\nfalse\ntrue 2\ntrue 6\nfalse\n2 4\n2 4\n2 4\n"
REQUIRED = ("main.py", "kmp.py", "io_utils.py", "manacher.py")


class MainTests(unittest.TestCase):
    @unittest.skipUnless(all((ROOT / "src" / name).exists() for name in REQUIRED),
                         "Pendientes módulos de Partes 1 y 2")
    def test_nine_lines_from_files(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "src" / "main.py")],
            cwd=FIXTURE, capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, EXPECTED_STDOUT)


if __name__ == "__main__":
    unittest.main()
