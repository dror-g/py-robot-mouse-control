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


req = GATTRequester("D2:34:CA:A7:FA:20", False)   #set to your device address
response = GATTResponse()
req.connect(True, "random")

retry = 0

while True:
#Mouse
  data = display.Display().screen().root.query_pointer()._data

  try:
      olddata
  except:
      olddata = data

  if data["root_x"] == olddata["root_x"]:
      time.sleep(0.3)
      continue

  
  #forward/back
  right = olddata["root_y"] - data["root_y"]
  left = data["root_y"] - olddata["root_y"]

  #turn
  right = ((right + (olddata["root_x"] - data["root_x"])) / 20 ) + 90
  left = ((left + (olddata["root_x"] - data["root_x"])) / 20 ) + 90

  left = toStr(left)
  right = toStr(right)
  full = right + left
  

  req.write_by_handle_async(0x002a, str(bytearray(full)), response)
  while not response.received():
      time.sleep(0.1)
      ++retry
      if retry > 3:
          req.disconnect()
          req.connect(True, "random")
          retry = 0
      try:
        req.is_connected()
      except:
        req.connect(True, "random")
  
  olddata = data
  time.sleep(0.3)

