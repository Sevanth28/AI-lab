# ---------------------------------------
# GOAL STATE
# ---------------------------------------

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# ---------------------------------------
# GENERATE NEIGHBORS
# ---------------------------------------

def get_neighbors(state):
    neighbors = []

    # Find the position of blank (0)
    zero_pos = state.index(0)

    row = zero_pos // 3
    col = zero_pos % 3

    # Possible moves: Up, Down, Left, Right
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        # Check if the new position is inside the puzzle
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_pos = new_row * 3 + new_col

            # Convert tuple to list
            new_state = list(state)

            # Swap blank with the neighboring tile
            new_state[zero_pos], new_state[new_pos] = \
                new_state[new_pos], new_state[zero_pos]

            # Convert back to tuple
            neighbors.append(tuple(new_state))

    return neighbors


# ---------------------------------------
# DEPTH-LIMITED SEARCH
# ---------------------------------------

def depth_limited_search(state, depth, path):

    # Goal test
    if state == GOAL:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    # Explore neighbors
    for neighbor in get_neighbors(state):

        # Avoid states already present in current path
        if neighbor not in path:

            result = depth_limited_search(
                neighbor,
                depth - 1,
                path + [neighbor]
            )

            if result is not None:
                return result

    return None


# ---------------------------------------
# PRINT PUZZLE
# ---------------------------------------

def print_puzzle(state):

    for i in range(0, 9, 3):
        print(state[i:i + 3])

    print()


# ---------------------------------------
# ITERATIVE DEEPENING SEARCH
# ---------------------------------------

def ids(start):

    depth = 0

    while True:

        result = depth_limited_search(
            start,
            depth,
            [start]
        )

        if result is not None:
            return result

        depth += 1


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

start =  (1, 2, 3,
         0, 4, 6,
         7, 5, 8)


print("INITIAL STATE")
print_puzzle(start)

print("========== IDS ==========")

ids_solution = ids(start)

print("Number of moves:", len(ids_solution) - 1)

for i, state in enumerate(ids_solution):

    print("Step", i)
    print_puzzle(state)
