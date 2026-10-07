# Conditions in Python
#Conditions are used to perform different actions based on different conditions. In Python, we use if, elif, and else statements to implement conditional logic.
#Applying conditions in Python allows us to control the flow of our program and make decisions based on certain criteria. Below are some examples of how to use conditions in Python: 
#1. If Statement
#If statement is used to execute a block of code if a specified condition is true. The syntax of an if statement is as follows:
#Syntax:
# if condition:
    # block of code to be executed if the condition is true
#Example:
x = int(input("Please enter the value of x: "))
if x > 5:
    print("x is greater than 5")
#2. If-Else Statement
#If-Else statement is used to execute a block of code if a specified condition is true, and another block of code if the condition is false. The syntax of an if-else statement is as follows:
#Syntax:
# if condition:
    # block of code to be executed if the condition is true
# else:
    # block of code to be executed if the condition is false
#Example:
x = int(input("Please enter the value of x: "))
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
    
#3. If-Elif-Else Statement
#If-Elif-Else statement is used to execute one block of code if a specified condition is true, and another block of code if the condition is false, and yet another block of code if the first two conditions are false. The syntax of an if-elif-else statement is as follows:
#Syntax:
# if condition1:
    # block of code to be executed if condition1 is true
# elif condition2:
    # block of code to be executed if condition1 is false and condition2 is true
# else:
    # block of code to be executed if both condition1 and condition2 are false
#Example:
x = int(input("Please enter the value of x: "))
y = int(input("Please enter the value of y: "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

#4. Nested If Statement
#Nested If statement is used to execute a block of code if a specified condition is true, and another block of code if the condition is false, and yet another block of code if the first two conditions are false. The syntax of a nested if statement is as follows:
#Syntax:
# if condition1:
    # block of code to be executed if condition1 is true
#     if condition2:
        # block of code to be executed if condition1 is true and condition2 is true
#     else:
        # block of code to be executed if condition1 is true and condition2 is false
# else:
    # block of code to be executed if condition1 is false
#Example:
a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
if a > b:
    if a > 10:
        print("a is greater than b and also greater than 10")
    else:
        print("a is greater than b but not greater than 10")
        
        