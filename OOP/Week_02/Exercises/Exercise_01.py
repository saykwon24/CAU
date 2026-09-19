# Liters in a 12-ounce can and a two-liter bottle
CAN = 0.355
BOTTLE = 2

# Numbers of cans per pack
cansPerPack = 6

# Calculate six-pack of cans
totalVolume = CAN * cansPerPack    # initialize with volume of cans
print("A six-pack of 12-ounce cans contains" , totalVolume, "liters.")

# Calculate total volume
totalVolume += BOTTLE
print("A six-pack and a two-liter bolttle contain", totalVolume, "liters.")
