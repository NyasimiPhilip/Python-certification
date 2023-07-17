#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath("/home/enwai/Python-certification/Arithmetic_arranger"))

from arithmetic_arranger import arithmetic_arranger
# Test that the function raises a ValueError when given more than 5 problems
try:
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2", "3 + 4"])
except ValueError as e:
    assert str(e) == "Error: Too many problems", f"Unexpected error message: {str(e)}"
    print("Test passes: ValueError raised with the correct error message")
else:
    assert False, "Expected a ValueError to be raised"
