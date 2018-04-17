
'''
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Extras:
Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# 假定链表是有序的
list_ret = []

for element in list_a :
	if element in list_b :
		list_ret.append(element)

print(list_ret)



