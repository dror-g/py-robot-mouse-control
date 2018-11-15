from gattlib import GATTRequester, GATTResponse
import time
import sys
import readchar
#Mouse
from Xlib import display

def toStr(num):
    numoct = []
    numstr = str(num)
    for c in numstr:
        okt = ord(c)
        numoct.append(okt)
    numoct.append(012)
    return numoct


req = GATTRequester("D2:34:CA:A7:FA:20", False)
response = GATTResponse()
req.connect(True, "random")

help(req)
