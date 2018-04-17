
'''
the number is odd or even
'''

#from

while True :
	str_input = input("please input a number: ")
	try:
		num_input = int(str_input)
		break
	except ValueError:
		print("please input a valid number")

num_ret = num_input % 2

if num_ret == 0 :
	print(num_input, "is an even number")
else :
	print(num_input, "is an odd number")



