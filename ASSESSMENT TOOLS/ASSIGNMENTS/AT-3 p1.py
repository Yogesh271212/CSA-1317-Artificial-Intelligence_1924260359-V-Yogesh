def get_symbols(sentences):
    return list(set(c for s in sentences for c in s if c.isupper()))

def pl_true(sentences, model):
    for s in sentences:
        for sym, val in model.items():
            s = s.replace(sym, str(val))
        s = s.replace('^', ' and ').replace('v', ' or ').replace('~', ' not ')
        if '=>' in s:
            l, r = s.split('=>')
            s = f"(not ({l})) or ({r})"
        if not eval(s):
            return False
    return True

def tt_entails(kb, alpha):
    symbols = get_symbols(kb + alpha)
    return tt_check_all(kb, alpha, symbols, {})

def tt_check_all(kb, alpha, symbols, model):
    if not symbols:
        if pl_true(kb, model):
            return pl_true(alpha, model)
        else:
            return True 
    P = symbols[0]
    rest = symbols[1:]
    return (tt_check_all(kb, alpha, rest, {**model, P: True}) and 
            tt_check_all(kb, alpha, rest, {**model, P: False}))

kb1 = ["P=>Q", "P"]
query1 = ["Q"]
print(f"KB: {kb1}, Query: {query1}")
print(f"Entails: {tt_entails(kb1, query1)}\n")

kb2 = ["P=>Q", "Q"]
query2 = ["P"]
print(f"KB: {kb2}, Query: {query2}")
print(f"Entails: {tt_entails(kb2, query2)}")
