import heapq

def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = state[:]
            new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
            neighbors.append(new_state)

    return neighbors

def astar(start, goal):
    start = list(start)
    goal = list(goal)

    pq = [(heuristic(start, goal), 0, start, [start])]
    visited = {}

    while pq:
        f, g, state, path = heapq.heappop(pq)
        state_tuple = tuple(state)

        if state == goal:
            return path

        if state_tuple in visited and visited[state_tuple] <= g:
            continue

        visited[state_tuple] = g

        for neighbor in get_neighbors(state):
            new_g = g + 1
            neighbor_tuple = tuple(neighbor)

            if neighbor_tuple not in visited or new_g < visited[neighbor_tuple]:
                new_f = new_g + heuristic(neighbor, goal)
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))

    return None

def print_path(path):
    if path is None:
        print("No solution exists")
        return

    print("Number of moves:", len(path) - 1)

    for state in path:
        for i in range(0, 9, 3):
            print(state[i:i + 3])
        print()

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

path = astar(start, goal)
print_path(path)