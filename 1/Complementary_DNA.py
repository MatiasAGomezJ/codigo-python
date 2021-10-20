from os import system
from time import sleep

def clear():
    system('clear')

def DNA_strand(var):
    r = range(len(var))
    l = ""
    newvar = ""
    for i in r:
        if var[i] == "A":
            l = "T"
        if var[i] == "T":
            l = "A"
        if var[i] == "C":
            l = "G"
        if var[i] == "G":
            l = "C"
        newvar += l
    return newvar

## -----
clear()

string = "ACATG"
print(DNA_strand(string))
sleep(5.5)
clear()