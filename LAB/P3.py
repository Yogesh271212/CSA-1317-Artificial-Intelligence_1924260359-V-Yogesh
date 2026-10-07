from collections import deque

def solve_water_jug(capacity_x, capacity_y, target):
    if target > max(capacity_x, capacity_y):
        return None  # Target cannot be larger than the largest jug

    start_state = (0, 0)
    queue = deque([(start_state, [])])
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        current_path = path + [(x, y)]
        
        if x == target or y == target:
            return current_path
            
        moves = [
            (capacity_x, y),  # Fill Jug X
            (x, capacity_y),  # Fill Jug Y
            (0, y),           # Empty Jug X
            (x, 0),           # Empty Jug Y
            (x - min(x, capacity_y - y), y + min(x, capacity_y - y)), # Pour X to Y
            (x + min(y, capacity_x - x), y - min(y, capacity_x - x))  # Pour Y to X
        ]
        
        for next_state in moves:
            if next_state not in visited:
                queue.append((next_state, current_path))
                
    return None

if __name__ == "__main__":
    print("--- Water Jug Solver ---")
    try:
        jug1 = int(input("Enter the capacity of Jug 1: "))
        jug2 = int(input("Enter the capacity of Jug 2: "))
        target = int(input("Enter the target amount to measure: "))
        
        solution = solve_water_jug(jug1, jug2, target)
        
        if solution:
            print(f"\nSteps to get exactly {target} units:")
            for step, state in enumerate(solution):
                print(f"Step {step}: Jug 1 = {state[0]} | Jug 2 = {state[1]}")
        else:
            print(f"\nNo solution exists to measure {target} using jugs of {jug1} and {jug2}.")
    except ValueError:
        print("Invalid input. Please enter integers only.")
