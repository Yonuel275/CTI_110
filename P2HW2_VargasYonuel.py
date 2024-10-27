'''
BEGIN
    // Declare a list to store grades
    DECLARE LIST grades

    // Input grades for each module
    PRINT "Enter the grade for Module 1: "
    READ grade1
    ADD grade1 to grades list

    PRINT "Enter the grade for Module 2: "
    READ grade2
    ADD grade2 to grades list

    PRINT "Enter the grade for Module 3: "
    READ grade3
    ADD grade3 to grades list

    PRINT "Enter the grade for Module 4: "
    READ grade4
    ADD grade4 to grades list

    PRINT "Enter the grade for Module 5: "
    READ grade5
    ADD grade5 to grades list

    PRINT "Enter the grade for Module 6: "
    READ grade6
    ADD grade6 to grades list

    // Calculate required values
    SET lowest_grade = MIN(grades)
    SET highest_grade = MAX(grades)
    SET sum_of_grades = SUM(grades)
    SET average_grade = sum_of_grades / LENGTH(grades)

    // Output results
    PRINT "Lowest Grade: ", lowest_grade
    PRINT "Highest Grade: ", highest_grade
    PRINT "Sum of Grades: ", sum_of_grades
    PRINT "Average Grade: ", average_grade formatted to 2 decimal places
END
'''
# Pseudocode
# 1. Declare a list to store grades.
# 2. Prompt the user to enter grades for each of the six modules.
# 3. Add each entered grade to the list.
# 4. Calculate the lowest grade, highest grade, sum of grades, and average of grades.
# 5. Display the results in the specified format.

# Declare a list to store grades
grades = []

# Input grades for each module
grades.append(float(input("Enter the grade for Module 1: ")))
grades.append(float(input("Enter the grade for Module 2: ")))
grades.append(float(input("Enter the grade for Module 3: ")))
grades.append(float(input("Enter the grade for Module 4: ")))
grades.append(float(input("Enter the grade for Module 5: ")))
grades.append(float(input("Enter the grade for Module 6: ")))

# Calculate required values
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)
print("----------Results----------")
# Output results
print(f"Lowest Grade:   {lowest_grade:.2f}")
print(f"Highest Grade:  {highest_grade:.2f}")
print(f"Sum of Grades:  {sum_of_grades:.2f}")
print(f"Average Grade:  {average_grade:.2f}")
print("---------------------------")
