#Functions in Python
#Functions are reusable blocks of code that perform a specific task. They allow us to organize our code into logical units and avoid repetition. In Python, we define a function using the def keyword followed by the function name and parentheses. 
#Functions can take parameters, which are values passed into the function to customize its behavior. Parameters are defined within the parentheses of the function definition. Inside the function, we can use these parameters to perform operations or calculations. Functions can also return values using the return statement, allowing us to capture the result of the function's execution.
#Parameters are optional and can be used to pass values into the function. Functions can be called by their name followed by parentheses, and any required arguments can be passed inside the parentheses.  
#Functions can also be defined with default parameter values, allowing them to be called with or without arguments. Additionally, functions can be nested, meaning that one function can be defined inside another function. This allows for more complex and modular code structures.
#Arguments can be passed to functions in different ways, including positional arguments, keyword arguments, and variable-length arguments. Positional arguments are passed based on their position in the function call, while keyword arguments are passed using the parameter name. Variable-length arguments allow us to pass a variable number of arguments to a function.
#The syntax of a function is as follows:
# Syntax:
# def function_name():
    # block of code to be executed
#Example:
#Greeting function
#Greeting function performs a simple greeting message when called. It does not take any parameters and simply prints a welcome message to the console. This function can be reused whenever a greeting is needed in the program.
def greet():
    print("Hello, welcome to Python functions!")
greet()

#Function Loop without parameters
#Function Loop performs a simple loop that prints numbers from 0 to 4. It does not take any parameters and simply iterates through a range of numbers, printing each number to the console. This function can be reused whenever a loop is needed in the program.   
def print_values():
    for i in range(5):
        print(i)
print_values()

#Function to add two numbers with parameters
#Add two numbers function takes two parameters, a and b, and returns their sum. This function can be called with different values of a and b to perform addition on various pairs of numbers. The result of the addition is then printed to the console.    
a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
def add_numbers(a, b):
    return a + b

result = add_numbers(a, b)
print(result)

#Function to multiply two numbers with parameters
#Multiply two numbers function takes two parameters, a and b, and returns their product. This function can be called with different values of a and b to perform multiplication on various pairs of numbers. The result of the multiplication is then printed to the console.
def multiply_numbers(a, b):
    return a * b        

result = multiply_numbers(a, b)
print(result)

#Function to divide two numbers with parameters
#Divide two numbers function takes two parameters, a and b, and returns their quotient. This function can be called with different values of a and b to perform division on various pairs of numbers. The result of the division is then printed to the console.
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
    
result = divide_numbers(a, b)
print(result)

#Function to subtract two numbers with parameters
#Subtract two numbers function takes two parameters, a and b, and returns their difference. This function can be called with different values of a and b to perform subtraction on various pairs of numbers. The result of the subtraction is then printed to the console.
def subtract_numbers(a, b):
    return a - b

result = subtract_numbers(a, b)
print(result)

#Function to calculate the square of a number with parameters
#Mathematical formula: a^2 = a * a
#Square a number function takes one parameter, a, and returns its square. This function can be called with different values of a to calculate the square of various numbers. The result of the calculation is then printed to the console.
def square_number(a):
    return a ** 2   

result = square_number(a)
print(result)

#Function to calculate the cube of a number with parameters
#Mathematical formula: a^3 = a * a * a
#Cube a number function takes one parameter, a, and returns its cube. This function can be called with different values of a to calculate the cube of various numbers. The result of the calculation is then printed to the console.
def cube_number(a):
    return a ** 3

result = cube_number(a)
print(result)

#Function to calculate the factorial of a number with parameters
#Mathematical formula: n! = n * (n-1) * (n-2) * ... * 1
#Factorial a number function takes one parameter, n, and returns its factorial. This function can be called with different values of n to calculate the factorial of various numbers. The result of the calculation is then printed to the console.
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

result = factorial(a)
print(result)

#Function to calculate the power of a number with parameters
#Mathematical formula: a^b = a * a * ... * a (b times)
#Power a number function takes two parameters, base and exponent, and returns the result of raising the base to the power of the exponent. This function can be called with different values of base and exponent to perform power calculations on various pairs of numbers. The result of the calculation is then printed to the console.
def power(base, exponent):
    return base ** exponent

result = power(a, b)
print(result)

#Function to calculate the average of two numbers with parameters
#Mathematical formula: (a + b) / 2
#Average of two numbers function takes two parameters, a and b, and returns their average. This function can be called with different values of a and b to calculate the average of various pairs of numbers. The result of the calculation is then printed to the console.
def average(a, b):
    return (a + b) / 2  

result = average(a, b)
print(result)

#Function to calculate the maximum of two numbers with parameters
#Mathematical formula: max(a, b)
#Maximum of two numbers function takes two parameters, a and b, and returns the larger of the two. This function can be called with different values of a and b to find the maximum of various pairs of numbers. The result of the calculation is then printed to the console.
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

result = maximum(a, b)
print(result)

#Function to calculate the minimum of two numbers with parameters
#Mathematical formula: min(a, b)
#Minimum of two numbers function takes two parameters, a and b, and returns the smaller of the two. This function can be called with different values of a and b to find the minimum of various pairs of numbers. The result of the calculation is then printed to the console.
def minimum(a, b):
    if a < b:
        return a
    else:
        return b

result = minimum(a, b)
print(result)

#Function to check if a number is even or odd with parameters
#Even number is a number that is divisible by 2, while an odd number is a number that is not divisible by 2. The even or odd function takes one parameter, n, and returns "Even" if the number is even, otherwise "Odd". This function can be called with different values of n to check if they are even or odd. The result of the check is then printed to the console.
#Even or odd function takes one parameter, n, and returns "Even" if the number is even, otherwise "Odd".
def is_even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

result = is_even_or_odd(a)
print(result)

#Function to check if a number is prime with parameters
#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The prime function takes one parameter, n, and returns "Prime" if the number is prime, otherwise "Not prime". This function can be called with different values of n to check if they are prime. The result of the check is then printed to the console.
#A composite number is a natural number greater than 1 that is not prime, meaning it has positive divisors other than 1 and itself. The prime function checks for primality by testing divisibility from 2 up to the square root of n. If any divisor is found, the number is classified as "Not prime"; otherwise, it is classified as "Prime".
def is_prime(n):
    if n <= 1:
        return "Not prime"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

result = is_prime(a)
print(result)

#Function to calculate the sum of a list of numbers with parameters
#Sum of list function takes one parameter, numbers, and returns the sum of all elements in the list. This function can be called with different lists of numbers to calculate their sums. The result of the calculation is then printed to the console.
def sum_of_list(numbers):
    return sum(numbers) 

result = sum_of_list([1, 2, 3, 4, 5])
print(result)

#Function to calculate the length of a list with parameters
#Length of list function takes one parameter, numbers, and returns the length of the list. This function can be called with different lists of numbers to calculate their lengths. The result of the calculation is then printed to the console.
def length_of_list(numbers):
    return len(numbers)

result = length_of_list([1, 2, 3, 4, 5])
print(result)

#Function to reverse a string with parameters
#Reverse string are a common operation in programming, and this function provides a simple way to reverse a given string. 
# The function takes one parameter, s, which is the string to be reversed. It uses Python's slicing feature to create a new string that is the reverse of the input string. 
# The reversed string is then returned as the output of the function. This allows for easy manipulation of strings in various applications, such as text processing or data formatting.
def reverse_string(s):
    return s[::-1]  

result = reverse_string("Hello, World!")
print(result)

#Function to check if a string is a palindrome with parameters
#palindrome is a word, phrase, number, or other sequence of characters that reads the same forwards and backwards, ignoring spaces, punctuation, and capitalization. 
#The palindrome function checks if a given string is a palindrome by first converting it to lowercase and removing any spaces. 
# It then compares the cleaned string to its reverse. If they are the same, the function returns True, indicating that the string is a palindrome; otherwise, it returns False. 
# This function can be useful in various applications, such as text analysis or data validation.
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

result = is_palindrome("A man a plan a canal Panama")
print(result)

#Function to convert Celsius to Fahrenheit with parameters
#Celisus are a unit of temperature measurement, and Fahrenheit is another unit of temperature measurement. 
# The Celsius to Fahrenheit function takes one parameter, celsius, and converts it to the equivalent temperature in Fahrenheit using the formula: 
# Fahrenheit = (Celsius * 9/5) + 32.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

result = celsius_to_fahrenheit(0)
print(result)

#Function to convert Fahrenheit to Celsius with parameters
# The Fahrenheit to Celsius function takes one parameter, fahrenheit, and converts it to the equivalent temperature in Celsius using the formula: 
# Celsius = (Fahrenheit - 32) * 5/9.
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

result = fahrenheit_to_celsius(32)
print(result)

#Function to calculate the area of a rectangle with parameters
#Mathematical formula: Area = length * width
#Area of rectangle function takes two parameters, length and width, and returns the area of the rectangle. This function can be called with different values of length and width to calculate the area of various rectangles. The result of the calculation is then printed to the console.
def area_of_rectangle(length, width):
    return length * width

result = area_of_rectangle(5, 3)
print(result)

#Function to calculate the area of a circle with parameters
#Mathematical formula: Area = π * radius^2
#Area of circle function takes one parameter, radius, and returns the area of the circle. This function can be called with different values of radius to calculate the area of various circles. The result of the calculation is then printed to the console.
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

result = area_of_circle(5)
print(result)   

#Function to calculate the area of a triangle with parameters
#Mathematical formula: Area = (base * height) / 2
#Area of triangle function takes two parameters, base and height, and returns the area of the triangle. This function can be called with different values of base and height to calculate the area of various triangles. The result of the calculation is then printed to the console.
def area_of_triangle(base, height):
    return (base * height) / 2

result = area_of_triangle(5, 3)
print(result)

#Function to calculate the perimeter of a rectangle with parameters
#Mathematical formula: Perimeter = 2 * (length + width) 
#Perimeter of rectangle function takes two parameters, length and width, and returns the perimeter of the rectangle. This function can be called with different values of length and width to calculate the perimeter of various rectangles. The result of the calculation is then printed to the console.
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

result = perimeter_of_rectangle(5, 3)
print(result)

#Function to calculate the perimeter of a circle with parameters
#Mathematical formula: Perimeter = 2 * π * radius   
#Perimeter of circle function takes one parameter, radius, and returns the perimeter of the circle. This function can be called with different values of radius to calculate the perimeter of various circles. The result of the calculation is then printed to the console.
def perimeter_of_circle(radius):
    return 2 * math.pi * radius 

result = perimeter_of_circle(5)
print(result)

#Function to calculate the perimeter of a triangle with parameters
#Mathematical formula: Perimeter = side1 + side2 + side3
#Perimeter of triangle function takes three parameters, side1, side2, and side3, and returns the perimeter of the triangle. This function can be called with different values of side1, side2, and side3 to calculate the perimeter of various triangles. The result of the calculation is then printed to the console.
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3    

result = perimeter_of_triangle(5, 3, 4)
print(result)

#Function to calculate the area of a square with parameters
#Mathematical formula: Area = side^2
def area_of_square(side):
    return side ** 2

result = area_of_square(5)
print(result)

#Function to calculate the perimeter of a square with parameters
#Mathematical formula: Perimeter = 4 * side 
def perimeter_of_square(side):
    return 4 * side

result = perimeter_of_square(5)
print(result)

#Function to calculate the area of a parallelogram with parameters
#Mathematical formula: Area = base * height
def area_of_parallelogram(base, height):
    return base * height

result = area_of_parallelogram(5, 3)
print(result)

#Function to calculate the perimeter of a parallelogram with parameters
#Mathematical formula: Perimeter = 2 * (base + side)
def perimeter_of_parallelogram(base, side):
    return 2 * (base + side)

result = perimeter_of_parallelogram(5, 3)
print(result)

#Function to calculate the area of a trapezoid with parameters
#Mathematical formula: Area = (1/2) * (base1 + base2) * height
def area_of_trapezoid(base1, base2, height):
    return (1/2) * (base1 + base2) * height

result = area_of_trapezoid(5, 3, 4)
print(result)

#Function to calculate the perimeter of a trapezoid with parameters
#Mathematical formula: Perimeter = base1 + base2 + side1 + side2
def perimeter_of_trapezoid(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2    

result = perimeter_of_trapezoid(5, 3, 4, 6)
print(result)   

#Function to calculate the area of a rhombus with parameters
#Mathematical formula: Area = (1/2) * diagonal1 * diagonal2     
def area_of_rhombus(diagonal1, diagonal2):
    return (1/2) * diagonal1 * diagonal2

result = area_of_rhombus(5, 3)
print(result)

#Function to calculate the perimeter of a rhombus with parameters
#Mathematical formula: Perimeter = 4 * side 
def perimeter_of_rhombus(side):
    return 4 * side

result = perimeter_of_rhombus(5)
print(result)

#Nested Function
#Nested functions are functions defined inside other functions. They can be useful for encapsulating functionality and creating closures. 
# In this example, we define a nested function called inner_function inside the outer_function. 
# The inner_function is called within the outer_function, and it has access to the variables defined in the outer_function's scope. 
# This allows for more modular and organized code.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function 

result = outer_function(5)(3)
print(result)

#Create a nested function that calculates the area of a rectangle and then uses that area to calculate the perimeter of a rectangle.
def rectangle_area_perimeter(length, width):    
    def area():
        return length * width
    def perimeter():
        return 2 * (length + width)
    return area(), perimeter()  

result = rectangle_area_perimeter(5, 3)
print(result)

#git commit -m "Added functions for basic mathematical operations, geometric calculations, and string manipulations in Python."