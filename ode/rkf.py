def rkf(f,h:float,x0:float,y0:float,x:float,debug_mode:bool=False)->float:
	'''
	implements the Runge-Kutta-Fehlberg Method as provided on
	Applied Numerical Analysis page 344
	
	* The stepsize h provided is the inital step size
	'''
	while abs(x0-x) >= 10e-6 and x0 <= x:
		k1 = h*f(x0,y0)
		k2 = h*f(x0+(h/4), y0+(k1/4))
		k3 = h*f(x0+(3/8)*h, y0+(3/32)*k1+(9/32)*k2)
		k4 = h*f(x0+(12/13)*h, y0+(1932/2197)*k1-(7200/2197)*k2+(7296/2197)*k3)	
		k5 = h*f(x0+h, y0+(439/216)*k1-8*k2+(3680/513)*k3-(845/4104)*k4)
		k6 = h*f(x0+(h/2),y0-(8/27)*k1+2*k2-(3544/2565)*k3+(1859/4104)*k4-(11/40)*k5)
		y_by_rk4 = y0 + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5
		y_by_rk5 = y0 + (16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5+(2/55)*k6
		if abs(y_by_rk4 - y_by_rk5) > 10e-8:
			h /= 2 
			continue
		if debug_mode:
			print(x0,y0)
		x0 += h
		y0 = y_by_rk5
	return y0
