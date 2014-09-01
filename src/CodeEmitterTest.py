#!/usr/bin/env python2

""" Unittest class CodeEmitter. """

import CodeEmitter
import IntermediateRepresentation
import unittest


class CodeEmitterTest(unittest.TestCase):

    def test01(self):
        ce = CodeEmitter.CodeEmitter()
        ce.addAbstractInstructionTemplates()
        ir = IntermediateRepresentation.IntermediateRepresentation()
        insn  = ir.createNop()
        s = ce.instructionToString(insn)
        self.assertEqual(s, "\tNOP\n")


if __name__ == '__main__':
    unittest.main()

