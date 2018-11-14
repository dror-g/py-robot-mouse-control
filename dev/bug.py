import bluetooth
x = bluetooth.discover_devices()
n = bluetooth.lookup_name(x[0])
print(n)

