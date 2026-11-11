import heapq

def uniform_cost_search(graph, start, goal):
    frontier = [(0, start, [start])]
    explored = set()
    nodes_expanded = 0
    
    while frontier:
        cost, current, path = heapq.heappop(frontier)
        nodes_expanded += 1
        
        if current == goal:
            return path, cost, nodes_expanded
            
        if current not in explored:
            explored.add(current)
            for neighbor, travel_time in graph[current].items():
                if neighbor not in explored:
                    heapq.heappush(frontier, (cost + travel_time, neighbor, path + [neighbor]))
                    
    return None

hospital_map = {
    'Pharmacy': {'Junction A': 2, 'Junction B': 5},
    'Junction A': {'Pharmacy': 2, 'Ward 1': 3, 'Lift Lobby': 1},
    'Junction B': {'Pharmacy': 5, 'Ward 2': 4},
    'Lift Lobby': {'Junction A': 1, 'Ward 3': 2},
    'Ward 1': {'Junction A': 3},
    'Ward 2': {'Junction B': 4},
    'Ward 3': {'Lift Lobby': 2}
}

result = uniform_cost_search(hospital_map, 'Pharmacy', 'Ward 3')

if result:
    path, cost, nodes_expanded = result
    print(f"Optimal Path: {path}")
    print(f"Total Cost: {cost}")
    print(f"Nodes Expanded: {nodes_expanded}")
