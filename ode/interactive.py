from euler import euler_s_method
from rk4 import rk4

from math import exp
from math import sqrt

'''
example of valid functions

Example 1 of the book "A first course in differential equations 
with modeling applications by Dennis G. Zill Section 2.6"
f = lambda x,y:0.1*sqrt(y) + 0.4*x*x
f = lambda x,y:-2*x-y
'''


f = eval(input("enter the function in lambda notation: "))
r = float(input("evaluate the unknown function at: "))
inital_condition = eval(input("enter the inital condition in tuple notation i.e. (x0,y0): "))
h = float(input("enter the step-size: "))

###############[method_of_solving]##############
method_of_solving = input("enter the method of solving [euler|rk4]: ")
if method_of_solving == "euler":
	numerical_method = euler_s_method
elif method_of_solving == "rk4":
	numerical_method = rk4

###################[analytic_function]##########
analytic_function = input("enter the analytic solution to calculate the error[0 for none]: ")
if analytic_function == '0':
	analytic_result = None
else:
	analytic_function = eval(analytic_function)
	analytic_result = analytic_function(r)

####################[debug_mode]################
debug_mode = input("debug mode [T|F]: ")
if debug_mode.upper() == 'T':
	debug_mode = True
elif debug_mode.upper() == 'F':
	debug_mode = False
else:
	print("incorrect debug mode inserted")
	exit()
################################################


print("\n\n")
numerical_result = numerical_method(f,h,inital_condition[0],inital_condition[1],r,debug_mode)

print(f"numerical_result: {numerical_result}\n")
print(f"analytic_result:  {analytic_result}\n")
if analytic_result != None:
	print(f"error: {abs(numerical_result - analytic_result)}\n")

