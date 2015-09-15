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
#	optional assignments of maxSteps and tolerance.
# Note that the package <numdifftools> is imported to handle the
#	numerical derivatives  
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

#----------- MATRIX COMPUTATION --------------------------------------

######################################################################
# Gaussian Elimination:
# Take an augmented matrix of dimentions ( n, n + 1 )
#	return solutions 
########################==##############################################
def gauss_elimination( A, b, doPricing = True ):
	"""
	Gaussian elimination wih partial pivoting

	input: 	A is an n x n numpy matrix
			b is an n x 1 numpy array
	output: x is the solution of A.x = b
			with ten entries permuted in accordance 
			with the pivoting done by the algorithm
	post-condition: A and b have been modified
	"""
	import numpy as np

	A = np.array(A)
	b = np.array(b)
	n = len(A)
	if b.size != n:
		raise ValueError("Invalid argument: incompatiable sizes between" +
				"A & b.", b.size, n)

	# k represents the current pivot row. Since GE traverses the matrix in the
	# upper right triangle, we also use k for indicating the k-th diagonal
	# column index

	# Elimination
	for k in range(n - 1):
		if doPricing:
			# Pivot
			maxindex = abs(A[k:,k]).argmax() + k
			if A[maxindex, k] == 0:
				raise ValueError("Matrix is singular.")
			# Swap
			if maxindex != k:
				A[[k, maxindex]] = A[[maxindex, k]]
				b[[k, maxindex]] = b[[maxindex, k]]
			else:
				if A[k, k] == 0:
					raise ValueError("Pivot element is zero. Try setting doPricing to True")

	# Back Substitution
	x = np.zeros(n)
	for k in range(n-1, -1, -1):
		x[k] = (b[k] - np.dot(A[k, k+1:], x[k+1:])) / A[k,k]
	return x 





	




























