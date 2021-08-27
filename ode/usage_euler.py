from euler import euler_s_method
from math import sqrt

'''
Example 1 of the book "A first course in differential equations 
with modeling applications by Dennis G. Zill Section 2.6"
'''

f = lambda x,y:0.1*sqrt(y) + 0.4*x*x
print(euler_s_method(f,0.1,2,4,2.5))
print("\n")
print(euler_s_method(f,0.05,2,4,2.5))
