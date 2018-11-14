from gattlib import GATTRequester, GATTResponse
import time
import sys
import readchar
#Mouse
from Xlib import display

req = GATTRequester("D2:34:CA:A7:FA:20", False)
response = GATTResponse()
req.connect(True, "random")


#event
#req.write_by_handle(0x001f, str(bytearray([0x2e])))

#uart - octal 3 digit numbers, 012 is nl delimiter
#req.write_by_handle(0x002a, str(bytearray([101,012,102,012,101,012]))) # efe - array

while True:
#Mouse
  data = display.Display().screen().root.query_pointer()._data

  try:
      olddata
  except:
      olddata = data

  #print("X:", data["root_x"])
  #print("Y:", data["root_y"])
  #print("X:", data["root_x"])
  #print("Y:", data["root_y"])
  
  #forward/back
  right = data["root_y"] - olddata["root_y"]
  left = olddata["root_y"] - data["root_y"]

  #turn
  right = right + (data["root_x"] - olddata["root_x"])
  left = left + (data["root_x"] - olddata["root_x"])

  print("left: ", left)
  print("right: ", right)

  time.sleep(0.5)

  #req.write_by_handle_async(0x002a, str(bytearray([key,012])), response)
  #while not response.received():
  #    time.sleep(0.01)


  #key = ord(readchar.readchar())
  #key = ord("q")

  #req.write_by_handle_async(0x002a, str(bytearray([key,012])), response)
  #while not response.received():
  #    time.sleep(0.01)


  #try:
  #  req.write_by_handle_async(0x002a, str(bytearray([key,012])), callback()) # efe - single string
  #except:
  #    print("fail")
  #time.sleep(0.1)

# Response
#response = GATTResponse()
#print(response)
#
#req.read_by_uuid_async('e95d8d00-251d-470a-a062-fa1922dfa9a8', response)
#while not response.received():
#    time.sleep(0.1)
#
#steps = response.received()[0]
#print(steps)
