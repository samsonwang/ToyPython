

'''
string list

Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''

def is_palindrome (str_param) :
	num_range = int(len(str_param) / 2)
	for i in range(1, num_range) :
		if str_param[i-1] != str_param[-i] :
			return False
	return True

# judge by reverse string
def is_palindrome2 (str_param) :
	str_reversed = str_param[::-1]
	return str_reversed == str_param
	
def main () :
	str_input = input("please input a string: ")
#	print("string :", str_input)
	if is_palindrome2 (str_input) :
		print("%s is palindrome" % str_input)
	else :
		print("%s is not a palindrome" % str_input)
	
if __name__ == '__main__' :
	main()

