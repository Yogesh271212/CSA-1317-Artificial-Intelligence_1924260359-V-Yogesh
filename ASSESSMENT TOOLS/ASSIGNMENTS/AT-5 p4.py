import time, random, math

intents = {
    "open_alerts": "which alerts are currently open active alarms",
    "explain_flag": "why was this packet flagged intrusion reason",
    "block_ip": "block source ip address firewall rule",
    "system_status": "show edge device cpu memory health status",
    "model_metrics": "what is current accuracy f1 latency score",
    "recent_logs": "list recent traffic logs last hour",
    "false_positive": "mark alert as false positive safe traffic",
    "export_report": "export daily incident summary report csv"
}

docs = [v.split() for v in intents.values()]
vocab = sorted(set(w for d in docs for w in d))
idf = {w: math.log((1 + len(docs)) / (1 + sum(w in d for d in docs))) + 1 for w in vocab}

def tfidf(words):
    v = [words.count(w) * idf.get(w, 0) for w in vocab]
    n = math.hypot(*v) or 1.0
    return [x / n for x in v]

mat, labels = [tfidf(d) for d in docs], list(intents)

def classify(q, th=0.45):
    v = tfidf(q.split())
    sims = [sum(a * b for a, b in zip(v, row)) for row in mat]
    i = max(range(len(sims)), key=sims.__getitem__)
    return (labels[i], round(sims[i], 3)) if sims[i] >= th else ("OUT_OF_SCOPE", round(sims[i], 3))

t0 = time.perf_counter()
print("Q1:", classify("which alerts are open right now"))
print("Q2:", classify("why was this flagged"))
print("Q3 (OOS):", classify("order pizza for dinner"))
print(f"Avg Response Latency: {(time.perf_counter()-t0)*1000/3:.3f} ms")

tests = [("which alerts are open", "open_alerts"), ("why was this flagged", "explain_flag"),
         ("block source ip address", "block_ip"), ("show edge health status", "system_status")]
oos = ["order pizza tonight", "play music loud", "book flight ticket"]
for wer in [0.0, 0.1, 0.2, 0.3]:
    ok = sum(classify(" ".join("err" if random.Random(s).random() < wer else w for w in q.split()))[0] == lbl for s in range(25) for q, lbl in tests)
    fa = sum(classify(q)[0] != "OUT_OF_SCOPE" for q in oos) / 3
    print(f"WER={int(wer*100):2d}% -> Intent Acc: {ok / 100:.2f} | OOS False-Accept: {fa:.2f}")
