import numpy as np
import data_reader
import sys

def newton_interpolation(x_values:list,y_values:list,x:float):
	nor = len(x_values) #nor - number of rows

	#DT - Difference Table
	#DT[i,i] = f[x_i]
	#DT[i,j] = f[x_i,x_(i+1),...,x_j] for j > i
	
	DT = np.zeros((nor,nor),dtype=np.float64)

	
	###############[calculate the kth divided difference]###############
	for i in range(0,nor):
		DT[i,i] = y_values[i]
	for m in range(1,nor):
		for j in range(0,nor-m):
			DT[j,j+m] = (DT[j+1,j+m] - DT[j,j+m-1])/(x_values[j+m]-x_values[j])
			
	#print(DT) #for debugging purposes only.
		

	##############[evaluate the interpolating polynomial at x]##########
	p = np.zeros(nor,dtype=np.float64)
	p[0] = y_values[0]
	for k in range(1,nor):
		p[k] = p[k-1]
		g = 1
		for i in range(0,k):
			g *= (x - x_values[i])
		g *= DT[0,k]
		p[k] += g 
	
	return p[nor-1] 

if __name__ == '__main__':
	help_message = f"""
	Usage: python3.7 {sys.argv[0]} <filename> x 
	* the first option is for the filename
	* the second option is the point you want to evaluate the interpolating polynomial. 
	"""

	if len(sys.argv) != 3:
		print(help_message)
		exit(1)

	f = data_reader.InterpolationData(sys.argv[1])	
	data = f.get_data_in_two_lists() 
	x = float(sys.argv[2])		

	print(newton_interpolation(data[0],data[1],x))	
