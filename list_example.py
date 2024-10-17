'''
# Add values to the list
myfam.append("Mallory")
myfam.append("Mandy")
myfam.append("Natalie")
myfam.append("Brant")
myfam.append("Yoshi")

# Display list
print(myfam)

# print item at index 3
print(myfam[3])
'''
num1 = int(input("gimme a number: "))
num2 = int(input("gimme a number: "))
num3 = int(input("gimme a number: "))
num4 = int(input("gimme a number: "))

# Create the list with the values in it
numbers = [num1, num2, num3, num4]

print(numbers)

# gives back the number of items in the list
print(len(numbers))

# Get the highest value in the list
print(f"The lowest value in the list is {min(numbers)}")
