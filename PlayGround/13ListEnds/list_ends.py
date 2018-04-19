

'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''

def trans_list(list_num):
    if len(list_num) <= 0:
        return []
    list_ret = [list_num[0], list_num[-1]]
    return list_ret


def main():
    list_temp = [1, 2, 3]
    print(trans_list(list_temp))


if __name__ == '__main__':
    main()
    
