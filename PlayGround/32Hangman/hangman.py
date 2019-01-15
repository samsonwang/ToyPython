

import random

def rand_word():
    wordlist = []
    with open('sowpods.txt', 'r') as f:
        line = f.readline()
        while line:
            wordlist.append(line)
            line = f.readline()
    print("word list count:", len(wordlist))

    word = random.choice(wordlist)
    print("random word:", word)

    return word.rstrip("\n\r")



def guess_word(word):
    word = word.lower()
    letters = list(word)
    guess = ['_' for i in letters]
    guess_count = 0
    guessed = set()

    print(letters)
    print(guess)

    while guess.count('_') > 0 and guess_count < 6:
        print(' ')
        print(' '.join(guess))
        l = input('Guess your letter(%d chances left): '
                  % (6-guess_count))
        if l in guessed:
            print('You have guessed:', l)
        elif l in letters:
            guessed.add(l)
            for i in range(len(letters)):
                if letters[i] == l:
                    guess[i] = l
        else:
            guessed.add(l)
            guess_count += 1
            print('Incorrect')

    if guess.count('_') == 0:
        print('\nBingo!', word)
    else:
        print('\nWhat a pity,', word)

def main():
    word = rand_word()
    guess_word(word)




if __name__ == '__main__':
    main()
