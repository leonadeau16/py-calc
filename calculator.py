import tkinter as tk 

class Calculator:
    def __init__(self):
        self.answer = None
        self.operation = None
        self.last_ans = None
        self.entries = [None, None]
    
    @property
    def operation(self):
        return self.operation
    
    @operation.setter
    def operation(self, op):
        self.operation = op
        return self
    
    @property
    def last_ans(self):
        return self.last_ans
    
    @property
    def entry_a(self):
        return self.entries[0]
    
    @entry_a.setter
    def entry_a(self, a):
        self.entries[0] = a
        return self
    
    @property
    def entry_b(self):
        return self.entries[1]
    
    @entry_b.setter
    def entry_b(self, b):
        self.entries[1] = b
        return self
    
    def calc_reset(self):
        self.__init__()
    
    def compute(self):
        return self.operation(self.entries[0],self.entries[1])
    