from gattlib import GATTRequester, GATTResponse
import time

req = GATTRequester("D2:34:CA:A7:FA:20", False)
req.connect(True, "random")
response = GATTResponse()
print(response)

# IO Pins
#req.write_by_handle(0x002d, str(bytearray([0x01, 0x00])))
#req.write_by_handle(0x002d, str(bytearray([0x11, 0xff])))
#req.write_by_handle(0x002c, str(bytearray([0x00, 0x00])))


#event
#req.write_by_handle(0x001f, str(bytearray([0x2e])))

#uart - octal 3 digit numbers, 012 is nl delimiter
req.write_by_handle(0x002a, str(bytearray([101,012,102,012,101,012]))) # efe - array
#req.write_by_handle(0x002a, str(bytearray([101,102,101,012]))) # efe - single string

# Response
#req.read_by_uuid_async('e95d8d00-251d-470a-a062-fa1922dfa9a8', response)
#while not response.received():
#    time.sleep(0.1)
#
#steps = response.received()[0]
#print(steps)
