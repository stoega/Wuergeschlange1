priceCable = 9.9
priceMonitor = 249.99
priceKeyboard = 27.5
width = 50

print("=" * width)
print("PC Parts Store - Order")
print("=" * width)

numCables = int(input("Number of cables: "))
numMonitors = int(input("Number of monitors: "))
numKeyboards = int(input("Number of keyboards: "))
costCables = numCables * priceCable
costMonitors = numMonitors * priceMonitor
costKeyboards = numKeyboards * priceKeyboard
print(f"{numCables:3d} cables ({priceCable:.2f} EUR each) = {costCables:.2f} EUR")
print(f"{numMonitors:3d} monitors ({priceMonitor:.2f} EUR each) = {costMonitors:.2f} EUR")
print(f"{numKeyboards:3d} keyboards ({priceKeyboard:.2f} EUR each) = {costKeyboards:.2f} EUR")

print("-" * width)
print(f"Total: {costCables + costMonitors + costKeyboards:.2f} EUR")
print("=" * width)