from collections import deque
from copy import deepcopy
from time import sleep
from queue import PriorityQueue

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


def shift_tile(puzzle, direction):
    """
    Takes a puzzle and shift a tile in the specified diection. If the tile
    cannot be shifted in the specified direction, the puzzle is not changed.

    Arguments:
        puzzle: Node object representing initial state of the puzzle
        direction: Integer representing the direction to shift the tile using
            the following ENUMS defined at the beginning of the this file

    Return:
        True if tile was shifted, False otherwise
    """
    max_row = len(puzzle) - 1
    max_col = len(puzzle[0]) - 1

    # find location of the zero tile
    for row in range(max_row + 1):
        for col in range(max_col + 1):
            if puzzle[row][col] == 0:
                zero_row = row
                zero_col = col
    
    # shift tile in specified direction
    if direction == UP and zero_row < max_row:
        puzzle[zero_row][zero_col] = puzzle[zero_row + 1][zero_col]
        puzzle[zero_row + 1][zero_col] = 0
        return True
    elif direction == LEFT and zero_col < max_col:
        puzzle[zero_row][zero_col] = puzzle[zero_row][zero_col + 1]
        puzzle[zero_row][zero_col + 1] = 0
        return True
    elif direction == DOWN and zero_row > 0:
        puzzle[zero_row][zero_col] = puzzle[zero_row - 1][zero_col]
        puzzle[zero_row - 1][zero_col] = 0
        return True
    elif direction == RIGHT and zero_col > 0:
        puzzle[zero_row][zero_col] = puzzle[zero_row][zero_col - 1]
        puzzle[zero_row][zero_col - 1] = 0
        return True

    return False


def BFS(puzzle):
    """
    Breadth-First Search.
    Store nodes to be expanded in a queue. Add children of the current node to
    the end of the queue and expand the first node in the queue. FIFO.

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """
    # initial state of the puzzle
    initial_node = format_puzzle(puzzle)

    # store nodes to be expanded and their path
    queue = []
    queue.append((initial_node, []))

    # list to store nodes that have been expanded
    expanded = []

    # list to store the path to the solution
    final_solution = []

    # while queue is not empty
    while queue:
        node, path = queue.pop(0)
        
        if node == GOAL_STATE:
            final_solution = path
            break

        if node not in expanded:
            # add node to expanded
            expanded.append(node)

            # add children of node to queue
            for direction in range(4):
                child = deepcopy(node)
                if shift_tile(child, direction):
                    queue.append((child, path + [direction]))

    return final_solution


def DFS(puzzle):
    """
    Depth-First Search.
    Store nodes to be expanded in a queue. Add children of the current node to
    the front of the queue and expand the first node in the queue. LIFO.

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """
    return []
    # initial state of the puzzle
    initial_node = format_puzzle(puzzle)
    
    # queue to store nodes to be expanded and their path
    queue = deque()
    queue.append((initial_node, []))
    
    # list to store nodes that have been expanded
    expanded = []

    # list to store the path to the solution
    final_solution = []

    # while queue is not empty
    while queue:
        node, path = queue.popleft()

        if node == GOAL_STATE:
            final_solution = path
            break

        if node not in expanded:
            # add node to expanded
            expanded.append(node)

            # add children of node to queue
            for direction in reversed(range(4)):
                child = deepcopy(node)
                if shift_tile(child, direction):
                    queue.insert(0, (child, path + [direction]))

    return final_solution


def A_Star_H1(puzzle):
    """
    A-Star with number of misplaced tiles as the heuristic function.

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """

    def find_num_tiles_misplaced(puzzle):
        """
        Finds the number of tiles that are misplaced in the puzzle.

        Arguments:
            puzzle: Node object representing a state of the puzzle

        Return:
            num_tiles_misplaced: the number of tiles that are misplaced.
        """
        num_tiles_misplaced = 0

        for row in range(len(puzzle)):
            for col in range(len(puzzle[0])):
                if puzzle[row][col] != GOAL_STATE[row][col]:
                    num_tiles_misplaced += 1

        return num_tiles_misplaced

    # initial state of the puzzle
    initial_node = format_puzzle(puzzle)

    # Priority Queue to store nodes to expand, their path, and their heuristic value
    queue = PriorityQueue()
    queue.put((find_num_tiles_misplaced(initial_node), (initial_node, [])))

    # list to store nodes that have been expanded
    expanded = []

    # list to store the path to the solution
    final_solution = []

    # while queue is not empty
    while queue:
        node, path = queue.get()[1]
        
        if node == GOAL_STATE:
            final_solution = path
            break

        if node not in expanded:
            # add node to expanded
            expanded.append(node)

            # add children of node to queue
            for direction in range(4):
                child = deepcopy(node)
                if shift_tile(child, direction):
                    queue.put((find_num_tiles_misplaced(child), (child, path + [direction])))

    return final_solution


def A_Star_H2(puzzle):
    """
    A-Star with manhattan distance as the heuristic function.

    Arguments:
        puzzle: Node object representing initial state of the puzzle

    Return:
        final_solution: An ordered list of moves representing the final solution.
    """

    def find_manhattan_distance(puzzle):
        """
        Finds the manhattan distance of each of the tiles in the puzzle.

        Arguments:
            puzzle: Node object representing a state of the puzzle

        Return:
            manhattan_distance: the sum of the manhattan distances of each tile.
        """
        manhattan_distance = 0

        for row in range(len(puzzle)):
            for col in range(len(puzzle[0])):
                if puzzle[row][col] != 0:
                    expected_row = (puzzle[row][col] - 1) // len(puzzle[0])
                    expected_col = (puzzle[row][col] - 1) % len(puzzle[0])
                    manhattan_distance += abs(expected_row - row) + abs(expected_col - col)

        return manhattan_distance

    # initial state of the puzzle
    initial_node = format_puzzle(puzzle)

    # Priority Queue to store nodes to expand, their path, and their heuristic value
    queue = PriorityQueue()
    queue.put((find_manhattan_distance(initial_node), (initial_node, [])))

    # list to store nodes that have been expanded
    expanded = []

    # list to store the path to the solution
    final_solution = []

    # while queue is not empty
    while queue:
        node, path = queue.get()[1]

        if node == GOAL_STATE:
            final_solution = path
            break

        if node not in expanded:
            # add node to expanded
            expanded.append(node)
            # add children of node to Queue
            for direction in range(4):
                child = deepcopy(node)
                if shift_tile(child, direction):
                    queue.put((find_manhattan_distance(child), (child, path + [direction])))

    return final_solution
