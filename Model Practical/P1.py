import heapq

def greedy_best_first_search(graph, heuristics, start, goal):
    pq = [(heuristics[start], start, [start])]
    visited = set()

    while pq:
        h, current, path = heapq.heappop(pq)

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor, weight in graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristics = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

path = greedy_best_first_search(graph, heuristics, 'A', 'G')
print("Path found:", " -> ".join(path) if path else "No path found")
