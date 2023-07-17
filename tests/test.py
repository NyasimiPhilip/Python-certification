#!/usr/bin/python3
import sys
import os

sys.path.append(os.path.abspath("/home/enwai/Python-certification/Arithmetic_arranger"))

from arithmetic_arranger import arithmetic_arranger
# Test that the function raises a ValueError when given more than 5 problems
try:
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "1 + 2", "3 + 4"])
