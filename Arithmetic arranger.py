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
        return 'Error: Too many problems.'

    first_line = "" # To hold the first line of each of the expressions (i.e the line containing the first operand)
    second_line = ""# To hold the second line of each of the expressions (i.e the line containing the operator and second operand)
    dashes = ""# Bunch of horizontal dashes to separate the operands from their result)
    results = ""
    max_result_length = 0
    for problems in list_of_problems:
       
        if "+" not in problems and  "-" not in problems:  # Second Error Handling: Only '+' and '-' operators are allowed
            return 'Error: Operator must be '+' or '-'.'

        first_number = problems.split()[0]
        operator = problems.split()[1]
        second_number = problems.split()[2]

        if not first_number.isdigit() or not second_number.isdigit():  # Third Error Handling: Numbers must only contain digits
            return 'Error: Numbers must only contain digits.'

        if len(first_number or second_number) > 4:  # Fourth Error Handling: Numbers must only contain 4 digits
            return 'Error: Numbers cannot be more than four digits.'

        result = ops[operator](int(first_number), int(second_number))
        aligning_space = max([len(first_number), len(second_number)]) + 2
        if problems != list_of_problems[-1]:
          first_line = first_line + first_number.rjust( aligning_space) + (4 * " ")
          second_line = second_line + operator + second_number.rjust(aligning_space - 1) + (4 * " ")
          dashes = dashes + aligning_space * '-' + (4 * " ")
          results = results + str(result).rjust(aligning_space) + (4 * " ")
        else:
          first_line = first_line + first_number.rjust( aligning_space)
          second_line = second_line + operator + second_number.rjust(aligning_space - 1) 
          dashes = dashes + aligning_space * '-' 
          results = results + str(result).rjust(aligning_space)   

        

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

def test_arithmetic_arranger():
    # Test with a single problem
    input1 = ['32 + 698']
    expected_output1 = '   32\n+ 698\n_____'
    assert arithmetic_arranger(input1) == expected_output1

    # Test with multiple problems
    input2 = ['32 + 698', '3801 - 2', '45 + 43']
    expected_output2 = ' 32       3801      45      \n+698      -2        +43      \n_____    ______    ____    '
    assert arithmetic_arranger(input2) == expected_output2

    # Test with multiple problems and the solver flag set to True
    expected_output3 = ' 32       3801      45      \n+698      -2        +43      \n_____    ______    ____    \n730      3799      88      '
    assert arithmetic_arranger(input2, solver=True) == expected_output3

test_arithmetic_arranger()
