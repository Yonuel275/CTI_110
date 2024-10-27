# P3LAB_VargasYonuel
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies 
# needed to make a given amount of money entered by the user.

# Input: a float value representing the amount of money
# Output: the most efficient combination of dollars, quarters, dimes, nickels, and pennies

# Get user input
amount = float(input("Enter a money value: "))

# Convert the amount to cents to avoid floating-point precision issues
cents = int(round(amount * 100))

# Calculate the number of dollars
dollars = cents // 100
cents %= 100

# Calculate the number of quarters
quarters = cents // 25
cents %= 25

# Calculate the number of dimes
dimes = cents // 10
cents %= 10

# Calculate the number of nickels
nickels = cents // 5
cents %= 5

# Remaining cents are pennies
pennies = cents

# Output results
if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")

if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")

if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
