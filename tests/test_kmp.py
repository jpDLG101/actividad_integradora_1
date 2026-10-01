import unittest
from pathlib import Path
from src.io_utils import read_clean
from src.kmp import format_result, kmp_search, prefix_function


PROJECT_ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = PROJECT_ROOT / "examples"


class PrefixFunctionTests(unittest.TestCase):
    def test_prefix_function_examples(self):
        self.assertEqual(prefix_function("ABABC"), [0, 0, 1, 2, 0])
        self.assertEqual(prefix_function("AAAA"), [0, 1, 2, 3])
        self.assertEqual(prefix_function("ABCD"), [0, 0, 0, 0])
        self.assertEqual(prefix_function(""), [])


class KmpSearchTests(unittest.TestCase):
    def test_match_at_start(self):
        self.assertEqual(kmp_search("ABABCABAB", "ABAB"), 1)

    def test_match_at_end(self):
        self.assertEqual(kmp_search("ABABCABAB", "CAB"), 5)

    def test_pattern_equals_text(self):
        self.assertEqual(kmp_search("ABCD", "ABCD"), 1)

    def test_pattern_longer_than_text(self):
        self.assertIsNone(kmp_search("A", "AB"))

    def test_empty_pattern(self):
        self.assertIsNone(kmp_search("ABC", ""))

    def test_overlapping_matches_return_first(self):
        self.assertEqual(kmp_search("AAAA", "AAA"), 1)

    def test_classic_kmp_fallback_case(self):
        self.assertEqual(kmp_search("AAAAAAB", "AAAB"), 4)

    def test_no_match_returns_none(self):
        self.assertIsNone(kmp_search("ABABCABAB", "XYZ"))

    def test_searches_example_files(self):
        transmission = read_clean(str(EXAMPLES / "transmission1.txt"))
        mcode1 = read_clean(str(EXAMPLES / "mcode1.txt"))
        mcode2 = read_clean(str(EXAMPLES / "mcode2.txt"))

        self.assertEqual(kmp_search(transmission, mcode1), 6)
        self.assertIsNone(kmp_search(transmission, mcode2))

    def test_format_result(self):
        self.assertEqual(format_result(5), "true 5")
        self.assertEqual(format_result(None), "false")


if __name__ == "__main__":
    unittest.main()
