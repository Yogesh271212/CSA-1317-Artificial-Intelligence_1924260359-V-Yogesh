import heapq

class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def get_blank_pos(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = get_blank_pos(state.board)
    directions = [('Up', -1, 0), ('Down', 1, 0), ('Left', 0, -1), ('Right', 0, 1)]
    
    for move, dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [list(row) for row in state.board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append((tuple(tuple(row) for row in new_board), move))
    return neighbors

def manhattan_distance(board, goal):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = board[i][j]
            if val != 0:
                gx, gy = next((r, c) for r, row in enumerate(goal) for c, v in enumerate(row) if v == val)
                dist += abs(i - gx) + abs(j - gy)
    return dist

def solve_8_puzzle(start, goal):
    start_tuple = tuple(tuple(row) for row in start)
    goal_tuple = tuple(tuple(row) for row in goal)
    
    pq = []
    start_state = PuzzleState(start_tuple, None, None, 0, manhattan_distance(start_tuple, goal_tuple))
    heapq.heappush(pq, start_state)
    visited = set()
    
    while pq:
        current = heapq.heappop(pq)
        
        if current.board == goal_tuple:
            path = []
            while current:
                if current.move:
                    path.append(current.move)
                current = current.parent
            return path[::-1]
        
        visited.add(current.board)
        
        for next_board, move in get_neighbors(current):
            if next_board not in visited:
                cost = current.depth + 1 + manhattan_distance(next_board, goal_tuple)
                new_state = PuzzleState(next_board, current, move, current.depth + 1, cost)
                heapq.heappush(pq, new_state)
    return None

def get_board_input(name):
    print(f"\nEnter the {name} state row by row (use 0 for blank, separate numbers by space):")
    board = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        board.append(row)
    return board

if __name__ == "__main__":
    print("--- 8-Puzzle Solver ---")
    start_state = get_board_input("START")
    goal_state = get_board_input("GOAL")
    
    print("\nSolving...")
    solution = solve_8_puzzle(start_state, goal_state)
    
    if solution is not None:
        print(f"Solution found in {len(solution)} steps!")
        print(f"Steps: {solution}")
    else:
        print("No solution exists for this configuration.")
