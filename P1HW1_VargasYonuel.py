# Name
# 9/24/2024
# P1HW1
# Make calculations

# Display output to user
print("----------Calculating Exponents----------")
print()
print()

# Get info from user
base_value = int(input("Enter and integer as the base value: "))
exponent = int(input("Enter and integer as the exponent: "))
print()
print()

# Calculate the value of the exponent math
result = base_value ** exponent

# Display results of the math
print(base_value, "raised to the power of", exponent, "is", result, "!!")
print()
print()

print("--------Addition and Subtraction--------")
print()
print()

# Get info from user
start_base = int(input("Enter a starting integer: "))
int_add = int(input("Enter an integer to add: "))
int_sub = int(input("Enter an integer to subtract: "))
print()
print()

# Calculate2 the math
result2 = start_base + int_add - int_sub

# Display the results
print(start_base, "+", int_add, "-", int_sub, "is equal to", result2)
