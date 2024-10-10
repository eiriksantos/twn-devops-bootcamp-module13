# Defining a function with parameter
def days_to_units(num_of_days, conversion_unit):
    if conversion_unit =="hours":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
    else:
        return "unsupported unit"

def validate_and_execute():
    try:
        # Typecasting and saving it to a variable
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            # Calling the defined function and saving it for printing
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            # Print output
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, try again")
    except ValueError:
        print("Your input is not correct")

user_input = ""
while user_input != "exit":
    # Input function for user input
    user_input = input("Hey user, enter a number of days and conversion unit. \n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()