# Takes in 2D List representing the board and outputs it to the console as a sudoku board
def print_sudoku(board):
    if len(board) != 9:
        print("ERROR, Invalid board passed to print_sudoku")
    for row in range(9):
        if len(board[row]) != 9:
            print("ERROR, Invalid board passed to print_sudoku")
        if row % 3 == 0 and row != 0:
            print("---------------------")
        line = ""
        for col in range(9):
            if col % 3 == 0 and col != 0:
                line = line + "| "
            if board[row][col] is None:
                line = line + "* "
            else:
                line = line + str(board[row][col]) + " "
        print(line)


# Takes in 2D List representing the board and returns True if the problem is solved in a valid way
def check_sudoku(board):
    domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Check there are no empty cells
    for row in board:
        for col in row:
            if col not in domain:
                return False

    # Check rows for AllDiff
    for row in board:
        if len(row) != len(set(row)):
            return False

    # Check cols for AllDiff
    for i in range(9):
        col = [row[i] for row  in board]
        if len(col) != len(set(col)):
            return False

    # Check subsquare for AllDiff
    for i in range(3):
        for j in range(3):
            subsquare = [board[3*i][3*j],     board[3*i][3*j + 1],     board[3*i][3*j + 2],
                         board[3*i + 1][3*j], board[3*i + 1][3*j + 1], board[3*i + 1][3*j + 2],
                         board[3*i + 2][3*j], board[3*i + 2][3*j + 1], board[3*i + 2][3*j + 2]]
            if len(subsquare) != len(set(subsquare)):
                return False
    return True

# ------------------------------------------------------------------------------
# Takes in 2D List representing the board and fills in empty/None squares using AC3
def solve_sudoku(board):
    domain = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    arcs = []

    # initialize cells with domains
    for row in range(9):
        for col in range(9):
            if board[row][col] is None:
                board[row][col] = domain.copy()

    # initialize arcs
    for row in range(9):
        for col in range(9):
            # if cell has a domain of numbers
            if isinstance(board[row][col], set):
                # add all arcs for that row and column
                for i in range(9):
                    if i != col:
                        arcs.append(((row, col), (row, i)))
                    if i != row:
                        arcs.append(((row, col), (i, col)))
                # add all arcs for that subsquare
                for i in range(3):
                    for j in range(3):
                        x = row - row % 3 + i
                        y = col - col % 3 + j
                        if i != row % 3 and j != col % 3:
                            arcs.append(((row, col), (x, y)))

    # eliminate values from domains
    for row in range(9):
        for col in range(9):
            # if cell has a domain of numbers
            if isinstance(board[row][col], set):
                # eliminate values from domains
                for i in range(9):
                    if board[row][i] is not None and i != col:
                        board[row][col].discard(board[row][i])
                    if board[i][col] is not None and i != row:
                        board[row][col].discard(board[i][col])
                # eliminate values from subsquare
                for i in range(3):
                    for j in range(3):
                        x = row - row % 3 + i
                        y = col - col % 3 + j
                        if board[x][y] is not None and x != row and y != col:
                            board[row][col].discard(board[x][y])

    print("After Elimination")
    print_sudoku(board)
    return

    print("After AC3")
    # AC3
    while len(arcs) > 0:
        (x, y) = arcs.pop(0)

        for x_value in board[x[0]][x[1]].copy():
            for y_value in board[y[0]][y[1]].copy():
                if x_value == y_value:
                    board[x[0]][x[1]].remove(x_value)
                    if len(board[x[0]][x[1]]) == 1:
                        arcs.append(((x[0], x[1]), (x[0], x[1])))

    print("After AC3")
    print_sudoku(board)
    return
# ------------------------------------------------------------------------------

problem1 = [[None, None, 3   , None, 2   , None, 6   , None, None],
            [9   , None, None, 3   , None, 5   , None, None, 1   ],
            [None, None, 1   , 8   , None, 6   , 4   , None, None],
            [None, None, 8   , 1   , None, 2   , 9   , None, None],
            [7   , None, None, None, None, None, None, None, 8   ],
            [None, None, 6   , 7   , None, 8   , 2   , None, None],
            [None, None, 2   , 6   , None, 9   , 5   , None, None],
            [8   , None, None, 2   , None, 3   , None, None, 9   ],
            [None, None, 5   , None, 1   , None, 3   , None, None]]

problem2 = [[None, 1   , 3   , 4   , 2   , None, None, 8   , 6   ],
            [2   , None, 4   , 6   , None, None, None, None, None],
            [None, 8   , 7   , None, 1   , None, 3   , None, None],
            [None, None, None, None, 3   , None, 6   , None, None],
            [None, 6   , 2   , 5   , None, None, None, None, 3   ],
            [5   , None, None, 7   , 6   , 4   , None, 9   , 1   ],
            [7   , None, None, None, 4   , None, 8   , 1   , None],
            [None, 4   , None, 8   , None, None, None, 6   , None],
            [None, None, 1   , 2   , 5   , 6   , None, 3   , 7   ]]

problem3 = [[6   , None, None, None, None, 7   , None, 2   , None],
            [None, None, None, None, None, None, None, 1   , 5   ],
            [2   , 4   , 9   , None, 1   , None, None, None, 3   ],
            [4   , None, 5   , 8   , None, 1   , 3   , 9   , None],
            [3   , 8   , None, None, 4   , 9   , None, None, None],
            [None, 1   , 6   , None, 7   , None, None, None, None],
            [8   , None, 4   , 1   , 5   , 3   , 6   , None, 2   ],
            [None, None, None, None, 6   , 4   , 8   , 3   , None],
            [1   , 6   , None, None, None, 2   , None, None, 9   ]]

print('-' * 80)
print("Example 1")
print("Initial State")
print_sudoku(problem1)
solve_sudoku(problem1)
print("Solved: " + str(check_sudoku(problem1)))
print("Final State")
print_sudoku(problem1)
print("")

"""
print('-' * 80)
print("Example 2")
print("Initial State")
print_sudoku(problem2)
solve_sudoku(problem2)
print("Solved: " + str(check_sudoku(problem2)))
print("Final State")
print_sudoku(problem2)
print("")

print('-' * 80)
print("Example 3")
print("Initial State")
print_sudoku(problem3)
solve_sudoku(problem3)
print("Solved: " + str(check_sudoku(problem3)))
print("Final State")
print_sudoku(problem3)
print("")
"""
