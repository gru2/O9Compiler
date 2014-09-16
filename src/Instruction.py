#!/usr/bin/env python2

""" Implementation of class Instruction. """

OC_NOP = "NOP"

OC_LABEL = "LABEL"

OC_JMP = "JMP"
OC_CALL = "CALL"
OC_RET = "RET"

OC_MOVE = "MOVE"

OC_ADD = "ADD"
OC_SUB = "SUB"
OC_MUL = "MUL"
OC_DIV = "DIV"
OC_NEG = "NEG"

OC_AND = "AND"
OC_OR = "OR"
OC_XOR = "XOR"
OC_NOT = "NOT"

OC_EQ = "EQ"
OC_NEQ = "NEQ"
OC_LT = "LT"
OC_LE = "LE"
OC_GT = "GT"
OC_GE = "GE"

OC_LOAD = "LOAD"
OC_STORE = "STORE"

OC_BEGFN = "BEGFN"
OC_ENDFN = "ENDFN"

OC_ARG = "ARG"
OC_VAR = "VAR"


class Instruction:

    def __init__(self):
        self.opcode = OC_NOP
        self.operands = []
