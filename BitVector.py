#!/usr/bin/env python2

""" Implementation of BitVector class. """

class BitVector:

    def __init__(self):
        self.data = []

    def get(self, index):
        if index >= len(self.data):
            return False
        return self.data[index]

    def set(self, index, value):
        assert value == True or value == False
        while index >= len(self.data):
            self.data.append(False)
        self.data[index] = value

    def reset(self):
        self.data = []
