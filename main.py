"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.0
numChars = input("numChars: ")
woodType = input("woodType: ")
color = input("color: ")
oak = 20.0
minc = 35.0
gold = 15.0
# Write assignment and if statements here as appropriate.

if int(numChars) > 5:
    charge = minc + (int(numChars)-5) *4

elif int(numChars) < 5:
    charge = minc


if woodType == "oak":
        charge += oak

       
       
if color == "gold":
    charge += gold 

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
