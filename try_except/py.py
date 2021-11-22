sep = '-' * 45 + '\n'

#---------------------------------------------------

print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

#---------------------------------------------------

print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

#---------------------------------------------------

print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

#---------------------------------------------------

print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    # x = 1 / 0
    pass
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

#---------------------------------------------------

print(sep + 'EXCEPTION RAISED, con except correcto')
try:
    x = 1 / 0
except ZeroDivisionError:
    print('except run')
finally:
    print('finally run')
print('after run')

#---------------------------------------------------

print(sep + 'EXCEPTION RAISED, con mas de un except')
try:
    x = 1 / 0
except IndexError:
    print('except 1 run')
except ZeroDivisionError:
    print('except 2 run')
finally:
    print('finally run')
print('after run')

#---------------------------------------------------

print(sep + 'EXCEPTION RAISED, con except as x')
try:
    x = 1 / 0
except ZeroDivisionError as exce:
    print(exce)
finally:
    print('finally run')
print('after run')