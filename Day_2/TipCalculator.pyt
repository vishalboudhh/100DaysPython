print("Welcome to the tip calculator! ")
bill = float(input("What is the total bill? "))
percentage = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

tip = bill * (percentage / 100)
total_bill = bill + tip
per_person = total_bill / people

print(f'Each person should pay: ${per_person:.2f}')