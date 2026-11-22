import random

rng = random.Random(42)
X = [[rng.gauss(0, 1) for _ in range(4)] for _ in range(500)]
y = [1 if r[0] + r[1] + rng.gauss(0, 0.3) > 1.0 else 0 for r in X]
X_tr, X_te, y_tr, y_te = X[:400], X[400:], y[:400], y[400:]

trees = [(f, th) for f in range(4) for th in [-0.5, 0.0, 0.5, 1.0, 1.5] for _ in range(5)]
valid = [t for t in trees if sum((r[t[0]] > t[1]) == yt for r, yt in zip(X_tr, y_tr)) > 270]

def eval_rf(data):
    probs = [sum(r[f] > th for f, th in valid) / len(valid) for r in data]
    preds = [int(p >= 0.35) for p in probs]
    tp = sum(p == 1 and yt == 1 for p, yt in zip(preds, y_te))
    fp = sum(p == 1 and yt == 0 for p, yt in zip(preds, y_te))
    fn = sum(p == 0 and yt == 1 for p, yt in zip(preds, y_te))
    tn = sum(p == 0 and yt == 0 for p, yt in zip(preds, y_te))
    acc, pre, rec = (tp + tn) / 100, tp / (tp + fp), tp / (tp + fn)
    pos, neg = [pr for pr, yt in zip(probs, y_te) if yt == 1], [pr for pr, yt in zip(probs, y_te) if yt == 0]
    auc = sum((p1 > p0) + 0.5 * (p1 == p0) for p1 in pos for p0 in neg) / (len(pos) * len(neg))
    return acc, pre, rec, 2 * pre * rec / (pre + rec), auc, [[tn, fp], [fn, tp]]

acc, pre, rec, f1, auc, cm = eval_rf(X_te)
print(f"Full Model -> Acc:{acc:.4f} P:{pre:.4f} R:{rec:.4f} F1:{f1:.4f} AUC:{auc:.4f}")
print("Confusion Matrix:", cm)
print(f"Counterexamples Found -> False Negatives: {cm[1][0]}, False Positives: {cm[0][1]}")
print(f"Under Sensor Noise (sigma=1.5) -> F1 drops to: {eval_rf([[v + rng.gauss(0, 1.5) for v in r] for r in X_te])[3]:.4f}")
