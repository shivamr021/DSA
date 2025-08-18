from typing import *

class InfiniteArray:
    def __init__(self):
        self.defaltValue = False
        self.globalVersion = 0
        self.indexValue = {}

    def setAllTrue(self) -> None:
        # Implement the function here
        self.defaltValue = True
        self.globalVersion += 1

    def setAllFalse(self) -> None:
        # Implement the function here
        self.defaltValue = False
        self.globalVersion += 1

    def setIndexTrue(self, index: int) -> None:
        # Implement the function here
        self.indexValue[index] = (True, self.globalVersion)

    def setIndexFalse(self, index: int) -> None:
        # Implement the function here
        self.indexValue[index] = (False, self.globalVersion)

    def getIndex(self, index: int) -> bool:
        # Implement the function here
        if index in self.indexValue:
            val, ver = self.indexValue[index]
            if ver == self.globalVersion:
                return val
        return self.defaltValue

