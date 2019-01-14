
'''
given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
'''

import logging as log

log.basicConfig(level=log.DEBUG)

#暂时没有考虑数组越界的问题
# accept matrix holds in list of list
# returns player number, draw game returns 0
def horzontal_judge(list_data):
    for list_h in list_data:
        item_1 = list_h[0]
        bool_same = True
        for item in list_h:
            if item != item_1:
                bool_same = False
        if bool_same == True:
            log.debug("hor return: %d" % item_1)
            return item_1
    log.debug("hor return: 0")
    return 0

# matrix input
def vertical_judge(list_data):
    num_size = len(list_data)
    for num_i in range(0, num_size):
        item_1 = list_data[0][num_i]
        log.debug("ver item_1 [%d][%d]=%d" % (num_i, 0,  item_1))
        bool_same = True
        for num_j in range(0, num_size):
            log.debug("ver [%d][%d]=%d" % (num_j, num_i,  list_data[num_j][num_i]))
            if list_data[num_j][num_i] != item_1:
                bool_same = False
        if bool_same == True:
            log.debug("ver return: %d" % item_1)
            return item_1
    log.debug("ver return: 0")
    return 0


def diagonal_judge(list_data):
    num_size = len(list_data)
    item_1 = list_data[0][0]
    bool_same = True
    for num_i in range(0, num_size):
        if list_data[num_i][num_i] != item_1:
            bool_same = False
    if bool_same == True:
        log.debug("diagonal return: %d" % item_1)
        return item_1
    item_1 = list_data[num_size-1][0]
    bool_same = True
    for num_i in range(0, num_size):
        if list_data[num_i][num_size-1-num_i] != item_1:
            bool_same = False
    if bool_same == True:
        log.debug("diagonal return: %d" % item_1)
        return item_1
    log.debug("diagonal return: 0")
    return 0

def tic_tac_toe_judge(list_data):
    num_ret = vertical_judge(list_data)
    if num_ret == 0:
        num_ret = horzontal_judge(list_data)
        if num_ret == 0:
            return diagonal_judge(list_data)
        else:
            return num_ret
    else:
        return num_ret


def main():
    list_game1 = [[1, 2, 1],
                  [2, 1, 0],
	              [1, 2, 1]]

    num_ret = tic_tac_toe_judge(list_game1)
    print("winner is:" , num_ret)

if __name__ == '__main__':
    main()
