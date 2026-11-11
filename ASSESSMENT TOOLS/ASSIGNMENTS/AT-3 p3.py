def forward_chain(rules, facts, query):
    inferred = set()
    agenda = list(facts)
    
    while agenda:
        p = agenda.pop(0)
        if p == query: return True
        if p not in inferred:
            inferred.add(p)
            for premises, conclusion in rules:
                if p in premises and all(prem in inferred for prem in premises):
                    agenda.append(conclusion)
    return False
    
rules = [({'L', 'M'}, 'P'), ({'B', 'L'}, 'M'), ({'A', 'P'}, 'L'), ({'A', 'B'}, 'L')]
facts = ['A', 'B']

print(f"Entails 'P': {forward_chain(rules, facts, 'P')}")
print(f"Entails 'Q': {forward_chain(rules, facts, 'Q')}")
