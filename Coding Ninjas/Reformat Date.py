from os import *
from sys import *
from collections import *
from math import *

def reformDate(s):
    # Write your code here.
    month_map = {
        "Jan": "01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05",
        "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10",
        "Nov":"11", "Dec":"12"
    }

    day, mon, year = s.split()

    day = ''.join([ch for ch in day if ch.isdigit()])
    day = day.zfill(2)

    mon = month_map[mon]

    return "-".join([year, mon, day])
