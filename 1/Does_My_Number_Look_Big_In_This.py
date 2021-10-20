from os import system
from time import sleep

def clear():
    system('clear')

def narcissistic(value):
    num_string = str(value)
    len_num = len(num_string)
    total = 0
    for i in range(len_num):
        total += int(num_string[i]) ** len_num
    if total == value:
        return True
    else:
        return False

## -----
clear()

num = 122 
print(narcissistic(7))
print(narcissistic(371))
print(narcissistic(num))
print(narcissistic(4887))
sleep(5.5)
clear()