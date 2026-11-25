% P28: Forward Chaining

:- dynamic fact/1.

% Initial known facts
fact(has_feathers).
fact(lays_eggs).
fact(swims).

% Forward chaining rules: rule(ConditionsList, Conclusion)
rule([has_feathers, lays_eggs], is_bird).
rule([is_bird, swims], is_penguin).
rule([is_penguin], cannot_fly).

% Check if all conditions in a list are currently known facts
all_true([]).
all_true([H | T]) :-
    fact(H),
    all_true(T).

% Forward chaining inference loop
forward_chain :-
    rule(Conditions, Conclusion),
    all_true(Conditions),
    \+ fact(Conclusion),
    assertz(fact(Conclusion)),
    write('Derived new fact: '), write(Conclusion), nl,
    forward_chain.
forward_chain :-
    write('Forward chaining complete. No more facts can be derived.'), nl.

% Sample Queries:
% ?- forward_chain.
% ?- fact(is_penguin).
% ?- fact(cannot_fly).
% ?- listing(fact).
