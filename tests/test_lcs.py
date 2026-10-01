"""Pruebas de Parte 3; KMP se integra cuando esté disponible."""

from pathlib import Path
import sys
from time import perf_counter
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def setUpModule():
    global _best_prefix_match, longest_common_substring, prefix_function
    if not (ROOT / "src" / "kmp.py").exists():
        # Una copia temporal puede suministrarse por PYTHONPATH al validar.
        import importlib.util
        if importlib.util.find_spec("kmp") is None:
            raise unittest.SkipTest("Pendiente src/kmp.py de Parte 1")
    from kmp import prefix_function
    from lcs import _best_prefix_match, longest_common_substring


class PrefixMatchTests(unittest.TestCase):
    def test_prefix_table_example(self):
        self.assertEqual(prefix_function("ABC#XABY"), [0, 0, 0, 0, 0, 1, 2, 0])

    def test_partial_match(self):
        self.assertEqual(_best_prefix_match("ABC", "XABY"), 2)

    def test_no_match(self):
        self.assertEqual(_best_prefix_match("ZZZ", "XABY"), 0)

    def test_empty_b(self):
        self.assertEqual(_best_prefix_match("ABC", ""), 0)

    def test_only_b_zone_counts(self):
        self.assertEqual(_best_prefix_match("AAAA", "B"), 0)


class LongestCommonSubstringTests(unittest.TestCase):
    def test_middle_of_both(self):
        self.assertEqual(longest_common_substring("XABCDEY", "ZZBCDEQ"), (3, 6))

    def test_identical(self):
        self.assertEqual(longest_common_substring("ABC", "ABC"), (1, 3))

    def test_contained(self):
        self.assertEqual(longest_common_substring("0ABC9", "ABC"), (2, 4))

    def test_a_contained_in_b(self):
        self.assertEqual(longest_common_substring("ABC", "0ABC9"), (1, 3))

    def test_no_common_characters(self):
        self.assertEqual(longest_common_substring("ABC", "XYZ"), (0, 0))

    def test_tie_chooses_first_start_in_a(self):
        self.assertEqual(longest_common_substring("AB0CD", "CD1AB"), (1, 2))

    def test_start_of_a_end_of_b(self):
        self.assertEqual(longest_common_substring("ABC0", "9ABC"), (1, 3))

    def test_end_of_a(self):
        self.assertEqual(longest_common_substring("0ABC", "ABC9"), (2, 4))

    def test_repeated_characters(self):
        self.assertEqual(longest_common_substring("AAAAA", "AAA"), (1, 3))

    def test_empty_inputs(self):
        for a, b in [("", "ABC"), ("ABC", ""), ("", "")]:
            with self.subTest(a=a, b=b):
                self.assertEqual(longest_common_substring(a, b), (0, 0))

    def test_two_thousand_characters_under_ten_seconds(self):
        start = perf_counter()
        self.assertEqual(longest_common_substring("A" * 2000, "A" * 2000), (1, 2000))
        self.assertLess(perf_counter() - start, 10)

    @unittest.skipUnless((ROOT / "src" / "io_utils.py").exists(),
                         "Pendiente read_clean de Parte 1")
    def test_files_with_read_clean(self):
        from io_utils import read_clean
        fixture = ROOT / "tests" / "fixtures" / "integration"
        a = read_clean(str(fixture / "transmission1.txt"))
        b = read_clean(str(fixture / "transmission2.txt"))
        self.assertEqual(a, "0ABACDEF")
        self.assertEqual(b, "9ABAFDEF")
        self.assertEqual(longest_common_substring(a, b), (2, 4))


if __name__ == "__main__":
    unittest.main()
