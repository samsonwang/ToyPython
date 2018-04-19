
'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

def remove_dup(list_dup):
    list_nodup = []
    for elem in list_dup:
        if elem not in list_nodup:
            list_nodup.append(elem)
    print(list_nodup)


def remove_dup1(list_dup):
    set_nodup = set(list_dup)
    print(set_nodup)
    list_nodup = list(set_nodup)
    print(list_nodup)


def main():
    list_1 = [1, 3, 4, 1, 4, 6]
    remove_dup1(list_1)


if __name__ == '__main__':
    main()


