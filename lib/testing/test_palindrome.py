import pytest
from lib.palindrome import longest_palindromic_substring


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("cbbd", "bb"),
        ("racecar", "racecar"),
        ("a", "a"),
    ]
)
def test_known_palindromes(input_str, expected):
    assert longest_palindromic_substring(input_str) == expected


def test_babad_returns_valid_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_ac_returns_single_character():
    result = longest_palindromic_substring("ac")
    assert result in ["a", "c"]


def test_empty_string():
    assert longest_palindromic_substring("") == ""


def test_all_same_characters():
    assert longest_palindromic_substring("aaaa") == "aaaa"


def test_no_repeating_characters():
    result = longest_palindromic_substring("abcdef")
    assert len(result) == 1
    assert result in "abcdef"


def test_even_length_palindrome():
    assert longest_palindromic_substring("abccba") == "abccba"


def test_odd_length_palindrome():
    assert longest_palindromic_substring("madam") == "madam"


def test_palindrome_in_middle():
    assert longest_palindromic_substring("xyzracecarabc") == "racecar"


def test_long_string():
    s = "a" * 100
    assert longest_palindromic_substring(s) == s


def test_numeric_string():
    assert longest_palindromic_substring("12321") == "12321"


def test_alphanumeric_string():
    assert longest_palindromic_substring("ab12321cd") == "12321"