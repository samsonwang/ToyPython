
'''
element search

Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
Extras:
Use binary search.
'''

def element_search(num, ordered_list):
    if num in ordered_list:
        return True;
    else:
        return False

def main():
    list_num = [1, 3, 5, 6, 8, 9]
    if element_search(3, list_num):
        print("number is in list")
    else:
        print("number is not found in list")

if __name__ == '__main__':
    main()



