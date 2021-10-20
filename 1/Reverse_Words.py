from os import system
from time import sleep

def clear():
    system('clear')

def reverse_words(var):
    bol = True
    array2 = []
    var2 = ""
    s = ""
    start = 0
    finish = 0
    for i in range(len(var)):
        s = ""
        finish += 1
        if var[i] == " ":
            s += var[i]
            array2.append(s)
            start = i+1
        if var[i] == " " and var[i+1] == " ":
            continue
        if i == len(var)-1:
            finish = len(var)
            rango = range(finish-start)
            for j in rango:
                s += var[start+j]
            array2.append(s)
            break
        if var[i+1] == " ":
            rango = range(finish-start)
            for j in rango:
                s += var[start+j]
            array2.append(s) 
    for i in range(len(array2)):
        var2 += (array2[i].replace(array2[i], array2[i][::-1]))
    return var2
## -----
clear()
for jota in range(1):
    print(jota)
string = "Los electrones no son bolitas en el espacio, sino ondas que se mueven por un campo invisible"
string = "ax bx cx  dx ex fx"
print("a" + string[3] + "b")
print(reverse_words(string))