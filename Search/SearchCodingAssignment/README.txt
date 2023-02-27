WARNING:
    The Depth-First Search algorithm does not have a depth limit and takes
    a long time to run (took about 10 minutes on my computer for example 2).

    I implemented tie-breaks based off the ENUMS provided in the code: UP,
    LEFT, DOWN, RIGHT. I understand the README says to break ties in the order
    UP, DOWN, LEFT, RIGHT, but it feels more natural to break ties based off
    the order of the ENUMS. I accept any points lost for this.

Files:
    README.txt
        This file, with information on how to run the code, requirements or
        dependencies, and answers to the comparison questions.

    search.py
        File of the 4 algorithms: BFS, DFS, A* with heuristic 1, and A* with 
        heuristic 2.

Software Requirements:
    python3
    python3 `deepcopy` module from `copy` library
    python3 `deque` module from `collection` library
    python3 `PriorityQueue` module from `queue` library
    python3 `time` library

Running:
    python3 main.py

Comparison Questions:
    Which algorithm performed the fastest?
        Short Answer:
            A-Star with H2
        Long Answer:
            Here is the times for each algorithm on each test file:
            test_data/ex1.txt:
                BFS             took 0.0003132820129394531 seconds
                DFS             took 8.034706115722656e-05 seconds
                A-Star with H1  took 0.00014019012451171875 seconds
                A-Star with H2  took 0.00011920928955078125 seconds
            test_data/ex1.txt:
                BFS             took 0.0039827823638916016 seconds
                DFS             took 643.7607798576355 seconds
                A-Star with H1  took 0.003318309783935547 seconds
                A-Star with H2  took 0.0002906322479248047 seconds
            test_data/ex3.txt:
                BFS             took 0.005118608474731445 seconds
                DFS             took 1.4567451477050781 seconds
                A-Star with H1  took 0.012156963348388672 seconds
                A-Star with H2  took 0.0002269744873046875 seconds
    Which algorithm used the most memory?
        Short Answer:
            By far Depth-First Search used the most memory. 
        Long Answer: 
            My first implementation of each algorithm was to store the path to
            each node in a list. It worked fine for all algorithms except DFS,
            which crashed my computer from all the paths it was storing. This
            forced me to store the tile shift that resulted in the current node
            and then backtrack to find the path. This was much more memory
            efficient and allowed me to run DFS without crashing my computer.
    Which algorithm gave the best solution?
        Short Answer:
            A-Star with H2 
        Long Answer:
            A-Star with H2 was the fastest to find the solution and gave the
            shortest path. BFS also gave the shortest path but took longer to
            find.

