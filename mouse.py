from Xlib import display
data = display.Display().screen().root.query_pointer()._data
print("X:", data["root_x"])
print("Y:", data["root_y"])

