# Yonuel
# Date
# P2HW1
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
print(f"{'Location:':<20}{travel_place}")
print(f"{'Initial Budget:':<20}${budget_value:,.2f}")
print(f"{'Fuel:':<20}${gass_cost:,.2f}")
print(f"{'Accomodation:':<20}${hotel_cost:,.2f}")
print(f"{'Food:':<20}${food_cost:,.2f}")
print("-----------------------------------")
# Calculate total expenses
result = budget_value - gass_cost - hotel_cost - food_cost
print(f"{'Remaining Balance:':<20}${result:,.2f}")
