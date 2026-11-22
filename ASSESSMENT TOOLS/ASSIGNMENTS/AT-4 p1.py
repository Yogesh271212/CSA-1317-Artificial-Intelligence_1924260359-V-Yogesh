import random

r = random.Random(42)
d = [([r.gauss(1.5 if y else -1.5, 1) for _ in range(10)], y) for y in [r.randint(0, 1) for _ in range(300)]]
r.shuffle(d)
tr, te = d[:240], d[240:]

fit = lambda d: min((sum(y != (x[f] > x0[f]) for x, y in d), f, x0[f]) for f in range(10) for x0, _ in d)[1:]
acc = lambda m, d: sum((x[m[0]] > m[1]) == y for x, y in d) / len(d)

m = fit(tr)
cv = sum(acc(fit([x for j, x in enumerate(tr) if j % 5 != k]), tr[k::5]) for k in range(5)) / 5
print(f"Train: {acc(m, tr):.4f} | CV: {cv:.4f} | Test: {acc(m, te):.4f}")
