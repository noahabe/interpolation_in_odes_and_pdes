'''
assumes that the Inital-Value Problem (IVP) is given by
	y' = f(x,y) , y(x_0) = y_0
and we want to evaluate the unknown function y(x) at r
for any r > x_0.
'''


def euler_s_method(f,h:float,x0:float,y0:float,x:float,debug_mode:bool=False)->float:
	'''
	we want to evaluate the unknown function y(x) at x.
	we know that y(x0) = y0. (the inital condition)
	'''
	while abs(x0-x) >= 10e-6 and x0 <= x:
		x0,y0 = x0+h,y0+h*f(x0,y0)
		if debug_mode: 
			print(x0,y0) #for debugging purposes only
	return y0


