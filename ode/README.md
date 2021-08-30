assume the inital value problem is give by:- 

##############################
#	dy		     #
#	-- = f(x,y)	     #
#	dx		     #
#			     #
#	y(x0) = y0	     #
##############################

Then `interactive.py` asks you the following questions:-

enter the function in lambda notation: - the right hand side of
the differential equation, that is f(x,y) in lambda notation
example: lambda x,y:-2*x-y

evaluate the unknown function at: - the point you want to evaluate
the unkown function at 
example: 3.2 
 
enter the inital condition in tuple notation i.e. (x0,y0): - 
example: (0,-1)
 
enter the step-size: - 
example: 0.1

enter the method of solving [euler|rk4]: - 
example: euler 

enter the analytic solution to calculate the error[0 for none]: - 
you enter the analytic solution of the initial value problem. example
for the above IVP the solution is: lambda x:-3*exp(-x)-2*x+2 

debug mode [T|F]: - lists each of the intermediary (xn,yn) values if 
debug mode is true.
