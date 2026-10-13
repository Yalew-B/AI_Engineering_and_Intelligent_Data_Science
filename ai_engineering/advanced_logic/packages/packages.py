"""
Packages and Libraries in Python

A library is a collection of reusable code.
A package is a way to organize related modules in directories.
Python ships with a rich standard library, and you can also install third-party packages.
"""

# Standard library imports
import math
import random
import datetime as dt


# Example 1: Using a library module

def circle_area(radius):
    """Return the area of a circle using the math module."""
    return math.pi * radius ** 2


# Example 2: Using random library

def roll_dice(sides=6):
    """Return a random number between 1 and the given number of sides."""
    return random.randint(1, sides)


# Example 3: Using datetime library

def current_time_formatted():
    """Return the current time as a formatted string."""
    now = dt.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# Example 4: Package structure concept
#
# my_project/
#   app.py
#   my_package/
#       __init__.py
#       math_tools.py
#       helpers.py
#
# Then you can import using:
# from my_package.math_tools import circle_area


def main():
    print("Packages and Libraries in Python")
    print(f"Area of circle (radius 5): {circle_area(5)}")
    print(f"Random dice roll: {roll_dice()}")
    print(f"Current time: {current_time_formatted()}")

    # Importing specific functions from a module
    from math import sqrt
    print(f"Square root of 81: {sqrt(81)}")


if __name__ == "__main__":
    main()


# Notes:
# - Python's standard library includes modules like math, random, datetime, os, json, sys.
# - Third-party packages can be installed with pip, for example: pip install requests
# - A package is a folder containing __init__.py and modules.
# - A library is a reusable collection of code, which can be a package or a module.
