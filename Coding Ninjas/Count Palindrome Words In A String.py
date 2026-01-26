from os import *
from sys import *
from collections import *
from math import *

def countNumberOfPalindromeWords(s):
    #Your code goes here
    words = s.split()
    cnt = 0
    for word in words:
        word = word.lower()
        if word == word[::-1]:
            cnt += 1
    
    return cnt
