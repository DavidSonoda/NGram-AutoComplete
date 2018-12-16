#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from ngram_mapper import *

class TestMapperFunc(unittest.TestCase):
    """
    Test mapper functions
    """

    def test_brackets_closed(self):
        test_str1 = '(单元复习)'
        test_str2 = '（单元'
        self.assertEqual(True, brackets_closed(test_str1))
        self.assertEqual(False, brackets_closed(test_str2))

    def test_is_chn_char(self):
        test_str1 = '啊'
        test_str2 = '？'
        self.assertEqual(True, is_chn_char(test_str1[0]))
        self.assertEqual(False, is_chn_char(test_str2[0]))

    def test_is_valid_key(self):
        test_str1 = ':'
        test_str2 = '啊？'
        self.assertEqual(False, is_valid_key(test_str1))
        self.assertEqual(True, is_valid_key(test_str2))


# def test_func():
#     test_str1 = '(单元'
#     # test_str2 = '（单元'
#     print(brackets_closed(test_str1))
#     # self.assertEqual(False, brackets_closed(test_str2))

if __name__ == '__main__':
    unittest.main()
    # test_func()