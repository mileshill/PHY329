# Chapter 5: problem 7
import numpy as np
import NumericalMethods as num
import decimal
from collections import OrderedDict


#-----------------------------------------------------------
# Helper functions
#-----------------------------------------------------------

def eng_form(x_float):
	"""
	if x_float > 99, chop the decimal portion and return in engineering form
	"""
	dec, integer = np.modf(x_float)

	if len( str(integer)) > 4 :
		return decimal.Decimal( integer ).normalize().to_eng_string()
	else:
		return x_float


#-----------------------------------------------------------
# C5 P7: Solve using Bisection, FalsePosition. maxSteps = 3
#-----------------------------------------------------------
def c5p7():

	f,a,b,*kwargs = [lambda x: np.log( x**2 ) - 0.7,  0.5,  2.0, {'maxSteps':3}]

	return {'bisection':num.bisection( f,a,b,**kwargs[0] ), 'false_position':num.false_position( f,a,b,**kwargs[0] )}

#-----------------------------------------------------------
# C5 P16: Solve using Bisection, FalsePosition
#	solving for root == N
# 	doping density as a function of resistivity
#-----------------------------------------------------------

def c5p16():
	# Given functions:
	def rho(q, n, mu):
		return 1.0 / ( q * n * mu )

	def n( N, ni ):
		return 0.5 * ( N + np.sqrt( N**2 + 4 * ni**2 ) )

	def mu( T, T0, mu0 ):
		return mu0 * ( T / T0 )**(-2.42)

	# Constants
	T0, T, mu0, q, ni, rho_desired = 300., 1000., 1360., 1.7 * 10**(-19), 6.21 * 10**9, 6.5 * 10**6

	# args for solutions
	f = lambda N: rho( q, n(N,ni), mu(T,T0,mu0) ) - rho_desired
	a,b = 0., 2.5 * 10**10

	return {'bisection': eng_form( num.bisection( f,a,b ) ),'false_position':eng_form( num.false_position(f,a,b) ) }

#-----------------------------------------------------------
# C5 P22: Solve using Bisection, FalsePosition. 
#	solving for root == h
# 	Floating Equilibrium
#-----------------------------------------------------------
def c5p22():
	# Given Functions
	def force_grav( rho_object, v, g=9.8 ):
		return rho_object * v * g

	def force_buoy( rho_medium, v_displaced, g=9.8 ):
		return rho_medium * v_displaced * g

	def vol_sphere( rad ):
		return 4.0/3 * np.pi * rad**3

	def vol_dry( rad, h ):
		return (np.pi * h**2 / 3) * (3 * rad - h)

	def vol_disp( rad, h ):
		return vol_sphere(rad) - vol_dry( rad, h )

	# Constants
	rho_object, rho_medium, rad = 200., 1000., 1.
	# args for solutions
	f = lambda h: force_grav( rho_object, vol_sphere( rad )) - force_buoy( rho_medium, vol_disp( rad,h ))
	a,b = 0.,2.

	return {'bisection': num.bisection( f,a,b ) ,'false_position':eng_form( num.false_position(f,a,b) ) }

#-----------------------------------------------------------
# C6 P22: Solve using NewtonRaphson. 
#	
#-----------------------------------------------------------
def c6p19():
	# Impedance
	def z(r, c, l, w):
		return np.sqrt( r**(-2) + ( w * c - (w * l)**(-1) )**2 )**(-1)

	# Constants
	r, c, l, z_desired = 225., 0.6 * 10**(-6), 0.5, 100.

	# Args for solution
	f = lambda w: z(r, c, l, w) - z_desired
	x0, x1, dx = 210, 215, 10**(-4)

	return {'newton_raphson': num.newton_raphson( f,x0 ), 'secant_method': num.secant_method( f, x0, x1 ), 'modified_secant': num.modified_secant( f,x1,dx) }

# Solutions
solutions = OrderedDict()
solutions['Chapter 5: Problem 7']  = c5p7()
solutions['Chapter 5: Problem 16'] = c5p16()
solutions['Chapter 5: Problem 22'] = c5p22()
solutions['Chapter 6: Problem 19'] = c6p19()

 