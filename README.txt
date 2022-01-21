# optimalpath_maze
Implemented Python-based breadth-first search and priority queue techniques to find an optimal path between any two points of a rectangular maze represented as a list of lists


For result, append the following code:

puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

print(solve_puzzle(puzzle, (0, 2), (2, 2)))
print(solve_puzzle(puzzle, (0, 0), (4, 4)))
