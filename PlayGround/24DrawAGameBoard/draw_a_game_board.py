
'''
draw a game pad
Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
'''

def get_size_from_user_input():
    while True:
        try:
            str_size = input('What size do you want? ')
            num_size = int(str_size)
            return num_size;
        except ValueError:
            print("please input a valid size")

def print_horiz_line(num_size):
    print(" --- " * num_size)

def print_vert_line(num_size):
    print("|    " * (num_size + 1))

    
def draw_square_pattern(num_size):
    num_count = 0
    while num_count < num_size:
        print_horiz_line(num_size)
        print_vert_line(num_size)
        num_count += 1
    print_horiz_line(num_size)


def main():
    num_size = get_size_from_user_input()
    draw_square_pattern(num_size)

    
# another solution without iteration
def main2():
    a = '---'.join('    ')
    b = '   '.join('||||')
    print('\n'.join((a, b, a, b, a, b, a)))
    
    
if __name__ == '__main__':
    main()




