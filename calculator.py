#https://github.com/ryannew02/lab10-RJ-MB.git
#Partner 1: Ryan Juergens
#Partner 2: Marcel Bossa
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example

def square_root(a):
	try:
		return math.sqrt(a)
	except:
		raise ValueError

def hypotenuse(a, b):
	return math.hypot(a, b)

def div(a, b):
	if a == 0:
		raise ZeroDivisionError
	else:
		return b / a

def logarithm(a, b):
	if a <= 1 or b <= 0:
		raise ValueError
	return math.log(b, a)

def exp(a, b):
	return a ** b

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def mul(a,b):
    return a * b





