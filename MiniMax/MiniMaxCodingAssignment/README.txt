Files:
    README.txt
        This file contains information on how to run the code, any requirements
        or dependencies, and a brief description of the script.

    minimax.py
        File containing the implementation of the minimax algorithm with DFS.

Software Requirements:
    Python 3.x

Running:
    python3 minimax.py

What is the time and space complexity of the algorithm? why?
    Time complexity: O(b^m)
    Space complexity: O(m)

    Where b is the branching factor and m is the maximum depth of the search
    tree.

    The time complexity of the minimax algorithm with DFS is proportional to
    the number of nodes in the search tree, which is the branching factor
    raised to the power of the maximum depth of the tree. The space complexity
    is proportional to the maximum depth of the search tree, because the
    algorithm stores the state of the game at each level of the tree.
