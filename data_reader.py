import os

class InterpolationData:
	''''
	the file should include the interpolation data in the following format
		x_1,y_1
		x_2,y_2
		  ... 
	example:
		3.2,22.0
		2.7,17.8
		1.0,14.2
		4.8,38.3
		5.6,51.7
	'''

	def __init__(self,name_of_file=None):
		self.name_of_file = name_of_file

	def set_name_of_file(self,name_of_file):
		self.name_of_file = name_of_file

	def validity(self)->bool:
		'''
		checks the validity of the file existing or not
		'''
		return self.name_of_file != None and\
			os.path.exists(self.name_of_file)
 
	def get_data_in_two_lists(self):
		'''
		returns a list containing two lists. the first list contains
		the x values and the second list contains the y values.
		example (continuing from the data given in the class docstring)

		[[3.2, 2.7, 1.0, 4.8, 5.6], [22.0, 17.8, 14.2, 38.3, 51.7]]		
		'''

		if not self.validity():
			raise TypeError("Trying to open up a None file or file doesn't exist.")
		f = open(self.name_of_file,'r')
		retval = [[],[]]
		for line in f:
			try:
				line = line.strip().split(',')
				retval[0].append(float(line[0]))
				retval[1].append(float(line[1]))
			except:
				pass
		f.close()
		return retval

	def get_data_in_pairs(self):
		'''
		for the example given in the class docstring:-
		[(3.2, 22.0), (2.7, 17.8), (1.0, 14.2), (4.8, 38.3), (5.6, 51.7)]
		'''

		if not self.validity():
			raise TypeError("Trying to open up a None file or file doesn't exist.")
		f = open(self.name_of_file,'r')
		retval = []
		for line in f:
			line = line.strip().split(',')
			try:
				retval.append( (float(line[0]),float(line[1])) )
			except:
				pass
		f.close()
		return retval
