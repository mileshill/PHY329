##########
# BISECTION
##########
def bisection( func, lower, upper, maxSteps=10,tol=10**(-6) ):
	# local vars
	a , b = lower, upper

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