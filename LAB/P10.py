import heapq

def a_star(graph, heuristics, start, goal):
    open_list = [(heuristics[start], 0, start, [start])]
    visited = set()
    
    while open_list:
        f_score, g_score, current, path = heapq.heappop(open_list)
        
        if current == goal:
            return path, g_score
            
        if current in visited:
            continue
            
        visited.add(current)
        
        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                new_g_score = g_score + cost
                new_f_score = new_g_score + heuristics[neighbor]
                heapq.heappush(open_list, (new_f_score, new_g_score, neighbor, path + [neighbor]))
                
    return None, float('inf')

graph = {
    'S': {'A': 1, 'B': 4},
    'A': {'B': 2, 'C': 5, 'G': 12},
    'B': {'C': 2},
    'C': {'G': 3},
    'G': {}
}

heuristics = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'G': 0
}

path, cost = a_star(graph, heuristics, 'S', 'G')
print(f"A* Path: {' -> '.join(path)}")
print(f"Total Cost: {cost}")
