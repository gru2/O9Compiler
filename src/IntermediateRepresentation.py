#!/usr/bin/env python2

""" Implementation of class IntermediateRepresentation. """

import Instruction


class IntermediateRepresentation:

    def __init__(self):
        pass

    def createNop(self):
        insn = Instruction.Instruction()
        insn.opcode = Instruction.OC_NOP
        return insn
