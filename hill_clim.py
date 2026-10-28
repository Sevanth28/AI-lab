import random

def heuristic(board, n):
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def hill_climbing(n):
    board = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        current_h = heuristic(board, n)

        if current_h == 0:
            return board

        best_board = board[:]
        best_h = current_h

        for col in range(n):
            for row in range(n):
                if board[col] != row:
                    new_board = board[:]
                    new_board[col] = row
                    h = heuristic(new_board, n)

                    if h < best_h:
                        best_h = h
                        best_board = new_board

        if best_h >= current_h:
            return None

        board = best_board

def print_board(board, n):
    for row in range(n):
        for col in range(n):
            print("Q" if board[col] == row else ".", end=" ")
        print()

n = int(input("Enter number of queens: "))
solution = hill_climbing(n)

if solution:
    print("Solution found:")
    print_board(solution, n)
    print("Conflicts:", heuristic(solution, n))
else:
    print("Local minimum reached. No solution found.")