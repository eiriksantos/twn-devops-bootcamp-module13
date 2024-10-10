# Calculation of days to seconds
# Creating a variable with different data types
from conditionals import user_input

calculation_to_hours = 24
name_of_unit = "hours"

# Defining a function with parameter
def days_to_units(num_of_days):
    # Return value using formatted string
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    try:
        # Typecasting and saving it to a variable
        user_input_number = int(user_input)
        if user_input_number > 0:
            # Calling the defined function and saving it for printing
            calculated_value = days_to_units(user_input_number)
            # Print output
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, try again")
    except ValueError:
        print("Your input is not a number")

user_input = ""
while user_input != "exit":
    # Input function for user input
    user_input = input("Hey user, enter a number of days and I will convert it to hours! \n")
    validate_and_execute()


