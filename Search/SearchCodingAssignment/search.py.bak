import time
from collections import deque
from queue import PriorityQueue
from copy import deepcopy

# ENUMS
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


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
    start_time = time.time()

    # keep track of the nodes we have and have not explored
    unexplored_nodes = deque([(puzzle, [])])
    explored_nodes = []
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    while unexplored_nodes:
        node, path = unexplored_nodes.popleft()

        if node == goal_state:
            end_time = time.time()
            print(end_time - start_time)
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

    end_time = time.time()
    print(end_time - start_time)
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
    while i < 20 and unexplored_nodes:
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
        
        i += 1

    return final_solution


def get_num_misplaced(puzzle):
    num_misplaced = 0

    for row in range(len(puzzle)):
         for col in range(len(puzzle[row])):
             p = row * 3 + col + 1
             if puzzle[row][col] != p:
                 num_misplaced += 1

    return num_misplaced


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """
    final_solution = []

     # keep track of the nodes we have and have not explored
    unexplored_nodes = PriorityQueue()
    unexplored_nodes.put((get_num_misplaced(puzzle), puzzle, []))

    explored_nodes = []
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    while unexplored_nodes:
        man, node, path = unexplored_nodes.get()

        if node == goal_state:
            return path

        explored_nodes.append(node)

        # add UP to queue
        temp1 = deepcopy(node)
        if move_up(temp1):
            if temp1 not in explored_nodes:
                unexplored_nodes.put((get_num_misplaced(temp1), temp1, path + [0]))

        # add LEFT to queue
        temp2 = deepcopy(node)
        if move_left(temp2):
            if temp2 not in explored_nodes:
                unexplored_nodes.put((get_num_misplaced(temp2), temp2, path + [1]))

        # add DOWN to queue
        temp3 = deepcopy(node)
        if move_down(temp3):
            if temp3 not in explored_nodes:
                unexplored_nodes.put((get_num_misplaced(temp3), temp3, path + [2]))

        # add RIGHT to queue
        temp4 = deepcopy(node)
        if move_right(temp4):
            if temp4 not in explored_nodes:
                unexplored_nodes.put((get_num_misplaced(temp4), temp4, path + [3]))

    return []


def manhattan_dist(puzzle):
    man_dist = 0

    for row in range(len(puzzle)):
         for col in range(len(puzzle[row])):
             num = puzzle[row][col]
             if num == 0:
                 man_dist += (2 - row) + (2 - col)
             else:
                 target_row = (num - 1) // 3
                 target_col = (num - 1) % 3
                 man_dist += abs(row - target_row) + abs(col - target_col)

    return man_dist


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    final_solution: An ordered list of moves representing the final solution.
    """

    final_solution = []

     # keep track of the nodes we have and have not explored
    unexplored_nodes = PriorityQueue()
    unexplored_nodes.put((manhattan_dist(puzzle), puzzle, []))

    explored_nodes = []
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    while unexplored_nodes:
        man, node, path = unexplored_nodes.get()

        if node == goal_state:
            return path

        explored_nodes.append(node)

        # add UP to queue
        temp1 = deepcopy(node)
        if move_up(temp1):
            if temp1 not in explored_nodes:
                unexplored_nodes.put((manhattan_dist(temp1), temp1, path + [0]))

        # add LEFT to queue
        temp2 = deepcopy(node)
        if move_left(temp2):
            if temp2 not in explored_nodes:
                unexplored_nodes.put((manhattan_dist(temp2), temp2, path + [1]))

        # add DOWN to queue
        temp3 = deepcopy(node)
        if move_down(temp3):
            if temp3 not in explored_nodes:
                unexplored_nodes.put((manhattan_dist(temp3), temp3, path + [2]))

        # add RIGHT to queue
        temp4 = deepcopy(node)
        if move_right(temp4):
            if temp4 not in explored_nodes:
                unexplored_nodes.put((manhattan_dist(temp4), temp4, path + [3]))

    return []
