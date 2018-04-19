
'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def main():
    str_var = input("please input a number:")
    while True:
        try:
            num_var = int(str_var)
            break
        except ValueError:
            print("please input a number")

    if is_prime(num_var):
        print("%d is a prime" % num_var)
    else:
        print("%d is not a prime" % num_var)
        
if __name__ == "__main__":
    main()


