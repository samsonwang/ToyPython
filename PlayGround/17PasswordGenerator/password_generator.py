
'''
password generator
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

from random import randint, choice, sample
import string

def random_num():
    return choice(string.digits)


def random_uppercase_letter():
    return choice(string.ascii_uppercase)


def random_lowercase_letter():
    return choice(string.ascii_lowercase)


def random_char():
    num_rand = randint(1, 3)
    switcher_func = {
        1: random_num,
        2: random_uppercase_letter,
        3: random_lowercase_letter
    }
    func = switcher_func.get(num_rand, lambda:"invalid switch")
    return func()


def generate_password2():
    str_population = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return "".join(sample(str_population, 20))


def generate_password1():
    num_password_len = 20
    str_password  = ""
    for i in range(num_password_len):
        str_password += random_char()
    return str_password


def main():
    print("password1: ", generate_password1())
    print("password2: ", generate_password2())


if __name__ == '__main__':
    main()


