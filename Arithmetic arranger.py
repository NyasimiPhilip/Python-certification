# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Create a function that receives a list of strings that are arithmetic
# problems and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument and
# when the second argument is set to `True`, the answers should be displayed'''

import operator

ops = {"+": operator.add, "-": operator.sub}

def arithmetic_arranger(list_of_problems, solver=False):
    """
    :param solver:
    :type list_of_problems: list
    """
    if len(list_of_problems) > 5:  # Function must only accept a maximum of five problems
        raise ValueError ('Error: Too many problems')

    first_line = "" # To hold the first line of each of the expressions (i.e the line containing the first operand)
    second_line = ""# To hold the second line of each of the expressions (i.e the line containing the operator and second operand)
    dashes = ""# Bunch of horizontal dashes to separate the operands from their result)
    results = ""
    aligning_space = 0
    for problems in list_of_problems:
       
        if "+" not in problems and "-" not in problems:  # Second Error Handling: Only '+' and '-' operators are allowed
            raise ValueError('Error: Operator must be \'+\' or \'-\'.')

        first_number = problems.split()[0]
        operator = problems.split()[1]
        second_number = problems.split()[2]

        if not first_number.isdigit() or not second_number.isdigit():  # Third Error Handling: Numbers must only contain digits
            raise ValueError('Error: Numbers must only contain digits.')

        if len(first_number or second_number) > 4:  # Fourth Error Handling: Numbers must only contain 4 digits
            raise ValueError('Numbers must only contain 4 digits')

        result = ops[operator](int(first_number), int(second_number))
        aligning_space = max([len(first_number), len(second_number)]) + 2

        first_line = first_line + first_number.rjust( aligning_space) + (4 * " ")
        second_line = second_line + operator + second_number.rjust(aligning_space - 1) + (4 * " ")
        dashes = dashes + aligning_space * '_' + (4 * " ")
        results = results + str(result).rjust(aligning_space) + (4 * " ")

    arranged_problems = f"{first_line}\n{second_line}\n{dashes}"
    if solver:
        arranged_problems += f"\n{results}"

    return arranged_problems
    
# Test that the function raises a ValueError when given more than 5 problems
try:
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2", "3 + 4"])
except ValueError as e:
    assert str(e) == "Error: Too many problems", f"Unexpected error message: {str(e)}"
else:
    assert False, "Expected a ValueError to be raised"

# Test that the function raises a ValueError when given an invalid operator
try:
    arithmetic_arranger(["32 * 698"])
except ValueError as e:
    assert str(e) == "Error: Operator must be '+' or '-'.", f"Unexpected error message: {str(e)}"
else:
    assert False, "Expected a ValueError to be raised"

# Test that the function raises a ValueError when given a non-numeric operand
try:
    arithmetic_arranger(["abc + 698"])
except ValueError as e:
    assert str(e) == "Error: Numbers must only contain digits.", f"Unexpected error message: {str(e)}"
else:
    assert False, "Expected a ValueError to be raised"

# Test that the function raises a ValueError when given a number with more than 4 digits
try:
    arithmetic_arranger(["12345 + 698"])
except ValueError as e:
    assert str(e) == "Numbers must only contain 4 digits", f"Unexpected error message: {str(e)}"
else:
    assert False, "Expected a ValueError to be raised"

# Test that the function returns the expected output for a valid input
assert arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) == " 32      + 698    \n3801    - 2       \n________________\n 45      + 43      \n123      + 49      \n________________", "Unexpected output"

# Test that the function returns the expected output for a valid input with the solver option set to True
assert arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], solver=True) == " 32      + 698    \n3801    - 2       \n________________\n 45      + 43      \n123      + 49      \n________________\n730      3799      \n168      172       ", "Unexpected output"
