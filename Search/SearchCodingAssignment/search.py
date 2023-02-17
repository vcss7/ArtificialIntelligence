# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

def is_solved(puzzle):
    """
    Checks if a puzzle is in the solved state:
        1 2 3
        4 5 6
        7 8 0

    Arguments:
    - puzzle: Node object to check

    Return:
    is_solved: boolean of whethe the puzzle is solved or not
    """
    if puzzle[0][0] != 1 and puzzle[0][1] != 2 and puzzle[0][2] != 3:
        return false
    if puzzle[1][0] != 4 and puzzle[1][1] != 5 and puzzle[1][2] != 6:
        return false
    if puzzle[2][0] != 7 and puzzle[2][1] != 8 and puzzle[2][2] != 0:
        return false


def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    # TODO: WRITE CODE

    return final_solution


def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    # TODO: WRITE CODE

    return final_solution


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    # TODO: WRITE CODE

    return final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

    # TODO: WRITE CODE

    return final_solution
