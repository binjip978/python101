import unittest

def length_of_the_string(s):
    '''
    return length of the string
    "hello" -> 5
    "" -> 0
    "hello world" -> 11
    '''
    pass

def symbol_n(s, n):
    '''
    return n-th symbol from the string
    symbol_n("hello", 0) -> "h"
    symbol_n("hello", 4) -> "o"
    symbol_n("hello", 2) -> "l"
    '''
    pass

def capitalize(s):
    '''
    return capitalize string
    "hello" -> "Hello"
    "" -> ""
    "hello world" -> "Hello world"
    '''
    pass

def concat(s1, s2):
    '''
    return concatinated strings
    "a", "b"    -> "ab"
    "a", ""     -> "a"
    "a", " "    -> "a "
    '''
    pass

def contains(sub, s):
    '''
    return True if sub contains in s
    contains("hello", "hello world") -> True
    contains("a", "b") -> False
    '''
    pass

def prefix_of_length_n(s, n):
    '''
    return prefix of string n
    prefix_of_length_n("hello", 2) -> "he"
    prefix_of_length_n("", 2) -> ""
    prefix_of_length_n("ab", 2) -> "ab"
    '''
    pass

def suffix_of_length_n(s, n):
    '''
    return suffix of string n
    suffix_of_length_n("hello", 2) -> "lo"
    suffix_of_length_n("", 2) -> ""
    suffix_of_length_n("ab", 2) -> "ab")
    '''
    pass

def substring_from_n_to_k(s, n, k):
    '''
    return substring s [n, k)
    substring_from_n_to_k("hello", 0, 2) -> "he"
    substring_from_n_to_k("hello", 0, 0) -> ""
    substring_from_n_to_k("hello", 1, 3) -> "el"
    substring_from_n_to_k("hello", 0, 5) -> "hello"
    '''
    pass


class TestStrings(unittest.TestCase):
    def test_lenght(self):
        self.assertEqual(length_of_the_string("hello"), 5)
        self.assertEqual(length_of_the_string(""), 0)
        self.assertEqual(length_of_the_string("hello world"), 11)

    def test_capitalize(self):
        self.assertEqual(capitalize("hello"), "Hello")
        self.assertEqual(capitalize(""), "")
        self.assertEqual(capitalize("hello world"), "Hello world")

    def test_concat(self):
        self.assertEqual(concat("a", "b"), "ab")
        self.assertEqual(concat("a", ""), "a")
        self.assertEqual(concat("a", " "), "a ")

    def test_contains(self):
        self.assertTrue(contains("hello", "hello world"))
        self.assertFalse(contains("a", "b"))

    def test_prefix(self):
        self.assertEqual(prefix_of_length_n("hello", 2), "he")
        self.assertEqual(prefix_of_length_n("", 2), "")
        self.assertEqual(prefix_of_length_n("ab", 2), "ab")

    def test_symbol_n(self):
        self.assertEqual(symbol_n("hello", 0), "h")
        self.assertEqual(symbol_n("hello", 4), "o")
        self.assertEqual(symbol_n("hello", 2), "l")
    
    def test_substring(self):
        self.assertEqual(substring_from_n_to_k("hello", 0, 2), "he")
        self.assertEqual(substring_from_n_to_k("hello", 0, 0), "")
        self.assertEqual(substring_from_n_to_k("hello", 1, 3), "el")
        self.assertEqual(substring_from_n_to_k("hello", 0, 5), 
                         "hello")


if __name__ == '__main__':
    unittest.main()
