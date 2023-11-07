'''
puzzle game
https://github.com/NazarDizhak/dizhak-nazar-lab8-task2.git
'''
def rows_check(board:str) -> bool:
    '''checking rows for duplicate elements
    >>> board = ["**** ****",\
                 "***1 ****",\
                 "**  3****",\
                 "* 4 1****",\
                 "     9 5 ",\
                 " 6  83  *",\
                 "3   1  **",\
                 "  8  2***",\
                 "  2  ****"]

    >>> rows_check(board)
    True
    '''
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
    '''checking columns for duplicate elements
    >>> board = ["**** ****",\
                 "***1 ****",\
                 "**  3****",\
                 "* 4 1****",\
                 "     9 5 ",\
                 " 6  83  *",\
                 "3   1  **",\
                 "  8  2***",\
                 "  2  ****"]

    >>> columns_check(board)
    False
    '''
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
    '''checking colors for duplicate elements
    >>> board = ["**** ****",\
                 "***1 ****",\
                 "**  3****",\
                 "* 4 1****",\
                 "     9 5 ",\
                 " 6  83  *",\
                 "3   1  **",\
                 "  8  2***",\
                 "  2  ****"]

    >>> colors_check(board)
    True
    '''
    colors = []
    for i in range(5):
        temp_1 = [(board[8-i][i+j]) for j in range(4)]
        temp_2 = [(board[8-i-j][i]) for j in range(4)]
        colors.append(temp_1)
        colors[-1].extend(temp_2)
    res = any(colors[_].count(x) > 1 for _ in range(5) for x in colors[_] if x.isdigit())
    return not res

def validate_board(board:str) -> bool:
    '''taking all() from previous functions to validate a board
    >>> board = ["**** ****",\
                 "***1 ****",\
                 "**  3****",\
                 "* 4 1****",\
                 "     9 5 ",\
                 " 6  83  *",\
                 "3   1  **",\
                 "  8  2***",\
                 "  2  ****"]

    >>> validate_board(board)
    False
    '''
    res_rows = rows_check(board)
    res_columns = columns_check(board)
    res_colors = colors_check(board)

    return all([res_rows, res_columns, res_colors])


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
