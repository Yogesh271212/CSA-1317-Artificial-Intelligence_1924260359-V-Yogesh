import math, random
from collections import Counter

ent = lambda y: -sum(
    c/len(y) * math.log2(c/len(y))
    for c in Counter(y).values()
)
gain = lambda d, i: ent([r[-1] for r in d]) - sum(
    len(s)/len(d) * ent([r[-1] for r in s])
    for v in set(r[i] for r in d)
    for s in [[r for r in d if r[i] == v]]
)

toy = [
    'HDGP','HDBP','HMGP','HMBF',
    'LDGP','LDBF','LMGF','LMBF'
]
print([round(gain(toy, i), 4) for i in range(3)])

r = random.Random(42)
d = [
    ([r.gauss(1.5 if y else -1.5, 1)
      for _ in range(5)], y)
    for y in [r.randint(0, 1) for _ in range(100)]
]
tr, te = d[:80], d[80:]
f, t = min(
    (sum(y != (x[j] > x0[j]) for x, y in tr),
     j, x0[j])
    for j in range(5) for x0, _ in tr
)[1:]
tp, fp, tn, fn = [
    sum((x[f] > t) == a and y == b for x, y in te)
    for a, b in [(1,1), (1,0), (0,0), (0,1)]
]
print(f"Acc:{(tp+tn)/20:.2f} P:{tp/(tp+fp):.2f}")
print(f"R:{tp/(tp+fn):.2f} F1:{2*tp/(2*tp+fp+fn):.2f}")
print("CM:", [[tn, fp], [fn, tp]])
