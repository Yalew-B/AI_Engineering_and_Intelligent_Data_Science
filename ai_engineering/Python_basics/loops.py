#Loops in Python
#Loops are used to execute a block of code repeatedly until a certain condition is met. In Python, we have two types of loops: for loops and while loops.
#Applying loops in Python allows us to automate repetitive tasks and iterate over sequences of data. Below are some examples of how to use loops in Python:
#1. For Loop
#For loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. The syntax of a for loop is as follows:
#Syntax:
# for item in sequence:
    # block of code to be executed for each item
#Example:
fruits = ["apple", "banana", "cherry"]  
for fruit in fruits:
    print(fruit)

#2. While Loop
#While loop is used to execute a block of code repeatedly as long as a specified condition is true. The syntax of a while loop is as follows:
#Syntax:    
# while condition:
    # block of code to be executed as long as the condition is true 
#Example:
count = int(input("Please enter the starting value of count: "))
end = int(input("Please enter the ending value of count: "))
while count < end:
    print(count)
    count += 1
    