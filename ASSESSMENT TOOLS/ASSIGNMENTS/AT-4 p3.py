import math, random

pdf = lambda x, m, v: (
    math.exp(-((x - m) ** 2) / (2 * max(v, 1e-6)))
    / math.sqrt(2 * math.pi * max(v, 1e-6))
)

def em(X, norm=True, it=5, sd=42):
    r = random.Random(sd)
    p, m, v = [.5]*2, [r.uniform(0, 3), r.uniform(8, 12)], [1.]*2
    lls = []
    for _ in range(it):
        g = [[p[k]*pdf(x, m[k], v[k]) for k in (0, 1)] for x in X]
        lls.append(round(sum(math.log(max(1e-12, sum(row))) for row in g), 3))
        if norm:
            g = [[val / max(1e-12, sum(row)) for val in row] for row in g]
        for k in (0, 1):
            Nk = max(1e-12, sum(row[k] for row in g))
            m[k] = sum(g[i][k] * X[i] for i in range(4)) / Nk
            v[k] = sum(g[i][k] * (X[i] - m[k])**2 for i in range(4)) / Nk
            p[k] = Nk / 4
    return sum(p), lls

X = [0., 1., 10., 11.]
print("Faulty:", em(X, False))
print("Fixed :", em(X, True))
mono = all(
    l[i] <= l[i+1] + 1e-6
    for s in range(20)
    for l in [em(X, True, 6, s)[1]]
    for i in range(5)
)
print("Mono:", mono)
