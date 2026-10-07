#1. Arithmetic Operators
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

#Addition    
print("The sum of x and y is: ", x + y)
#Subtraction
print("The difference of x and y is: ", x - y)
#Multiplication
print("The product of x and y is: ", x * y)
#Division
print("The quotient of x and y is: ", x / y)
#Modulus
print("The remainder of x and y is: ", x % y)
#Exponentiation
print("The result of x raised to the power of y is: ", x ** y)

#2. Comparison Operators
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
#Equal to
print("Is a equal to b? ", a == b)
#Not equal to
print("Is a not equal to b? ", a != b)
#Less than
print("Is a less than b? ", a < b)
#Greater than
print("Is a greater than b? ", a > b)
#Less than or equal to
print("Is a less than or equal to b? ", a <= b)
#Greater than or equal to
print("Is a greater than or equal to b? ", a >= b)

#3. Logical Operators
p = bool(int(input("Enter 1 for True, 0 for False: ")))
q = bool(int(input("Enter 1 for True, 0 for False: ")))
#Logical AND
print("The result of p AND q is: ", p and q)
#Logical OR
print("The result of p OR q is: ", p or q)
#Logical NOT
print("The result of NOT p is: ", not p)

#4. Assignment Operators
m = int(input("Enter the value of m: "))
print("The value of m is: ", m)
#Addition assignment
m += 5      
print("After addition assignment, the value of m is: ", m)
#Subtraction assignment
m -= 3
print("After subtraction assignment, the value of m is: ", m)
#Multiplication assignment
m *= 2  
print("After multiplication assignment, the value of m is: ", m)
#Division assignment    
m /= 4
print("After division assignment, the value of m is: ", m)  
#Modulus assignment
m %= 3
print("After modulus assignment, the value of m is: ", m)
#Exponentiation assignment
m **= 2 
print("After exponentiation assignment, the value of m is: ", m)    

#5. Bitwise Operators
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
#Bitwise AND
print("The result of num1 AND num2 is: ", num1 & num2)
#Bitwise OR
print("The result of num1 OR num2 is: ", num1 | num2)
#Bitwise XOR
print("The result of num1 XOR num2 is: ", num1 ^ num2)
#Bitwise NOT
print("The result of NOT num1 is: ", ~num1)
#Left shift
print("The result of left shift of num1 by 2 is: ", num1 << 2)
#Right shift
print("The result of right shift of num1 by 2 is: ", num1 >> 2) 
