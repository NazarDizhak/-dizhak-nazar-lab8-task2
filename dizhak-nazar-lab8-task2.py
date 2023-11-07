'''
puzzle game
https://github.com/NazarDizhak/dizhak-nazar-lab8-task2.git
'''
def rows_check(board:str) -> bool:
    '''checking rows for duplicate elements'''
    res = True
    for row in board:
        temp = []
        for elem in row:
            if elem.isdigit() and elem not in temp:
                temp.append(elem)
            elif elem in temp:
                res = False
    return res

def columns_check(board:str) -> bool:
    '''checking columns for duplicate elements'''
    res = True
    for col in range(9):
        temp = []
        for row in range(9):
            elem = board[row][col]
            if elem.isdigit() and elem not in temp:
                temp.append(elem)
            elif elem.isdigit() and elem in temp:
                res = False
    return res

def colors_check(board:str) -> bool:
    '''checking colors for duplicate elements'''
    pass

def validate_board(board:str) -> bool:
    '''taking all() from previous functions to validate a board'''
    pass

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
