from os import system
from time import sleep

def clear():
    system('clear')

def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

## -----
clear()

op = "+"
num1 = 5
num2 = 8
print(basic_op(op, num1, num2))

sleep(5.5)
clear()