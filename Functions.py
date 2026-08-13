print("Creating Different Types Of Functions")
import math
def sqrt(a):
    sqrt = math.sqrt(a)
    return sqrt
def ceil(a):
    ceil = math.ceil(a)
    return ceil
def floor(a):
    floor = math.floor(a)
    return floor
def square(a):
    sq = a**2
    return sq
# try:
#     n = int(input("Enter A Number: "))
#     m = int(input("Enter Another Number: "))
#     operation = input("Enter a Operation: ")
# except ValueError:
#     print("Invalid Input! Enter A Valid Input.")
n = 0
def cube(a):
    cb = a**3
    return cb
def sum(a,b):
    sum = a+b
    return sum
def multiply(a,b):
    multiply = a*b
    return multiply
def even_odd(a):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
def largest(a,b):
    if a > b:
        return a
    else:
        return b
def factorial(a):
    if a < 0:
        return "Factorial Doesn't Exist."
    elif a == 0 or a == 1:
        return "Factorial for Given Number Is One."
    else:
        fact = 1
        for i in range(2,a+1):
            fact *= i
        return fact
def power(a,b):
    res = 1
    for i in range(b):
        res *= a
    return res
# name = input("Enter Your Name: ")
def greet(name, message = "Hello "):
    greet = message + name
    return greet
def Calculator(a,b,operation):
    if operation == "+":
        sum = a+b
        return sum
    elif operation == "-":
        sub = a-b
        return sub
    elif operation == "*":
        mul = a*b
        return mul
    elif operation == "/":
        div = a/b
        return div
    else:
        return a,b
def prime(a):
    count = 0
    for i in range(1,a+1):
        if a % i == 0:
            count += 1
    if count > 2:
        return a,"Is Not a Prime Number."
    else:
        return a, "IS a Prime Number."

def SumOfNumbers(a):
    if a == 0:
        return 0
    return a + SumOfNumbers(a-1)
def recfact(a):
    if a == 1 or a == 0:
        return 1
    return a * recfact(a-1)
def fibonacci(a):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    return fibonacci(a-1) + fibonacci(a-2)
result = fibonacci(n)