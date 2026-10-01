import time
import unittest
from src.manacher import _transform, longest_palindrome


class TransformTests(unittest.TestCase):
    def test_transform_examples(self):
        self.assertEqual(_transform("AB"), "#A#B#")
        self.assertEqual(_transform("ABBA"), "#A#B#B#A#")


class LongestPalindromeTests(unittest.TestCase):
    def test_odd_palindrome(self):
        self.assertEqual(longest_palindrome("XABCBAY"), (2, 6))

    def test_even_palindrome(self):
        self.assertEqual(longest_palindrome("XABBAY"), (2, 5))

    def test_whole_string_is_palindrome(self):
        self.assertEqual(longest_palindrome("ABCBA"), (1, 5))
        self.assertEqual(longest_palindrome("ABBA"), (1, 4))

    def test_palindrome_at_start(self):
        self.assertEqual(longest_palindrome("ABBAXYZ"), (1, 4))

    def test_palindrome_at_end(self):
        self.assertEqual(longest_palindrome("XYZABBA"), (4, 7))

    def test_tie_returns_first(self):
        self.assertEqual(longest_palindrome("ABAXCDC"), (1, 3))
        self.assertEqual(longest_palindrome("AAXBB"), (1, 2))

    def test_single_char(self):
        self.assertEqual(longest_palindrome("A"), (1, 1))

    def test_no_real_palindrome(self):
        self.assertEqual(longest_palindrome("ABCDEF"), (1, 1))

    def test_long_string_is_linear(self):
        s = "A" * 5000
        inicio = time.perf_counter()
        resultado = longest_palindrome(s)
        duracion = time.perf_counter() - inicio
        self.assertEqual(resultado, (1, 5000))
        self.assertLess(duracion, 1)

    def test_long_string_with_planted_palindrome(self):
        s = "0123456789ABCDEF" * 300 + "XYZZYX" + "0123456789ABCDEF" * 20
        inicio = 16 * 300 + 1
        self.assertEqual(longest_palindrome(s), (inicio, inicio + 5))


if __name__ == "__main__":
    unittest.main()
