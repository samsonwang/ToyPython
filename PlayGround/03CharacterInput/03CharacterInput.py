
'''
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
import sys
from datetime import date

date_today = date.today()
num_this_year = date_today.year
print("today is %s, this year is %d"
	  % (date_today.isoformat(), num_this_year))

str_name = input("what is your name? ")
str_age = input("how old are you? ")
try:
	num_age = int(str_age)
except ValueError:
	print("please input a number")
	sys.exit()
	
if num_age<1 or num_age>100 :
	print("please input a valid age")
	sys.exit()
	
num_year_delta = 100 - num_age
num_target_year = num_year_delta + num_this_year

print("Hi %s, you will be 100 years old in %d" % (str_name, num_target_year) )
