#!/usr/bin/env python2

""" Unittest class IntermediateRepresentation. """

import IntermediateRepresentation
import Instruction
import unittest


class IntermediateRepresentationTest(unittest.TestCase):

    def testInstructionCreation(self):
        ir = IntermediateRepresentation.IntermediateRepresentation()
        nop = ir.createNop()
        self.assertEqual(nop.opcode, Instruction.OC_NOP)


if __name__ == '__main__':
    unittest.main()

