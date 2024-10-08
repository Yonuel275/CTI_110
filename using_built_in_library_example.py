# Using Python built-in libraries

# Import the datetime library to use it in the program
import datetime

# assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month

month_word = (time.strftime("%B"))

# Display date/time
print(f"The current date and time is {time}")
print(f"The current month is {month}")
print(f"The current month is {month_word}")
