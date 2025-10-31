from os import *
from sys import *
from collections import *
from math import *

prefix_suffix_map = {}

def wordFilter(words):
    # Write your code here.
    global prefix_suffix_map
    prefix_suffix_map = {}

    for idx, word in enumerate(words):
        n = len(word)
        for i in range(1, n+1):
            prefix = word[:i]
            for j in range(n):
                suffix = word[j:]
                prefix_suffix_map[prefix + '#' + suffix] = idx

def find(prefix, suffix):
    # Write your code here.
    global prefix_suffix_map
    key = prefix + '#' + suffix
    return prefix_suffix_map.get(key, -1)
