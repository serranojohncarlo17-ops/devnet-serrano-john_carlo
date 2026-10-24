"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: [your name]
Date: [date]

============================================
WHAT IS THIS TOPIC? (explain it like you're
teaching a friend who's never coded before)
============================================
Control flow is used when I want my program to make decisions.

For example, I can tell Python to check a student's grade.
If the grade is high enough or above 85, it can display "Passed". If it doesnt meet the requirement, it can display another message or "Failed".



============================================
KEY VOCABULARY
============================================
- condition: something when you want to see if it is True or False.
- if : used when I want the program to do something if a condition
  is True.
- elif: used to check another condition if the previous condition
  was not True.
- else: used when none of the previous conditions are True.
- comparison operator:
- boolean expression:
(add more as needed)


============================================
MY OWN EXAMPLE(S)
============================================
Write at least one working example below that you
came up with yourself — not copied from class.
"""

grade = 92

if grade >= 90:
    print("With Honor!")
elif grade >= 75:
    print("Passed.")
else:
    print("Failed.")


"""
============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
One thing that can be confusing is the difference between =
and ==. A single = is used to give a value to a variable. While
Double == is used to compare values.



============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
[optional]
"""
