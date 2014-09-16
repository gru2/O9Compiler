#!/usr/bin/env python2

""" Implementation of class CodeEmitter. """

import Instruction


class CodeEmitter:

    def __init__(self):
        self.instructionTemplates = {}
        self.outputStream = None

    def emitInstruction(self, instruction):
        s = self.instructionToString(instruction)
        self.emitString(s)

    def instructionToString(self, instruction):
        template = self.findTemplate(instruction.opcode)
        s = self.replaceOperands(instruction, template)
        return s

    def operandToString(self, operand):
        return "r"

    def findTemplate(self, opcode):
        if self.instructionTemplates.has_key(opcode):
            return self.instructionTemplates[opcode]
        return "\tUNKNOWN_INSTRUCTION\n"

    def emitString(self, s):
        assert self.outputStream != None
        self.outputStream.write(s)

    def replaceOperands(self, instruction, template):
        s = template
        return s

    def addVirtualInstructionTemplates(self):
        i = Instruction
        t = { i.OC_NOP : "NOP", i.OC_JMP : "JMP\t%1", i.OC_CALL : "CALL\t%1", \
            i.OC_RET : "RET\t%1", i.OC_MOVE : "MOVE\t%1 %2", \
            i.OC_ADD : "ADD\t%1 %2 %3", i.OC_SUB : "SUB\t%1 %2 %3", \
            i.OC_MUL : "MUL\t%1 %2 %3", i.OC_DIV : "DIV\t%1 %2 %3", \
            i.OC_NEG : "NEG\t%1 %2", i.OC_AND : "AND\t%1 %2 %3", \
            i.OC_OR : "OR\t%1 %2 %3", i.OC_XOR : "XOR\t%1 %2 %3", \
            i.OC_NOT : "NOT\t%1 %2", \
            i.OC_EQ : "EQ\t%1 %2 %3", i.OC_NEQ : "NEQ\t%1 %2 %3", \
            i.OC_LT : "LT\t%1 %2 %3", i.OC_LE : "LE\t%1 %2 %3", \
            i.OC_GT : "GT\t%1 %2 %3", i.OC_GE : "GE\t%1 %2 %3", \
            i.OC_LOAD : "LOAD\t%1 %2", i.OC_STORE : "STORE\t%1 %2", \
            i.OC_BEGFN : "BEGFN", i.OC_ENDFN : "ENDFN", \
            i.OC_ARG : "ARG\t%1 %2", i.OC_VAR : "VAR\t%1 %2" }

        for opcode in t:
            self.instructionTemplates[opcode] = "\t" + t[opcode] + "\n"

        self.instructionTemplates[i.OC_LABEL] = "%1:\n"

