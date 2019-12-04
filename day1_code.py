import math
def calcFuel(mass):
    fuelNeeded = math.floor(mass/3) - 2
    if fuelNeeded < 0:
        fuelNeeded = 0
    return fuelNeeded

fuelTotal = 0
fuelNeeded = 0
with open("day1_inputs") as f:
    inputs = f.readlines()
for input in inputs:
    fuelNeeded = calcFuel(int(input))
    fuelTotal += fuelNeeded
    while fuelNeeded > 0:
        fuelNeeded = calcFuel(int(fuelNeeded))
        fuelTotal += fuelNeeded
    fuelTotal += fuelNeeded
print(fuelTotal)
