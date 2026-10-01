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
# t1: 0123456789ABCDE; t2: FEDCB9876543210. Solo t1 contiene
# 56789 (posición 6). No hay palíndromos mayores a un carácter;
# tampoco substrings comunes de largo > 1. Gana la posición 1.
EXAMPLES_STDOUT = "true 6\nfalse\nfalse\nfalse\nfalse\nfalse\n1 1\n1 1\n1 1\n"


class MainTests(unittest.TestCase):
    def assert_output(self, directory, expected):
        result = subprocess.run(
            [sys.executable, str(ROOT / "src" / "main.py")],
            cwd=directory, capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, expected)

    def test_nine_lines_from_files(self):
        self.assert_output(FIXTURE, EXPECTED_STDOUT)

    def test_nine_lines_from_team_examples(self):
        self.assert_output(ROOT / "examples", EXAMPLES_STDOUT)


if __name__ == "__main__":
    unittest.main()
