from collections import deque


def solve_puzzle(Board, Source, Destination):
    visited = []
    # Priority queue start with empty 'path' list and 'direction' string
    pq = deque([([Source], '')])  # Add starting location to queue

    size_row, size_col = len(Board) - 1, len(Board[0]) - 1
    end_row, end_col = Destination[0], Destination[1]

    while len(pq) > 0:
        curr = pq.popleft()
        visited.append(curr[0][-1])

        path = curr[0]
        row = path[-1][0]
        col = path[-1][1]
        direction = curr[1]

        relative_to_end = (row - end_row, col - end_col)
        if relative_to_end == (0, 0):
            return curr

        # Check/P-Queue UP, RIGHT, LEFT, DOWN of a cell
        if row - 1 >= 0:  # UP
            if (row - 1, col) not in visited:
                if Board[row - 1][col] == '-':
                    if relative_to_end[0] > 0:  # compare rows
                        # is positive, then up is optimal path
                        pq.appendleft((path + [(row - 1, col)], direction + 'U'))
                    else:
                        # is 0 or negative, then up is non-optimal path
                        pq.append((path + [(row - 1, col)], direction + 'U'))
                else:  # if == '#'
                    visited.append((row - 1, col))

        if col - 1 >= 0:  # LEFT
            if (row, col - 1) not in visited:
                if Board[row][col - 1] == '-':
                    if relative_to_end[1] > 0:  # compare columns
                        # is positive, then left is optimal path
                        pq.appendleft((path + [(row, col - 1)], direction + 'L'))
                    else:
                        # is 0 or negative, then left is non-optimal path
                        pq.append((path + [(row, col - 1)], direction + 'L'))
                else:  # if == '#'
                    visited.append((row, col - 1))

        if row + 1 <= size_row:  # DOWN
            if (row + 1, col) not in visited:
                if Board[row + 1][col] == '-':
                    if 0 > relative_to_end[0]:  # compare rows
                        # is negative, then down is optimal path
                        pq.appendleft((path + [(row + 1, col)], direction + 'D'))
                    else:
                        # is 0 or positive, then down is non-optimal path
                        pq.append((path + [(row + 1, col)], direction + 'D'))
                else:  # if == '#'
                    visited.append((row + 1, col))

        if col + 1 <= size_col:  # RIGHT
            if (row, col + 1) not in visited:
                if Board[row][col + 1] == '-':
                    if 0 > relative_to_end[1]:  # compare columns
                        # is negative, then right is optimal path
                        pq.appendleft((path + [(row, col + 1)], direction + 'R'))
                    else:
                        # is 0 or positive, then right is non-optimal path
                        pq.append((path + [(row, col + 1)], direction + 'R'))
                else:  # if == '#'
                    visited.append((row, col + 1))

    return None

