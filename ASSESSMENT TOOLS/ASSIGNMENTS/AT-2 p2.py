tree = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G']}
scores = {'D': 3, 'E': 5, 'F': 2, 'G': 9}

def ab_pruning(node, alpha, beta, is_max):
    if node in scores: return scores[node]
    best = -float('inf') if is_max else float('inf')
    for child in tree.get(node, []):
        val = ab_pruning(child, alpha, beta, not is_max)
        best = max(best, val) if is_max else min(best, val)
        alpha, beta = (max(alpha, best), beta) if is_max else (alpha, min(beta, best))
        if beta <= alpha: break
    return best

print(f"Optimal value: {ab_pruning('A', -float('inf'), float('inf'), True)}")
