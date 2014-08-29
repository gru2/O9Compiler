#!/usr/bin/env python2

""" Implementation of class Instruction. """

OC_NOP = "NOP"

OP_MOVE = "MOVE"

OP_JMP = "JMP"
OP_CALL = "CALL"
OP_RET = "RET"

OP_ADD = "ADD"
OP_SUB = "SUB"
OP_MUL = "MUL"
OP_DIV = "DIV"
OP_NEG = "NEG"

OP_AND = "AND"
OP_OR = "OR"
OP_XOR = "XOR"
OP_NOT = "NOT"

OP_EQ = "EQ"
OP_NEQ = "NEQ"
OP_LT = "LT"
OP_LE = "LE"
OP_GT = "GT"
OP_GE = "GE"


class Instruction:

    def __init__(self):
        self.opcode = OC_NOP
        self.operands = []
