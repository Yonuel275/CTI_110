# Yonuel Vargas
# 10/29/2024
# P3HW2
# Program calculates paycheck based on OT or no OT

'''
Input: Get employee name from user - string (name)
Input: Get hours worked from user - int (hours)
Input: Get pay rate from user - float (pay_rate)

Output: print dotted line and employee name

If hours is greater than 40 (employee has OT)
    variable for hours worked already exists (don't have to create)
    (don't have to create pay rate, it already exists)
    create a variable (OT) that holds only the OT hours (hours - 40)
    create a variable for OT_pay_rate (pay_rate * 1.5)
    calculate pay for OT hours (OT * OT_pay_rate)
    calculate regular pay (pay_rate * 40)
    Calculate gross pay (pay for OT + regular pay)
else (NO OT - hours has to be 40 or less)
       create a variable (OT) that holds only the OT hours WHICH IS ZERO
       calculate pay for OT hours WHICH IS ZERO
       calculate regular pay (pay_rate * hours)
       Calculate gross pay (same as regular pay)

Display the line of strings with width specifiers
print(f"{'Hours Worked':<20}{'Pay Rate':<20}")
print(f"{hours:<20}${pay_rate:<20.2f}")
       

    

'''
# Get inputs from user
employee_name = input("Enter employee's name: ")
hours = int(input("Enter hours worked: "))
pay_rate = float(input("Enter pay rate: "))

# Print header and employee name
print("\n------------------------------------")
print(f"Employee Name: {employee_name}")

# Calculate paycheck based on overtime or no overtime
if hours > 40:
    # Calculate overtime details
    OT_hours = hours - 40
    OT_pay_rate = pay_rate * 1.5
    OT_pay = OT_hours * OT_pay_rate
    regular_pay = pay_rate * 40
    gross_pay = regular_pay + OT_pay
else:
    # No overtime
    OT_hours = 0
    OT_pay = 0
    regular_pay = pay_rate * hours
    gross_pay = regular_pay


# Display paycheck details
print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'Overtime Hours':<20}{'OT Pay':<20}{'Regular Pay':<20}{'Gross Pay':<20}")
print("---------------------------------------------------------------------------------------------------------------------------------------------")
print(f"{hours:<20}{pay_rate:<20.2f}{OT_hours:<20}{OT_pay:<20.2f}{regular_pay:<20.2f}{gross_pay:<20.2f}")
