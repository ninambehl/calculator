import streamlit as s

s.title("Calculator")
s.text("Welcome to the calculator! To get started, follow the instructions below.")


# def multiplication(x, y):
#     return x * y
# def division(x, y):
#     return x / y
# def addition(x, y):
#     return x + y
# def subtraction(x, y):
#     return x - y
# def squared(x):
#     return x^2

n1 = s.number_input("Enter first number: ")
operation = s.selectbox("Pick your operation", ["x", "/", "+", "-", "^", "%", "//"])
if operation != "^":
    n2 = s.number_input("Enter second number: ")
    if operation == "x":
        s.text(str(n1) + " " + operation + " " + str(n2) + " = " + str(n1 * n2))
    elif operation == "/":
        if n2 != 0:
            s.text(str(n1) + " " + operation + " " + str(n2) + " = " + str(n1 / n2))
        else:
            s.text("The answer is undefined")
    elif operation == "+":
        s.text(str(n1) + " " + operation + " " + str(n2) + " = " + str(n1 + n2))
    elif operation == "%":
        s.text(str(n1) + " " + operation + " " + str(n2) + " = " + str(n1 % n2))
    elif operation == "//":
        s.text(str(n1) + " " + operation + " " + str(n2) + " = " + str(n1 // n2))
    else:
        s.text(str(n1) + " " + operation + " " + str(n2) + " = " + str(n1 - n2))
else:
    s.text(n1 + " " + operation + " 2 =" + str(n1**2))
