def unify(x, y, theta):
    if theta is None: return None
    if x == y: return theta
    if isinstance(x, str) and x.islower(): return unify_var(x, y, theta)
    if isinstance(y, str) and y.islower(): return unify_var(y, x, theta)
    if isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return theta if not x else unify(x[1:], y[1:], unify(x[0], y[0], theta))
    return None

def unify_var(v, x, theta):
    if v in theta: return unify(theta[v], x, theta)
    if x in theta: return unify(v, theta[x], theta)
    return {**theta, v: x} 

term1 = ['Knows', 'John', 'x']
term2 = ['Knows', 'John', 'Jane']
print(f"MGU: {unify(term1, term2, {})}")
