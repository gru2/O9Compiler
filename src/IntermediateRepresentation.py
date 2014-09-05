#!/usr/bin/env python2

""" Implementation of class IntermediateRepresentation. """

import Instruction
import ResourceClass


class IntermediateRepresentation:

    def __init__(self):
        self.abstractRegisterResourceClass = None

    def initResourceClasses(self):
        self.abstractRegisterResourceClass = ResourceClass.ResourceClass()
        rc = self.abstractRegisterResourceClass
        rc.name = "abstract register"

    def createNop(self):
        insn = Instruction.Instruction()
        insn.opcode = Instruction.OC_NOP
        return insn
