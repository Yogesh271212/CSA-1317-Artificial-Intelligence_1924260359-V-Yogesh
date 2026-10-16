def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
        print("DFS Traversal: ", end="")
        
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example Graph (same as above)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')
print()
