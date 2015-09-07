#!/usr/bin/python3
__author__ = "MilesHill"
# Miles Hill
# UT PHY 329
# FALL 2015



##########
# Imports
##########
from sys import stdout

import Homework1

##########
# MAIN
##########
def main():
	stdout.write("MILES HILL: mjh3664\n")
	stdout.write("Homework 1\n")
	stdout.write("UT PHY 329\n")
	stdout.write("FALL 2015\n")

	form = "{0:<20}{1:<20}\n"
	
	stdout.write('\n')
	for prob,sol in Homework1.solutions.items():
		stdout.write( prob + '\n')

		for method, approx in sol.items():
			stdout.write( form.format(method, approx) )

		stdout.write('\n')



##########
# EVALUATION
##########
if __name__ == "__main__":
	main()
	