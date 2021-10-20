from os import system
from time import sleep
import string

def clear():
    system('clear')

def creador(var):
    punct = string.punctuation
    for a in punct:
        var = var.replace(a, "")
    var = string.capwords(var)
    var = var.replace(" ", "_")
    print(var)

## -----
clear()

texto = "Does my number look big in this"
creador(texto)