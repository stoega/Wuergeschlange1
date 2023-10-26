length = float(input("Length (meters): "))
width = float(input("Width (meters): "))
height = float(input("Height (meters): "))

print(f"Circumference: {(length + width) * 2:.2f} meters")
print(f"Volume: {length * width * height:.2f} cubic meters")
wallArea = 2* height*length + 2*height*width
print(f"Wall area: {wallArea:.2f} square meters")
numWindows = int(wallArea / 12)
print(f"Number of windows: {numWindows}")
print(f"Needed paint: {(wallArea - 2*numWindows) * .75:.2f} liters")