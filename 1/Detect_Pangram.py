from os import system
from time import sleep
import string

def clear():
    system('clear')


def is_pangram(s):
    s = s.lower()
    for i in string.ascii_lowercase:
        if i not in s:
            return False
    return True

## -----
clear()

pangram = "Pack my box with five dozen liquor jugs."
print(is_pangram(pangram))
sleep(5.5)
clear()