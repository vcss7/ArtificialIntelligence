# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# solved state of puzzle
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def format_puzzle(puzzle):
    """
    Takes a list of list of strings with whitespace as a delimiter and returns
    a list of list of integers.

    Arguments:
        puzzle: Node object represeting initial state of the puzzle
    
    Return:
        formatted_puzzle: A list of list of integers representing the puzzle.
    """
    formatted_puzzle = []

    for row in puzzle:
        formatted_row = []
        for tile in row:
            formatted_row.append(int(tile))
        formatted_puzzle.append(formatted_row)

    return formatted_puzzle


def shift_tile(puzzle, up=0, left=0, down=0, right=0):
    """
    Takes a puzzle and shifts the tile in the specified direction.
    When a direction value is one, the tile is shifted in that direction.
    Only one direction value can be one at a time.

    Arguments:
        puzzle: Node object representing initial state of the puzzle
        up: True if tile should be shifted up, False otherwise
        left: True if tile should be shifted left, False otherwise
        down: True if tile should be shifted down, False otherwise
        right: True if tile should be shifted right, False otherwise

    Return:
        True if tile was shifted, False otherwise
    """

    max_row = len(puzzle) - 1
    max_col = len(puzzle[0]) - 1

    if up + left + down + right == 1:

        # find location of the zero tile
        for row in ranger(max_row + 1):
            for col in range(max_col + 1):
                if puzzle[row][col] == 0:
                    zero_row = row
                    zero_col = col
        
        # shift tile 
        if up and zero_row < max_row:
            puzzle[zero_row][zero_col] = puzzle[zero_row + 1][zero_col]
            puzzle[zero_row + 1][zero_col] = 0
            return True
        elif left and zero_col < max_col:
            puzzle[zero_row][zero_col] = puzzle[zero_row][zero_col + 1]
            puzzle[zero_row][zero_col + 1] = 0
            return True
        elif down and zero_row > 0:
            puzzle[zero_row][zero_col] = puzzle[zero_row - 1][zero_col]
            puzzle[zero_row - 1][zero_col] = 0
            return True
        elif right and zero_col > 0:
            puzzle[zero_row][zero_col] = puzzle[zero_row][zero_col - 1]
            puzzle[zero_row][zero_col - 1] = 0
            return True

    return False


def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """

    formatted_puzzle = format_puzzle(puzzle)

    final_solution = []

    return final_solution


def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    return final_solution


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """

    def find_num_tiles_misplaced(puzzle):
        pass

    final_solution = []

    return final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """

    def find_manhattan_distance(puzzle):
        pass

    final_solution = []

    return final_solution
