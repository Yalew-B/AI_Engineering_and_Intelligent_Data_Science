# Modules in Python
## A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py added. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
#How to create a module:
#1. Create a new Python file with a .py extension.
#2. Define functions, classes, or variables in the file.
#3. Save the file with a descriptive name.

## Example of a simple module (math_operations.py):
from tkinter import constants


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
### How to use a module:
#1. Import the module using the import statement.


#2. Use the functions defined in the module.
result = math_operations.add(5, 3)
print(result)  # Output: 8

### Example of a module with classes (shapes.py):
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
### How to use a module with classes:
#1. Import the module using the import statement.   
#2. Create instances of the classes defined in the module and use their methods.
circle = shapes.Circle(5)
rectangle = shapes.Rectangle(4, 6)
print("Area of circle:", circle.area())  # Output: Area of circle: 78.5
print("Area of rectangle:", rectangle.area())  # Output: Area of rectangle: 24  

#### Example of a module with variables (constants.py):
PI = 3.14159
E = 2.71828

#### How to use a module with variables:
#1. Import the module using the import statement.   
#2. Access the variables defined in the module.
print("Value of PI:", constants.PI)  # Output: Value of PI: 3.14159
print("Value of E:", constants.E)  # Output: Value of E: 2.71828

