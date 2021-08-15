import numpy as np
import data_reader
import sys

def newton_interpolation(x_values:list,y_values:list,x:float):
	nor = len(x_values) #nor - number of rows
	#DT - Difference Table
	DT = np.empty((nor,nor),dtype=np.float64)
	for i in range(0,nor):
		DT[i,i] = y_values[i]
	for m in range(1,nor):
		for j in range(0,nor-m):
			DT[j,j+m] = (DT[j+1,j+m] - DT[j,j+m-1])/(x_values[j+m]-x_values[j])
			
	print(DT)

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
	
	
	
