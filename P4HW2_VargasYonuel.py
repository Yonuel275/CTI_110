# Yonuel Vargas
# 11/17/2024
# P4HW2
# This program calculates regular pay, overtime pay, and gross pay for multiple employees. 
# It also calculates total overtime pay, total regular pay, and total gross pay for all employees.

# Initialize totals
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    # Ask for employee name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    # Sentinel to exit loop
    if employee_name.lower() == "done":
        break

    # Input pay rate and hours worked
    try:
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

        # Calculate regular and overtime pay
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * pay_rate * 1.5
            regular_pay = 40 * pay_rate
        else:
            overtime_pay = 0
            regular_pay = hours_worked * pay_rate

        # Calculate gross pay
        gross_pay = regular_pay + overtime_pay

        # Update totals
        total_regular_pay += regular_pay
        total_overtime_pay += overtime_pay
        total_gross_pay += gross_pay
        employee_count += 1
        
        # Display individual employee's pay in a tabular format
        print("\nEmployee name:   ", employee_name)
        print()
        print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
        print("--------------------------------------------------------------------------------")
        print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}\n")

    except ValueError:
        print("Invalid input. Please enter numeric values for pay rate and hours worked.\n")

# Display total summary after loop ends
print("\nTotal Summary:")
print(f"{'Number of Employees:':<5}{employee_count:>5}")
print(f"{'Total Overtime Pay:':<5}${total_overtime_pay:>5.2f}")
print(f"{'Total Regular Pay:':<5}${total_regular_pay:>5.2f}")
print(f"{'Total Gross Pay:':<5}${total_gross_pay:>5.2f}")
