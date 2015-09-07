#----------------------------------------------------------------------
# NumericalMethods 
#----------------------------------------------------------------------



# -------------------- BRACKETING METHODS (Closed)---------------------

######################################################################
# BISECTION:
# Takes as input a function, lower and upper interval bounds as
#	optional assignments of maxSteps and tolerance. 
######################################################################
def bisection( func, lower, upper, maxSteps=100,tol=10**(-6) ):
	"""
	input: func = lambda x: f(x), float(x_l), float(x_u)
	return: float( approximate root )
	"""
	# local vars
	a , b = lower, upper

	try:
		assert a < b
	except AssertionError:
		return "ARGUMENT ERROR:\n x_lower !< x_upper\n "

	# initialized vars
	i = 1
	FA = func( lower )
	
	# iterative solution
	while (i < maxSteps) or ((b-a) > tol):
		p = a + (b-a)/2		# mid-point of interval
		FP = func(p)	

		if not FP: return p # if FP == 0, return p; break;
		
		# Check sign of interval and adjust 
		if FA * FP > 0.:
			a = p
			FA = FP
		else:
			b = p

		i += 1
	#end while
	return p


######################################################################
# FALSEPOSITION:
# Takes as input a function, lower and upper interval bounds as
#	optional assignments of maxSteps and tolerance and absolute error (eps). 
######################################################################
def false_position( func, lower, upper, maxSteps=100,tol=10**(-6) ):
	"""
	input: func = lambda x: f(x), float(x_l), float(x_u)
	return: float( approximate root )
	"""
	# local vars
	a , b = lower, upper

	try:
		assert a < b
	except AssertionError:
		return "ARGUMENT ERROR:\n x_lower !< x_upper\n "

	# initialized vars
	i = 1
	FA = func( lower )
	FB = func( upper )

	# iterative solution
	while (i < maxSteps) and (abs(b - a) > tol):
			
		p = b - (( func( b ) * ( a - b )) / (func(a)-func(b)))	# straight line intersection
		FP = func(p)	

		if not FP: return p # if FP == 0, return p; break;
		
		# Check sign of interval and adjust 
		if FA * FP > 0.:
			a = p
			FA = FP
		else:
			b = p 
			FB = FP

		i += 1
	#end while
	return p

# -------------------- OPEN METHODS ----------------------------
######################################################################
# NewtonRaphson:
# Takes as input a function and initial root guess
#	optional assignments of maxSteps and tolerance  
######################################################################
def newton_raphson( f, x0, maxSteps=10, tol=10.**(-6) ):
	import numdifftools as nd
	fp = nd.Derivative( f )
	
	i = 1;
	a = x0


	while (i < maxSteps):
		
		b = a - f(a) / fp(a)

		if ( b - a ) < tol: return b

		a = b
		i += 1
	# end while
	return b

######################################################################
# Secant method:
# Takes as input a function and initial steps x0, x1
#	optional assignments of maxSteps and tolerance  
######################################################################
def secant_method( f, x0, x1, maxSteps=10, tol=10.**(-6) ):
	i = 1
	a, b = x0, x1
	while (i < maxSteps) and (abs(b-a) > tol):
		c = b - (( f( b ) * ( a - b ) )/ ( f( a )-f( b ) ) )

		if abs( c - b ) < tol: return c

		a, b = b, c
		i += 1
	# end while
	return c

######################################################################
# Modified secant method:
# Takes as input a function and initial root guess and perturbation dx
#	optional assignments of maxSteps and tolerance  
######################################################################
def modified_secant( f, x0, dx, maxSteps=10, tol=10.**(-6) ):
	i = 1
	a = x0

	while (i < maxSteps):
		b = a - (( dx * a * f( a ) ) / ( f( a + dx * a ) - f( a ) ))

		if abs( b - a ) < tol: return b

		a = b
		i += 1
	# end while
	return b
