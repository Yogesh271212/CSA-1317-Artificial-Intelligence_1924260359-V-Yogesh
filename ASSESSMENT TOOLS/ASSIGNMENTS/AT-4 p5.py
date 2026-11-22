import math

X = [[2, 1, 0], [1, 2, 0], [0, 1, 2], [0, 2, 1]]
y = [0, 0, 1, 1]
t = [1, 0, 2]

for a in [1e-9, 0.1, 1.0, 10.0]:
    p = {}
    for c in [0, 1]:
        r = [X[i] for i in range(4) if y[i] == c]
        cnt = [sum(col) for col in zip(*r)]
        tot = sum(cnt) + a * 3
        p[c] = math.log(len(r) / 4) + sum(t[j] * math.log((cnt[j] + a) / tot) for j in range(3))
    m = max(p.values())
    e = {c: math.exp(p[c] - m) for c in [0, 1]}
    print(f"alpha={str(a):5s} ->", {c: round(e[c] / sum(e.values()), 4) for c in [0, 1]})
