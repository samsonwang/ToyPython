
'''
Divisors
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

from sys import *

str_input = input("please input a number: ")

try:
	num_input = int(str_input)
except ValueError:
	print("please input a valid number")
	exit()
	
if num_input==0 :
	print("0 is not a proper divisor")

print("divisors:")
for i in range(1, 11, 1) :
	print(i * num_input)

	

