from os import system
from time import sleep

def clear():
    system('clear')

def connotation(string):
    string = string.lower()
    string = string.split()
    a = 0
    n = 0
    for i in string:
        if ord('a') <= ord(i[0]) <= ord('m'):
            a += 1
        elif ord('n') <= ord(i[0]) <= ord('z'):
            n += 1
    if a >= n:
        return True
    else:
        return False    

## -----
clear()

string = "Hay 1000 metros en 1 kilometro" 
string = "All FOoD tAsTEs NIcE for someONe"
print(connotation(string))
sleep(5.5)
clear()