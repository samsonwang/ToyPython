
'''
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
'''

def fibonacci():
    num_1 = 1
    num_2 = 1
    list_fib = [num_1, num_2]
    i = 0
    while i < 10:
        list_fib.append(num_1 + num_2)
        num_1 = num_2
        num_2 = list_fib[-1]
        i = i + 1
    return list_fib


def main():
    print(fibonacci())


if __name__ == '__main__':
    main()

