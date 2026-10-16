def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if colors.get(neighbor) == color:
            return False
    return True

def get_color(node, graph, available_colors, colors):
    for color in available_colors:
        if is_safe(node, color, graph, colors):
            return color
    return None

def map_coloring(graph, available_colors):
    colors = {}
    for node in graph:
        colors[node] = get_color(node, graph, available_colors, colors)
        if colors[node] is None:
            return "No solution exists."
    return colors

if __name__ == "__main__":
    graph = {
        'WA': ['NT', 'SA'], 'NT': ['WA', 'SA', 'Q'], 'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'], 'NSW': ['Q', 'SA', 'V'], 'V': ['SA', 'NSW']
    }
    available_colors = ['Red', 'Green', 'Blue']
    print("Map Coloring Solution:", map_coloring(graph, available_colors))
