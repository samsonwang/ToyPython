
'''
file overlap

Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

'''

def get_num_from_file(str_filename):
    set_num = set([])
    with open(str_filename, 'r') as file_opened:
        str_num = file_opened.readline()
        while str_num:
            try:
                num = int(str_num)
                set_num.add(num)
#            print("%s has %d" % (str_filename, num) )
            except ValueError:
                pass
            finally:
                str_num = file_opened.readline()
    return set_num


def main():
    set_num1 = get_num_from_file('primenumbers.txt')
    set_num2 = get_num_from_file('happynumbers.txt')
    print("set1:" , set_num1)
    print("set2:" , set_num2)
    print("set1 & set2:", set_num1 & set_num2)


if __name__ == '__main__':
    main()

