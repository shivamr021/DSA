from sys import *
from collections import *
from math import *

from typing import *

def stringMania(n : int, m : int, str1 : str, str2 : str) -> int:
    # Write your code here.
    min_len = min(n,m)

    for i in range(min_len):
        if str1[i] != str2[i]:
            if str1[i] > str2[i]:
                return 1
            else:
                return -1

    if n > m:
        return 1
    elif n < m:
        return -1
    else:
        return 0
