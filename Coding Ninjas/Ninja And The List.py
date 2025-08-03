from os import *
from sys import *
from collections import *
from math import *
from typing import *

class NestedInteger():
    def __init__(self):
        self.data = -1
        self.a = []
        
    def isInteger(self):
        return len(self.a) == 0
    
    def getInteger(self):
        return self.data
    
    def getList(self):
        return self.a

class NestedIterator():
    def __init__(self, nestedList: NestedInteger):
        # Write your code here.
        self.stack = nestedList[::-1]
    
    def nex(self) -> int:
        # Write your code here.
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        # Write your code here.
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            nested = top.getList()
            self.stack.extend(nested[::-1])
        return False
