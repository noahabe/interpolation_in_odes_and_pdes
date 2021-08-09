#this code implements the naive way of getting an interpolating
#polynomial from a set of data points given.

import numpy as np
import data_reader
import sys

def create_matrix(x_values:list):
	nor = len(x_values) #nor - number of rows
	m = np.empty((nor,nor),dtype=np.float64)
	for i in range(0,nor):
		for j in range(nor-1,-1,-1):
			if j == nor-1:
				m[i,j] = 1
				continue
			m[i,j] = m[i,j+1] * x_values[i]
	return m

def solve_sle(A,b):
	'''solves the sle-system of linear equation'''
	return np.linalg.solve(A,b) 
		
if __name__ == '__main__':
	help_message = f"""
	Usage: {sys.argv[0]} <filename> [p|d]
	* the first option is for the filename
	* the second option is p - for python version, d - for desmos version 
	"""
	
	if len(sys.argv) != 3:
		print(help_message)
		exit(1)

	f = data_reader.InterpolationData(sys.argv[1])	
	data = f.get_data_in_two_lists() 
	m = create_matrix(data[0])	
	coeff = solve_sle(m,data[1])

	output = ""
	MODE = sys.argv[2] 

	if MODE == 'p':	
		output += "f = lambda x : "

	for i in range(len(coeff)):
		if i != 0:
			output += '+'
		output += str(coeff[i]) 
		if i == len(coeff) - 1:
			continue
		output += '*x'
		if MODE == 'p':
			output += '**'
		elif MODE == 'd':
			output += '^'
		output += str(len(coeff)-1-i)
		output += ' '
	print(output)
