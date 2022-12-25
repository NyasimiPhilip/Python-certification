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
    first_line = ""
    second_line = ""
    dashes = ""

    if len(list_of_problems) > 5:  # Function must only accept a maximum of five problems

        return 'Error: Too many problems'
    for problems in list_of_problems:

        problems = problems.replace(' ', '')
        if not "+" or "-" not in problems:  # Second Error Handling: Only '+' and '-' operators are allowed
            return 'Error: Operator must be \'+\' or \'-\'.'

        else:
            first_number = problems.split()[0]
            operator = problems.split()[1]
            second_number = problems.split()[2]

        if not first_number.isdigit() and not second_number.isdigit():

            return 'Error: Numbers must only contain digits.'  # Third Error Handling: Numbers must only contain digits
        else:
            pass
        if abs(first_number) and abs(second_number) > 1e4:  # Fourth Error Handling: Numbers must only contain 4 digits
            raise ValueError('Numbers must only contain 4 digits')
        else:
            pass
        aligning_space = max([len(first_number), len(second_number)]) + 2
        # Getting number of digits contained in the largest  operand and adding 2 to it
        # This sets the number of characters that a line can have in each arranged expression

        total = ops[operator](int(first_number), int(second_number))

        second_number = operator + second_number.rjust(aligning_space - 1)
        first_line = first_line + first_number.rjust(aligning_space) + (4 * " ")
        second_line = second_line + second_number + (4 * " ")
        dashes = dashes + aligning_space * '_' + (4 * " ")
        total = str(total).rjust(aligning_space) + (4 * " ")
    if solver:
        print(first_line)
        print(second_line)
        print(dashes)
        print(total)
        print(dashes)


if __name__ == "__main__":
    arithmetic_arranger([
        "34 + 645",
        "381 - 342",
        "43 + 4453",
        "13 + 4129",
        "1024 - 936"
    ], solver=True)

