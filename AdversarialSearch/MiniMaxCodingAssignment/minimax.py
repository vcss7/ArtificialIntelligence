# enums for game states
GAME_INCOMPLETE = 0
GAME_DRAW = 1
GAME_X = 2
GAME_O = 3

X = 1
O = -1
EMPTY = 0


def evaluate_game(board):
    """
    This function tests if a specific player wins.

    Possibilities:
    Three rows    [X X X] or [O O O]
    Three cols    [X X X] or [O O O]
    Two diagonals [X X X] or [O O O]

    Arguments:
    - board: the state of the current board

    Return:
    - GAME_INCOMPLETE, GAME_DRAW, GAME_X, or GAME_O

    """
    win_states = [[board[0][0], board[0][1], board[0][2]],
                  [board[1][0], board[1][1], board[1][2]],
                  [board[2][0], board[2][1], board[2][2]],
                  [board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[2][0], board[1][1], board[0][2]]]

    if [X, X, X] in win_states:
        return GAME_X
    if [O, O, O] in win_states:
        return GAME_O
    for row in board:
        for i in row:
            if i == EMPTY:
                return GAME_INCOMPLETE
    return GAME_DRAW


def print_board(board):
    """
    This function print out the current board.

    Arguments:
    - board: the state of the current board

    """
    for row in range(len(board)):
        line = ""
        for col in range(len(board[row])):
            if board[row][col] == X:
                line = line + ' X '
            elif board[row][col] == O: 
                line = line + ' O '
            else:
                line = line + "   "
            if col < 2:
                line = line + "|"
        print(line)
        if row < 2:
            print("-----------")
        else:                   # temp delete later
            print("")           # temp delete later


def O_move(board):
    """
    This function plays the O player (The opponent).

    Presently I have made O simply return the first valid move I find
    If you like, you can make this function match your X function
    to watch two minimax agents duke it out
    But really, this can be defined to anything you want it to do for testing.
    I will only be testing "X_move"

    Arguments:
    - board: the state of the current board

    Return:
    - a tuple (i,j) with the row, col of O's chosen move
    """
    best_score = -100
    best_move = None

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                board[row][col] = X
                score = minimax_o(board, O, 0)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move
    print("ERROR! No Valid Move!")


def minimax_o(graph, node, depth):
    """
    This function is a helper function to the X_move function.
    It performs a depth first search on the game tree to find the best move
    while using the minimax algorithm to evaluate the score of each node.
    """
    # just returns 0 for now
    state = evaluate_game(graph)
    if state == GAME_X:
        return 10 - depth
    elif state == GAME_O:
        return -10 - depth
    elif state == GAME_DRAW:
        return 0 - depth
    else:
        if node == X:
            best_score = -100
            for row in range(len(graph)):
                for col in range(len(graph[row])):
                    if graph[row][col] == EMPTY:
                        graph[row][col] = X
                        score = minimax_o(graph, O, depth + 1)
                        graph[row][col] = EMPTY
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 100
            for row in range(len(graph)):
                for col in range(len(graph[row])):
                    if graph[row][col] == EMPTY:
                        graph[row][col] = O
                        score = minimax_o(graph, X, depth + 1)
                        graph[row][col] = EMPTY
                        if score < best_score:
                            best_score = score
            return best_score


def X_move(board):
    # TODO: Implement the Minimax Algorithm
    #      Given an input game state, find the best move for X with the minimax algorithm
    #      For scores, you can use +10 for an X win, -10 for a O win, and 0 for a Draw
    #      In addition, in order to motivate the agent to win or lose as soon as possible, 
    #      subtract the depth of completed game state from the score. For Example:
    #
    #      If the input state is: X |   | X
    #                               |   | O
    #                               | O | 
    #
    #      Some potential completed game states might have the scores:
    #
    #      X | O | X     X Win = 10
    #        | X | O  ->             -> Score = 7
    #        | O | X     Depth = 3
    #
    #      X | X | X     X Win = 10
    #        |   | O  ->             -> Score = 9
    #        | O |       Depth = 1
    #
    #      X | O | X     Draw  = 0
    #      O | X | O  ->             -> Score = -5
    #      O | O | X     Depth = 5
    #
    #      X | O | X     O Win = -10
    #      X | O | O  ->             -> Score = -15  -> This state is actually not possible, because X always goes first
    #      O | O | X     Depth = 5                      However, in the input state I used, its actually impossible for O to win, as far as I can tell...
    #
    """
    This function plays the X player (The agent).

    The agent uses the minimax algorithm to find the best move.
    It values a win as 10, a loss as -10, and a draw as 0.
    It values a win that occurs sooner at a higher value than a win that occurs later.
    For every move that goes deeper into the game, the score is reduced by 1.
    """
    best_score = -100
    best_move = None

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                board[row][col] = X
                score = minimax_x(board, O, 0)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move
    print("ERROR! No Valid Move!")


def minimax_x(graph, node, depth):
    """
    This function is a helper function to the X_move function.
    It performs a depth first search on the game tree to find the best move
    while using the minimax algorithm to evaluate the score of each node.
    """
    # just returns 0 for now
    state = evaluate_game(graph)
    if state == GAME_X:
        return 10 - depth
    elif state == GAME_O:
        return -10 - depth
    elif state == GAME_DRAW:
        return 0 - depth
    else:
        if node == X:
            best_score = -100
            for row in range(len(graph)):
                for col in range(len(graph[row])):
                    if graph[row][col] == EMPTY:
                        graph[row][col] = X
                        score = minimax_x(graph, O, depth + 1)
                        graph[row][col] = EMPTY
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 100
            for row in range(len(graph)):
                for col in range(len(graph[row])):
                    if graph[row][col] == EMPTY:
                        graph[row][col] = O
                        score = minimax_x(graph, X, depth + 1)
                        graph[row][col] = EMPTY
                        if score < best_score:
                            best_score = score
            return best_score


board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

game_winner = GAME_INCOMPLETE
# Game Loop
while game_winner == GAME_INCOMPLETE:
    i, j = X_move(board)
    board[i][j] = X
    print_board(board)
    game_winner = evaluate_game(board)
    if game_winner != GAME_INCOMPLETE:
        break
    i, j = O_move(board)
    board[i][j] = O
    print_board(board)
    game_winner = evaluate_game(board)

# Game is complete, announce winner
if game_winner == GAME_DRAW:
    print("Game was a Draw!")
elif game_winner == GAME_X:
    print("X Wins!")
else:
    print("O Wins!")
