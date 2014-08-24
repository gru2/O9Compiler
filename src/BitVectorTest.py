#!/usr/bin/env python2

""" Unittest for class BitVector. """

import BitVector
import unittest

class BitVectorTest(unittest.TestCase):

    def test01(self):
        x = BitVector.BitVector()
        r = x.get(3)
        self.assertEqual(r, False)
        r = x.get(0)
        self.assertEqual(r, False)
        x.set(0, True)
        r = x.get(0)
        self.assertEqual(r, True)
        x.reset()
        r = x.get(0)
        self.assertEqual(r, False)
        x.set(4, True)
        r = x.get(3)
        self.assertEqual(r, False)
        r = x.get(4)
        self.assertEqual(r, True)
        r = x.get(5)
        self.assertEqual(r, False)


if __name__ == '__main__':
    unittest.main()

