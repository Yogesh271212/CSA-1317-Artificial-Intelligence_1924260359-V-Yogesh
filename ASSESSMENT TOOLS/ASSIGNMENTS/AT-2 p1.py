import heapq

def get_valid_neighbors(grid, current):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        x, y = current[0] + dx, current[1] + dy
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
            neighbors.append((x, y))
    return neighbors

def a_star_search(grid, start, goal):
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal: 
            break
            
        for next_node in get_valid_neighbors(grid, current):
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + abs(next_node[0]-goal[0]) + abs(next_node[1]-goal[1])
                heapq.heappush(frontier, (priority, next_node))
                came_from[next_node] = current
                
    return came_from, cost_so_far

grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]

start_node = (0, 0)
goal_node = (2, 3)

came_from, cost_so_far = a_star_search(grid, start_node, goal_node)

if goal_node in came_from:
    path = []
    current = goal_node
    while current != start_node:
        path.append(current)
        current = came_from[current]
    path.append(start_node)
    path.reverse()

    print(f"Optimal Path: {path}")
    print(f"Total Cost: {cost_so_far[goal_node]}")
