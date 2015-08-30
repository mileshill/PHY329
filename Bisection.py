from sys import argv, stdin, stdout
import math


def bisection( func, lower, upper, maxSteps ):

	# local vars
	a , b = lower, upper


	i = 1
	FA = func( lower )

	while i < maxSteps:
		p = a + (b-a)/2
		FP = func(p)

		if not FP: return p

		if FA * FP > 0.:
			a = p
			FA = FP
		else:
			b = p

		i += 1

	return p



def main():

	f = eval( argv[1] )
	a, b = float( argv[2] ), float( argv[3] )
	maxsteps = int( argv[4] )

	root = bisection( f, a, b, maxsteps )

	print( root )

if __name__ == "__main__":
	main()
	