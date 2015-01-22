#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import unittest

from pro020 import factors
from pro017 import less_than_1000


class ProblemTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_problem12(self):
        self.assertEqual(factors(1), 1)
        self.assertEqual(factors(3), 6)
        self.assertNotEqual(factors(4), 23)

    def test_less_than_1000(self):
        self.assertEqual(less_than_1000(1000), ['one', 'thousand'])


if __name__ == '__main__':
    unittest.main()

