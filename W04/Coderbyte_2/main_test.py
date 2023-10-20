from __future__ import annotations

import unittest
from string_builder import StringBuilder

class TestStringBuilder(unittest.TestCase):
    
    def test_string_builder_simple(self):
        string = StringBuilder()
        self.assertEqual(str(string), "")

        string = StringBuilder("Hello World")
        self.assertEqual(str(string), "Hello World")

        with self.assertRaises(Exception):
            string = StringBuilder("Hello World", 5)

        self.assertEqual(string.size(), 11)
        self.assertEqual(string.char_at(2), 'l')

        self.assertEqual(string.substring(0, 5), 'Hello')
        self.assertEqual(string.substring(6), 'World')

        string.append(". This is my first program")
        self.assertEqual(string.size(), 37)
        self.assertEqual(string.char_at(36), 'm')

        with self.assertRaises(Exception):
            string.substring(100)
        with self.assertRaises(Exception):
            string.substring(1,0)
        with self.assertRaises(Exception):
            string.substring(-1)
        with self.assertRaises(Exception):
            string.substring(0, 38)

    def test_string_builder_replace(self):
        string = StringBuilder("abc", 10)
        string.replace("a", "dc")
        self.assertEqual(str(string), "dcbc")

        string = StringBuilder("aaa", 11)
        string.replace("a", "aa")
        self.assertEqual(str(string), "aaaaaa")

        with self.assertRaises(Exception):
            string.replace("a", "aa")

    def test_string_builder_reverse(self):
        string = StringBuilder("Hello World", 20)
        self.assertEqual(str(string.reverse()), "dlroW olleH")
        self.assertEqual(str(string), "dlroW olleH")
        self.assertEqual(string.char_at(1), 'l')
        self.assertEqual(string.size(), 11)

    def test_string_builder_delete(self):
        string = StringBuilder("Hello World", 20)
        with self.assertRaises(Exception):
            string.delete(-1)
        with self.assertRaises(Exception):
            string.delete(11)
        with self.assertRaises(Exception):
            string.delete(2, 0)
        with self.assertRaises(Exception):
            string.delete(0, 12)
        string.delete(0, 6)
        self.assertEqual(string.size(), 5)
        self.assertEqual(str(string), "World")  

    def test_append_performance(self):
        string = StringBuilder("", 10000)
        for i in range(10000):
            string.append("a")
        self.assertEqual(string.size(), 10000)