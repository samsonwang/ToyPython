
'''
list overlap comprehension

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).
'''


import random as rand

def print_mutual_element(list_a, list_b):
    list_t1 = [num for num in list_a if num in list_b]
    list_ret = []
    for num in list_t1:
        if num not in list_ret:
            list_ret.append(num)
    print("list_a:", list_a)
    print("list_b:", list_b)
    print(list_ret)

def main():
    list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    list_1 = rand.sample(range(20), 10)
    list_2 = rand.sample(range(20), 10)
    print_mutual_element(list_1, list_2)
    
if __name__ == "__main__":
    main()



