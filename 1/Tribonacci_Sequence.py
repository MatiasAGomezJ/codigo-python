from os import system
from time import sleep

def clear():
    system('clear')

def tribonacci(array, n):
    restantes = n - len(array)
    new_array = []

    if n <= 3:
        if n == 1:
            new_array.append(array[0])
        if n == 2:
            new_array.append(array[0])
            new_array.append(array[1])
        if n == 3:
            new_array = array
        return new_array

    for i in range(restantes):
        new_array = array
        new_number = new_array[i+3-3] + new_array[i+3-2] + new_array[i+3-1]
        new_array.append(new_number)
    return new_array
## -----
clear()

array = [1,2,3]
n = 0
print(tribonacci(array, n))
sleep(5.5)
clear()