from collections import deque
from copy import deepcopy

# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
# TODO: make a class or struct to hold a num and its coordinates in the puzzle
#       add a swap function
#       add a check if correct coordinates for num
#       create a list of puzzle configurations visited

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
    solved_list = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            if puzzle[i][j] != solved_list[i][j]:
                return False
    return True

# if the empty space is in the first row, we cannot move down
# if the empty space is in the third row, we cannot move up
# if the empty space is in the first column, we cannot move right
# if the empty space is in the third column, we cannot move left

def move_up(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                if row == 2:
                    return False
                else:
                    puzzle[row][col] = puzzle[row + 1][col]
                    puzzle[row + 1][col] = 0
                    return True

def move_left(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                if col == 2:
                    return False
                else:
                    puzzle[row][col] = puzzle[row][col + 1]
                    puzzle[row][col + 1] = 0
                    return True



def move_down(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                if row == 0:
                    return False
                else:
                    puzzle[row][col] = puzzle[row - 1][col]
                    puzzle[row - 1][col] = 0
                    return True


def move_right(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                if col == 0:
                    return False
                else:
                    puzzle[row][col] = puzzle[row][col - 1]
                    puzzle[row][col - 1] = 0
                    return True


def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """
    # keep track of the nodes we have and have not explored
    unexplored_nodes = deque([(puzzle, [])])
    explored_nodes = []
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    while unexplored_nodes:
        node, path = unexplored_nodes.popleft()

        if node == goal_state:
            return path

        explored_nodes.append(node)

        # add UP to queue
        temp1 = deepcopy(node)
        if move_up(temp1):
            if temp1 not in explored_nodes:
                unexplored_nodes.append((temp1, path + [0]))

        # add LEFT to queue
        temp2 = deepcopy(node)
        if move_left(temp2):
            if temp2 not in explored_nodes:
                unexplored_nodes.append((temp2, path + [1]))

        # add DOWN to queue
        temp3 = deepcopy(node)
        if move_down(temp3):
            if temp3 not in explored_nodes:
                unexplored_nodes.append((temp3, path + [2]))

        # add RIGHT to queue
        temp4 = deepcopy(node)
        if move_right(temp4):
            if temp4 not in explored_nodes:
                unexplored_nodes.append((temp4, path + [3]))

    return []

def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """
    final_solution = []

    # keep track of the nodes we have and have not explored
    unexplored_nodes = [(puzzle, [])]
    explored_nodes = []
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    i = 0
    while unexplored_nodes:
        node, path = unexplored_nodes.pop()

        if node == goal_state:
            return path

        explored_nodes.append(node)

        # add RIGHT to queue
        temp4 = deepcopy(node)
        if move_right(temp4):
            if temp4 not in explored_nodes:
                unexplored_nodes.append((temp4, path + [3]))

        # add DOWN to queue
        temp3 = deepcopy(node)
        if move_down(temp3):
            if temp3 not in explored_nodes:
                unexplored_nodes.append((temp3, path + [2]))

        # add LEFT to queue
        temp2 = deepcopy(node)
        if move_left(temp2):
            if temp2 not in explored_nodes:
                unexplored_nodes.append((temp2, path + [1]))

        # add UP to queue
        temp1 = deepcopy(node)
        if move_up(temp1):
            if temp1 not in explored_nodes:
                unexplored_nodes.append((temp1, path + [0]))

        print(node)
        i += 1

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
