import itertools

def tsp(graph, start):
    nodes = list(graph.keys())
    nodes.remove(start)
    
    min_path_cost = float('inf')
    best_path = []

    for perm in itertools.permutations(nodes):
        current_cost = 0
        current_node = start

        for next_node in perm:
            current_cost += graph[current_node][next_node]
            current_node = next_node
            
        current_cost += graph[current_node][start]
        
        if current_cost < min_path_cost:
            min_path_cost = current_cost
            best_path = [start] + list(perm) + [start]
            
    return best_path, min_path_cost

tsp_graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

path, cost = tsp(tsp_graph, 'A')
print(f"Optimal TSP Path: {' -> '.join(path)}")
print(f"Minimum Cost: {cost}")
