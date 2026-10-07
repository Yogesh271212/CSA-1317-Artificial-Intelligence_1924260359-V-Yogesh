def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col]:
            return False
            
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
            
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False
            
    return True

def solve_n_queens_util(board, row, n, solutions):
    if row >= n:
        solutions.append([list(r) for r in board])
        return
        
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n, solutions)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens_util(board, 0, n, solutions)
    
    print(f"\nTotal valid configurations found for {n}x{n} board: {len(solutions)}")
    if solutions:
        show = input("Would you like to see the first solution? (y/n): ").strip().lower()
        if show == 'y':
            print("First valid solution:")
            print_board(solutions[0])

if __name__ == "__main__":
    print("--- N-Queens Solver ---")
    try:
        n = int(input("Enter the board size (N) for N-Queens (e.g., 8): "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            solve_n_queens(n)
    except ValueError:
        print("Invalid input. Please enter a number.")
