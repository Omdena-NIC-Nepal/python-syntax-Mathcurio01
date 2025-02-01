[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=17904476&assignment_repo_type=AssignmentRepo)
﻿# python_syntax_assignment


# Python Fundamentals Assignment (100 Points)

## Overview
This assignment tests your understanding of fundamental Python concepts across three main areas:
- Python Syntax (30 points)
- Data Structures (40 points)
- Operators (30 points)

## Instructions
1. Clone this repository to your local machine
2. Complete all functions in `assignment.py`
3. Test your solutions locally using `test_assignment.py`
4. Commit and push your changes to submit

## Requirements

### Part 1: Python Syntax (30 points)
1. Function `format_string(name, age)` (10 points)
   - Create a formatted string using f-strings
   - Return "My name is {name} and I am {age} years old"

2. Function `conditional_check(number)` (10 points)
   - If number > 10: return "Greater"
   - If number < 10: return "Lesser"
   - If number == 10: return "Equal"

3. Function `loop_sum(n)` (10 points)
   - Use a loop to sum numbers from 1 to n
   - Return the sum

### Part 2: Data Structures (40 points)
1. Function `list_operations(numbers)` (15 points)
   - Take a list of numbers
   - Return a tuple containing:
     - Sum of all numbers
     - Maximum number
     - Minimum number

2. Function `dict_operations(students_dict)` (15 points)
   - Take a dictionary of student names and scores
   - Return a list of names of students who scored above 80

3. Function `set_operations(list1, list2)` (10 points)
   - Take two lists
   - Return a set of common elements

### Part 3: Operators (30 points)
1. Function `arithmetic_ops(a, b)` (10 points)
   - Return a dictionary with:
     - 'sum': a + b
     - 'difference': a - b
     - 'product': a * b
     - 'quotient': a / b (handle division by zero)

2. Function `logical_ops(x, y)` (10 points)
   - Return a dictionary with results of:
     - 'and': x and y
     - 'or': x or y
     - 'not_x': not x

3. Function `bitwise_ops(a, b)` (10 points)
   - Return a dictionary with:
     - 'and': a & b
     - 'or': a | b
     - 'xor': a ^ b

## Grading
- Each function will be tested with multiple test cases
- Partial credit will be given for partially correct solutions
- Code style and proper error handling will be considered