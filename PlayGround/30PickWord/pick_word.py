
import random

__wordlist = []

def load_file():
    with open('sowpods.txt', 'r') as f:
        line = f.readline()
        while line:
            __wordlist.append(line)
            line = f.readline()
    print("word list count:", len(__wordlist))


def rand_word():
    word = random.choice(__wordlist)
    print("random word:", word)


def main():
    load_file()
    rand_word()

if __name__ == "__main__":
#    print("__name__:", __name__)
    main()
