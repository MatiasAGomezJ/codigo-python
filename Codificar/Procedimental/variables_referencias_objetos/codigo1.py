# OBJETOS INMUTABLES

a = 3
b = a
print(b)

print('------0')
###----

a = 3
b = a
a = 'spam'
print(b)

print('------1')
###----

# Los objetos integer no son mutables

a = 3
b = a
a = a + 2
print(b)

print('------2')
###------------------------------------------------------------------------------

# OBJETOS MUTABLES

L = [2, 3, 4]	# A mutable object
M = L			# Make a reference to the same object
L[0] = 24 		# An in-place change
print(L)
# Output: ([24, 3, 4])

print(M)
# Output: ([24, 3, 4])

print('------3')
###----

# Copia de objetos en vez de referencia:

L = [2, 3, 4]
M = L[:]		# Make a copy of L (or list(L), copy.copy(L), etc.)
L[0] = 24
print(L)
# Output: ([24, 3, 4])

print(M)   # M is not changed
# Output: ([2, 3, 4])			

print('------4')
###----

# Shared References and Equality

L = [1, 2, 3]
M = L 			    # M and L reference the same object
print(L == M)	    # Same values => operador igualdad de valores
# Output: (True)

print(L is M)	    # operador identidad de objetos: compara las referencias (los
# Output: (True)    # punteros)

print('------5')
###----

L = [1, 2, 3]
M = [1, 2, 3]	    # M and L reference different objects
print(L == M)	    # Same values
# Output: (True)

print(L is M)       # operador identidad de objetos: compara las referencias
# Output: (False)   # (los punteros)

print('------6')
###----

# CACHE:

X = 42
Y = 42		        # Should be two different objects
print(X  == Y)
# Output: (True)

print(X is Y)       # Same object anyhow: caching at work!!!!!!!!
# Output: (True)

print('------7')
###----

# Because small integers and strings are cached and reused, though, is tells us they reference the same single object.

# averiguar el numero de refencias a un objeto:

import sys
print(sys.getrefcount(1))
# Output: (647)             # 647 pointers to this shared piece of memory