import math, random

r = random.Random(42)
ys = list(range(10)) * 15
d = [([r.gauss(2*(j==y), .5) for j in range(10)], y) for y in ys]
r.shuffle(d); tr, te = d[:120], d[120:]
sig = lambda z: 1 / (1 + math.exp(-max(-20, min(20, z))))

def run(nm, H, lr):
    f = sig if nm=='sig' else lambda z: max(0, z)
    df = (lambda a: a*(1-a)) if nm=='sig' else (lambda a: a>0)
    W1 = [[r.uniform(-.2,.2) for _ in range(10)] for _ in range(H)]
    W2 = [[r.uniform(-.2,.2) for _ in range(H)] for _ in range(10)]
    for _ in range(25):
        for x, y in tr:
            h = [f(sum(a*b for a,b in zip(w, x))) for w in W1]
            o = [sig(sum(a*b for a,b in zip(w, h))) for w in W2]
            do = [(o[k]-(k==y))*o[k]*(1-o[k]) for k in range(10)]
            dh = [sum(W2[k][j]*do[k] for k in range(10))*df(h[j]) for j in range(H)]
            for k in range(10):
                for j in range(H): W2[k][j] -= lr * do[k] * h[j]
            for j in range(H):
                for i in range(10): W1[j][i] -= lr * dh[j] * x[i]
    ps = [max(range(10), key=lambda k: sum(W2[k][j]*f(sum(W1[j][i]*x[i] for i in range(10))) for j in range(H))) for x,_ in te]
    acc = sum(p==y for p,(_,y) in zip(ps,te)) / 30
    f1 = sum(2*sum(p==c==y for p,(_,y) in zip(ps,te))/max(1,sum((p==c)+(y==c) for p,(_,y) in zip(ps,te))) for c in range(10)) / 10
    print(f"{nm:4s} H={H:2d} LR={lr:<4} Acc={acc:.2f} F1={f1:.2f}")

for c in [('sig',8,.01),('relu',16,.1),('relu',32,.1),('sig',16,5.)]:
    run(*c)
