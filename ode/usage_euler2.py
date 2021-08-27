from euler import euler_s_method
from math import exp

f = lambda x,y:-2*x-y

r = float(input("evaluate the unknown function at: "))

numerical_result = euler_s_method(f,0.002,0.0,-1.0,r)
analytic_result = -3*exp(-r)-2*r+2

print(f"numerical_result: {numerical_result}\n")
print(f"analytic_result:  {analytic_result}\n")
print(f"error: {abs(numerical_result - analytic_result)}\n")

