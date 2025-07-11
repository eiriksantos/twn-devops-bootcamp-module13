# import function and variable by referring to the file name
# ex. from FILE_NAME import FUNCTION_NAME, VARIABLE_NAME
from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    # Input function for user input
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute(days_and_unit_dictionary)