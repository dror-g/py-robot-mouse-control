from gattlib import GATTRequester, GATTResponse
import time
import sys
import readchar

req = GATTRequester("D2:34:CA:A7:FA:20", False)
req.connect(True, "random")



#event
#req.write_by_handle(0x001f, str(bytearray([0x2e])))

#uart - octal 3 digit numbers, 012 is nl delimiter
#req.write_by_handle(0x002a, str(bytearray([101,012,102,012,101,012]))) # efe - array

while True:
  #key = ord(raw_input("key"))
  #key = ord(sys.stdin.read(1))
  #key = ord(repr(readchar.readchar()))
  key = ord(readchar.readchar())
  req.write_by_handle(0x002a, str(bytearray([key,012]))) # efe - single string
  time.sleep(0.1)

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
