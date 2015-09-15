import numpy as np
from numpy.linalg import inv, det
import NumericalMethods as num
from collections import OrderedDict

##############################################################################################
# Chapter 8: problem 3
# 	Given the coefficient and solution arrays: 
#		solve the linear system x-vector. ( A.x == b )
#   	compute the transpose of the coefficient array
#		compute the inverse of the coefficient array
def c8p3():
	A = np.array([[0,-6,5],[0,2,7],[-4,0,-4]])

	b = np.array([[50],[-30],[50]])

	return {'Solution Vector':num.gauss_elimination(A,b),"Coefficient Transpose": np.transpose(A),"Coefficient Inverse": inv(A) }

##############################################################################################
# Chapter 8: problem 11
# 	Given the system of equations for the 3-mass 4-spring system, and the values
# 	of k{1,2,3,4} and m{1,2,3}, and displacement vector x, 
#	compute the acceleration vector
#  		0 = a + W.x
def c8p11():
	k1 = k4 = 10.
	k2 = k3 = 40.
	m1 = m2 = m3 = 1.

	coeff = np.array([	[ (k1 + k2)/m1, -k2/m1, 0 ], 
						[ -k2/m2, (k2 + k3)/m2, -k3/m3 ], 
						[0, -k3/m3, (k3 + k4)/m3]	], dtype=float)

	disp = np.array([	[0.05],
						[0.04],
						[0.03]],	dtype=float)

	return {"Acceleration Vector": np.dot(-coeff, disp)}

##############################################################################################
# Chapter 8: problem 11
# 	Given the system of equations
#	compute the coefficent array determinant
#	solve for x-vector
#	modify value coeff[1,1]:
#		compute det
#		solve system 
def c9p5():
	A = np.array([	[0.5, -1],
					[1.02, -2]
				],dtype=float)

	A2 = np.array([	[0.52, -1],
					[1.02, -2]
				],dtype=float)

	b = np.array([	[-9.5],
					[-18.8]
				],dtype=float)



	return {'Coefficient Det': det(A), 'Solution Vector': np.dot(inv(A),b),'Modified Det': det(A2),'Modified Solution': np.dot(inv(A2),b) }

# Solutions
solutions = OrderedDict()
solutions['Chapter 8: Problem 3'] = c8p3()
solutions['Chapter 8: Problem 11'] = c8p11()
solutions['Chapter 9: Problem 5'] = c9p5()








