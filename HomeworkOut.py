#!/usr/bin/python3
__author__ = "MilesHill"
# Miles Hill
# UT PHY 329
# FALL 2015



##########
# Imports
##########
from sys import stdout

import Homework2

##########
# MAIN
##########
def main():
	stdout.write("MILES HILL: mjh3664\n")
	stdout.write("Homework 2\n")
	stdout.write("UT PHY 329\n")
	stdout.write("FALL 2015\n")

	form = "{0:<20}\n{1:<20}\n"
	
	stdout.write('\n')
	for prob,sol in Homework2.solutions.items():
		stdout.write( prob + '\n')

		for method, approx in sol.items():
			stdout.write( form.format( method, str(approx) ))

		stdout.write('\n')



##########
# EVALUATION
##########
if __name__ == "__main__":
	main()
	