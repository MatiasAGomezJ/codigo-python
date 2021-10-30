# 1. Arguments and Shared References
# Paso de objetos inmutables:

def f(a):	# a is assigned to (references) the passed object
	a = 99 	# Changes local variable a only

b = 88		
f(b)		# a and b both reference same 88 initially
print(b)	# b is not changed
