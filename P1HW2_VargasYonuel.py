# Yonuel
# Date
# P1HW2
# Travel info

# Display output to user
print("This program calculates and displays travel expenses")
print()

# Get info from user
budget_value = int(input("Enter budget: "))
print()
travel_place = (input("Enter your travel destination: "))
print()
gass_cost = int(input("How much do you think you will spend on gas? "))
print()
hotel_cost = int(input("Approximately, how much will you need for accodation/hotel? "))
print()
food_cost = int(input("Last, how much do you need for food? "))
print()
print()

print("----------Travel Expenses----------")
print()
print()

print(f"Location: {travel_place}")
print(f"Initial Budget: {budget_value}")
print()
print(f"Fuel: {gass_cost}")
print(f"Accomodation: {hotel_cost}")
print(f"Food: {food_cost}")

# Calculate total expenses
result = budget_value - gass_cost - hotel_cost - food_cost

print(f"Remaining Balance: {result}")

