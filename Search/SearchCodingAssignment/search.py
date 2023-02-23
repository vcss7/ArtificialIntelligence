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
                return false
    return true


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

    # keep track of the nodes we have not explored
    unexplored_nodes = [puzzle]

    print(unexplored_nodes)
    puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    unexplored_nodes.append(puzzle)
    print(unexplored_nodes)

    # keep track of the nodes we have explored
    explored_nodes = []

    # in BFS we prioritize exploring the siblings of nodes over exploring their
    # children
    # we explore siblings in the order: UP, DOWN, LEFT, RIGHT

    # add UP, DOWN, LEFT, RIGHT nodes to unexplored_node list
    # go into UP, add its children to the queue
    # go into DOWN, add its children to the queue
    # go into LEFT, add its children to the queue
    # go into RIGHT, add its children to the queue

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
