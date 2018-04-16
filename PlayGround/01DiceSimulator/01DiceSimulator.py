
'''
dice simulator
author: Samson Wang
data: 2018-04-16
'''

import random

# 最大最小值
num_min = 1
num_max = 6

is_need_exit = False

while not is_need_exit :
	print("==dice simulator==")
	print("dice is rolling!\n min=%d, max=%d" % (num_min, num_max))
	num_rand = random.randint(num_min, num_max)
	print(" rand number", num_rand)

	# ask whether next roll is needed
	while True:
		answer = input("roll dice again? (y/n): ")
		if (answer == "n") :
			is_need_exit = True
			break;
		elif (answer == "y") :
			is_need_exit = False
			break;
		else :
			print("please input \"y\" or \"n\" !!")
		
	


