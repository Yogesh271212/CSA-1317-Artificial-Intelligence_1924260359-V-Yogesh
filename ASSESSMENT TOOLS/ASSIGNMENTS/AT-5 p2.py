rules = [
    ("R4", {"high_temp", "low_flow"}, "DryRun", 4),
    ("R15", {"high_temp", "low_flow", "high_vibration"}, "BearingWear", 1)
]

def diag(f, s="specificity"):
    m = [r for r in rules if r[1] <= f]
    c = max(m, key=lambda r: (len(r[1]), r[3]) if s == "specificity" else r[3], default=None)
    return (c[2], f"Fired {c[0]}") if c else (None, "No rule matched.")

cf = {"high_temp", "low_flow", "high_vibration"}
print("Conflict (Specificity):", diag(cf))
print("Conflict (Priority):", diag(cf, "priority"))
print("Missing Evidence:", diag({"high_temp"}))

rules.append(("R16", cf | {"low_pressure"}, "ImpellerJam", 5))
print("Runtime Rule Added (New Case):", diag(cf | {"low_pressure"}))
print("Regression Check (Old Case):", diag({"high_temp", "low_flow"}))
