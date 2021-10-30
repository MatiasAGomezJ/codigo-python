# 3. Defaults

# defaults allow us to make selected function arguments optional; 
# if not passed a value, the argument is assigned its default before the function
# runs.

def f(a, b=2, c=3): 	# a required, b and c optional
	print(a, b, c)


f(1)
f(a=1)

###------------------------------------------------------------------------------

# If we pass two values, only c gets its default, and with three values, no defaults are used:

f(1, 4)
f(1, 4, 5)	# Override defaults

f(1, c=6)	# Choose defaults