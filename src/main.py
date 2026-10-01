from io_utils import read_clean
from kmp import kmp_search, format_result
from manacher import longest_palindrome
from lcs import longest_common_substring

def main():
    transmissions = [
        read_clean("examples/transmission1.txt"),
        read_clean("examples/transmission2.txt"),
    ]
    mcodes = [
        read_clean("examples/mcode1.txt"),
        read_clean("examples/mcode2.txt"),
        read_clean("examples/mcode3.txt"),
    ]

    for transmission in transmissions:
        for mcode in mcodes:
            print(format_result(kmp_search(transmission, mcode)))

    for transmission in transmissions:
        ini, fin = longest_palindrome(transmission)
        print(ini, fin)


    ini, fin = longest_common_substring(transmissions[0], transmissions[1])
    print(ini, fin)


if __name__ == "__main__":
    main()
