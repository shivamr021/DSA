from os import *
from sys import *
from collections import *
from math import *
import re
def checkPalindrome(s):
  # Write your code here
  clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
  # Return a boolean
	return clean_s == clean_s[::-1]
