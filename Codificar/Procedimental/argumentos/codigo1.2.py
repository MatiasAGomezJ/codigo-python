# 1. Arguments and Shared References
# Paso de objetos mutables:

def changer(a, b):	# Arguments assigned references to objects
	a = 2			# Changes local name's value only
	b[0] = 'spam' 	# Changes shared object in place

X = 1
L = [1, 2]
changer(X, L) # Caller: Pass immutable and mutable objects

# X is unchanged, L is different!
print(X, L)

###------------------------------------------------------------------------------

# Evitar que una routina modifique los elementos mutables:
# Opción 1:

X = 1
L = [1, 2]
changer(X, L[:])	# Pass a copy, so our 'L' does not change 

print(X, L)

###------------------------------------------------------------------------------

# Opción 2:

X = 1
L = [1, 2]
#changer(X, tuple(L))	# Pass a tuple, so changes are errors

###------------------------------------------------------------------------------

# Opción 3:

def changer(a, b):
	b = b[:]		# Copy input list so we don't impact caller
	a = 2
	b[0] = 'spam'	# Changes our list copy only

X = 1
L = [1, 2]
changer(X, L)
print(X, L)