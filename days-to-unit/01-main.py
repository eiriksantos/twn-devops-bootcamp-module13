# Calculation of days to hours
# Creating a variable with different data types
calculation_to_hours = 24
name_of_unit = "hours"

# Defining a function with parameter
def days_to_units(num_of_days):
    # Return value using a formatted string
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"

# Input function for user input
# Do not forget the validation of user input
user_input = input("Hey user, enter a number of days and I will convert it to hours! \n")

# Typecasting and saving it to a variable
user_input_number = int(user_input)

# Calling the defined function and saving the return value to a variable
calculated_value = days_to_units(user_input_number)

# Print the variable
print(calculated_value)
