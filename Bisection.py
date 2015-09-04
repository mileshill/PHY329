# Miles Hill
# UT PHY 329
# FALL 2015

# Bisection.py solves for the root of the given function between the 
# given bounds lower,upper and max iterations maxSteps

# Input is taken from the command line:
# >>> python Bisection.py "lambda x: x**2" "-1" "1" "10"
# interpreter fileName lambda lowerBound upperBound maxSteps

##########
# Imports
##########
from sys import argv, stdin, stdout
import math

##########
# BISECTION
##########
def bisection( func, lower, upper, maxSteps ):
	# local vars
	a , b = lower, upper

	# initialized vars
	i = 1
	FA = func( lower )
	
	# iterative solution
	while i < maxSteps:
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


##########
# MAIN
##########
def main():

	# parse commandline input
	f = eval( argv[1] )							# function
	a, b = float( argv[2] ), float( argv[3] )	# float bounds
	maxsteps = int( argv[4] )					# int maxSteps

	# determine root
	root = bisection( f, a, b, maxsteps )

	# output
	stdout.write(  str(root) )



##########
# EVALUATION
##########
if __name__ == "__main__":
	main()
	