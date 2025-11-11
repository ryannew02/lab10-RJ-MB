"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
import math

def square_root(a):
	try:
		return math.sqrt(a)
	except:
		raise ValueError

def hypotenuse(a, b):
	return math.hypot(a, b)

def log(a, b):
	if a <= 1 or b <= 0:
		raise ValueError
	return math.log(b, a)

def exp(a, b):
	return a ** b

def add(a, b): 
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b




