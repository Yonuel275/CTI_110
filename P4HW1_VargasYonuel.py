# Your Name
# Date
# P4HW1
# Program collects scores, validates them, calculates the average after dropping the lowest score, and determines the letter grade.

# Pseudocode (see above)

# Step 1: Ask user for the number of scores to enter
num_scores = int(input("How many scores do you want to enter? "))

# Step 2: Initialize the list to store scores
scores = []

# Step 3: Loop to collect scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score!!! Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

print("-----------------Results-------------------")

# Step 4: Display the lowest score
lowest_score = min(scores)
print("\nLowest scores:", lowest_score)

# Step 5: Remove the lowest score and display updated list
scores.remove(lowest_score)
print("Modified list:", scores)

# Step 6: Calculate average and display it
average = sum(scores) / len(scores)
print("Scores average:", round(average, 2))

# Step 7: Determine and display letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)
