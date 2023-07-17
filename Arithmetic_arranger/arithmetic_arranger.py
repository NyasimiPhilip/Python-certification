# Create a function that receives a list of strings that are arithmetic
# problems and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument and
# when the second argument is set to `True`, the answers should be displayed'''

import operator
import re

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
    aligning_space = 0
    for problems in list_of_problems:
       
        if re.search("[/]", problems) or re.search("[*]", problems):
          return "Error: Operator must be '+' or '-'."

        first_number = problems.split()[0]
        operator = problems.split()[1]
        second_number = problems.split()[2]

        if not first_number.isdigit() or not second_number.isdigit():  # Third Error Handling: Numbers must only contain digits
            return 'Error: Numbers must only contain digits.'

        if len(first_number) > 4 or len(second_number) > 4:  # Fourth Error Handling: Numbers must only contain 4 digits
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
