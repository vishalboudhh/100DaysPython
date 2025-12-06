print("Welcome to python delivery!")
size = input("What size pizza do you want ? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza ? Y or N:").lower()
extra_cheese = input("Do you want extra cheese ? Y or N:").lower()

bill = 0

# Size
if size == "s" or size == "S":
    bill += 15
elif size == "m" or size == "M":
    bill += 20
elif size == "l" or size == "L":
    bill += 30
else:
    print("Invalid size selected!")

# Pepperoni
if pepperoni == "y" or pepperoni == "Y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# Extra Cheese
if extra_cheese == "y" or extra_cheese == "Y":
    bill += 1

print(f"Your final bill is : ${bill}")
