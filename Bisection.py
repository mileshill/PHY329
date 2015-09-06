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
import numpy as np
from NumericalMethods import bisection
from sys import stdout

##########
# MAIN
##########
def main():

	# input for bisection
	f = lambda x: np.log( x**2 ) - 0.7
	a,b = 0.5, 2.0
	# determine root
	root = bisection( f, a, b )

	# output
	stdout.write(  str(root) )
	stdout.write( "\n" )



##########
# EVALUATION
##########
if __name__ == "__main__":
	main()
	