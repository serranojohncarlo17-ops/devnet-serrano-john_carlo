"""
Module 2 — Lesson 4: Functions
Student: John Carlo Serrano
Date: September 28, 2026

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Functions are used to group a set of instructions that I want
to use again in my program. Instead of writing the same code
many times, I can put it inside a function and call the function
whenever I need it.


============================================
KEY VOCABULARY
============================================
- function: a block of code that performs a specific task
- parameter: information that I give to a function
- argument: the actual value that I pass to a function
- return value: the result that a function sends back
- def: the keyword used to create a function
- function call: using the function so that its code runs
- return: sends a result back from the function
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

def check_grade(grade):
    if grade >= 75:
        print("Passed")
    else:
        print("Failed")


def show_student(name):
    print("Student:", name)


show_student("John Carlo")
check_grade(91)


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================

a mistake I want to avoid is forgetting to give the
function the information it needs when it has a parameter.


============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Functions can be useful when I have a task that I need to
repeat many times. Instead of writing the same code again,
I can create a function once and call it whenever I need it.
This can make my program shorter and easier to understand.
"""
