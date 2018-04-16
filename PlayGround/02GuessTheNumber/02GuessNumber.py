

'''
Guess Number
auther: Samson Wang
data: 2018-04-16
'''


import random

num_min = 1
num_max = 100
num_target = random.randint(num_min, num_max)
# print("target:", num_target)

is_answer_correct = False

while not is_answer_correct :
	print("guess the number, range(%d~%d)" % (num_min, num_max))
	
	answer = input(" answer is: ")
	try:
		num_answer = int(answer)
	except ValueError:
		print(" please input a number")
		continue
		
	if num_answer == num_target :
		print(" answer is correct!!")
		is_answer_correct = True
	elif num_answer > num_target :
		print(" your answer is too big")
	else :
		print(" your answer is to small")

	print("")
	
		
	
