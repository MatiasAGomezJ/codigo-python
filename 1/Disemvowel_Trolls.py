from os import system
from time import sleep

def clear():
    system('clear')

def disemvowel(string_):
    s2 = ""
    for c in range(len(string_)):
        if string_[c] == 'a' or string_[c] == 'e' or string_[c] == 'i' or string_[c] == 'o' or string_[c] == 'u' or string_[c] == 'A' or string_[c] == 'E' or string_[c] == 'I' or string_[c] == 'O' or string_[c] == 'U': 
            continue
        s2 += string_[c]
    return s2

## -----
clear()

text = "Hello my name is Markiplier and today, we are again, in Five Nights At Freddy's"
print(disemvowel(text))

sleep(5.5)
clear()