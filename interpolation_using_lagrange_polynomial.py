def lagrange_interpolation_evaluation(x_values:list,y_values:list,x:float):
	'''
	Returns the result of the interpolated polynomial evaluated
	at x.
	Source of Algorithm: Applied Numerical Analysis page 163 of 620
	'''

	assert(len(x_values) == len(y_values))
	
	result = 0
	
	for i in range(0,len(x_values)):
		P = 1 
		for j in range(0,len(x_values)):
			if j != i:
				P *= (x-x_values[j])/(x_values[i]-x_values[j]) 	
		result += P * y_values[i]
	return result
	

if __name__ == '__main__':
	a = lagrange_interpolation_evaluation(
		[3.2,2.7,1.0,4.8],
		[22,17.8,14.2,38.3],
		3)
	print(a)

