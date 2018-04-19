
'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

My name is Michele
Then I would see the string:

Michele is name My
shown back to me.
'''


def reverse_word_order(str_1):
    list_word = str_1.split(' ')
    num_size = len(list_word)
    str_new = ""
    for i in range(num_size-1, -1, -1):
        str_new = str_new + list_word[i] + " "
    return str_new


def reverse_word_order1(str_param):
    list_word = str_param.split(' ')
    str_new = ' '.join(reversed(list_word))
    return str_new


def main():
    str_1 = "hello world aaaa bbbbb"
    print(reverse_word_order1(str_1))


if __name__ == '__main__':
    main()



