'''
assumes that the Inital-Value Problem (IVP) is given by
	y' = f(x,y) , y(x_0) = y_0
implements rk4 - (the 4th order Runge-Kutta method) 
as described in Applied Numerical Analysis Equation number (6.13)
'''

def rk4(f,h:float,x0:float,y0:float,x:float,debug_mode:bool=False)->float:
	'''
	we want to evaluate the unknown function y(x) at x.
	we know that y(x0) = y0. (the inital condition)
	'''
	while abs(x0-x) >= 10e-6 and x0 <= x:
		k1 = h*f(x0,y0)
		k2 = h*f(x0+0.5*h,y0+0.5*k1)
		k3 = h*f(x0+0.5*h,y0+0.5*k2)
		k4 = h*f(x0+h,y0+k3)
		y0 += (1/6)*(k1 + 2*k2 + 2*k3 + k4)
		if debug_mode:
			print(x0,y0)
		x0 += h
	return y0
