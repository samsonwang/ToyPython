

def guess_word(word):
    word = word.lower()
    letters = list(word)
    guess = ['_' for i in letters]

#    print('letters: ', letters)
#    print('guess: ', guess)

    while guess.count('_') > 0:
        print(' '.join(guess))
        l = input('Guess your letter: ')
        if l in letters:
            for i in range(len(letters)):
                if letters[i] == l:
                    guess[i] = l
#            print(' '.join(guess))
        else:
            print('Incorrect')

    print('\nBingo!', word)


def main():
    guess_word('EVAPORATE')
    pass

if __name__ == "__main__":
    main()
