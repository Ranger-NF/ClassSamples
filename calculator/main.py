# THINGS INTRODUCED:
# Print statement
# Input statement
# split statement
# if statements (checking input)
# for loop (iteration)
# functions
# Operators (+ , /, *, -)


print("Welcome to the sample project: Calulator!")


def get_input() -> list:
    user_input: str = input(
        "Enter the integers to be added seperated with comma: ")
    given_nums: list = user_input.split(",")

    return given_nums


def check_input(input_list: list[str]):
    for value in input_list:
        if not value.isdigit():
            return False

    return True


initial_input: list[str] = get_input()

if check_input(initial_input):
    print("\n\nThe answer is: ")

    added_nums = int(initial_input[0]) + int(initial_input[1])

    print(added_nums)
else:
    print("The given values were not integers! Try again...")
