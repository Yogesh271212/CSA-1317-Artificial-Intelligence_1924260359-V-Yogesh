% P29: Backward Chaining

% Base known facts
known(has_fur).
known(gives_milk).
known(eats_meat).
known(has_tawny_color).
known(has_black_stripes).

% Rules: if(Goal, ConditionsList)
if(is_mammal, [has_fur, gives_milk]).
if(is_carnivore, [eats_meat]).
if(is_tiger, [is_mammal, is_carnivore, has_tawny_color, has_black_stripes]).

% Backward chaining inference engine
prove(Goal) :-
    known(Goal), !.

prove(Goal) :-
    if(Goal, Conditions),
    prove_all(Conditions).

prove_all([]).
prove_all([H | T]) :-
    prove(H),
    prove_all(T).

% Helper predicate for readable output
query_goal(Goal) :-
    prove(Goal), !,
    write('Goal proven: '), write(Goal), nl.
query_goal(Goal) :-
    write('Goal cannot be proven: '), write(Goal), nl.

% Sample Queries:
% ?- query_goal(is_tiger).
% ?- query_goal(is_mammal).
% ?- prove(is_tiger).
