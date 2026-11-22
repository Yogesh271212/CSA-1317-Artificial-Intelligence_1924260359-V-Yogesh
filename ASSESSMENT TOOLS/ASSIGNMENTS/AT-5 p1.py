def run(s, g, obs, bat, sud=None):
    p, o, log = s, set(obs), []
    for st in range(1, 13):
        if p == g: break
        if sud and st == sud[0]: o.add(sud[1])
        if bat <= sum(map(abs, p)) + 2:
            return log + [f"Step {st}: Pos={p}, Bat={bat}, Layer=Reactive, Act=EMERGENCY_LAND"]
        dx, dy = (g[0] > p[0]) - (g[0] < p[0]), (g[1] > p[1]) - (g[1] < p[1])
        nxt = (p[0] + dx, p[1]) if dx else (p[0], p[1] + dy)
        if nxt in o:
            safe = [c for c in [(p[0], p[1]+1), (p[0]+1, p[1]), (p[0], p[1]-1), (p[0]-1, p[1])] if c not in o and min(c) >= 0]
            if not safe: return log + [f"Step {st}: Pos={p}, Bat={bat}, Layer=Reactive, Act=HOVER_BLOCKED"]
            p, bat, act = safe[0], bat - 1, "Layer=Reactive, Act=AVOID_OBSTACLE"
        else:
            p, bat, act = nxt, bat - 1, "Layer=Deliberative, Act=MOVE_GOAL"
        log.append(f"Step {st}: Pos={p}, Bat={bat}, {act}")
    return log + [f"Done at {p}, Bat={bat}, Reached={p == g}"]

print("Scenario 1 (Normal):", run((0,0), (2,1), [], 10)[-1])
print("Scenario 2 (Sudden Obstacle):\n ", "\n  ".join(run((0,0), (3,0), [], 9, (2, (2,0)))))
print("Scenario 3 (Low Battery):", run((0,0), (4,4), [], 3)[-1])
