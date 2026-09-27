# Project 1    Calculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiple(a,b):
    return a * b

def divide(a,b):
    return a / b

num1 = float(input("Enter First Number: "))
operator = input("Enter Operator (+, -, *, /): ")

num2 = float(input("Enter Second Number: "))

if operator == "+":
    print("Result: ", add(num1,num2))

elif operator == "-":
    print("Result: ",subtract(num1,num2))

elif operator == "*":
    print("Result: ",multiple(num1,num2))

elif operator == "/":
    if num2 != 0:
        print("Result: ",divide(num1,num2))
    else:
        print("Cannot Divide By Zero")

else:
    print("Invalide Operator")

    

