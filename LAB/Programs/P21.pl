% P21: Bird Can Fly or Not

bird(sparrow).
bird(eagle).
bird(pigeon).
bird(penguin).
bird(ostrich).
bird(kiwi).

cannot_fly(penguin).
cannot_fly(ostrich).
cannot_fly(kiwi).

can_fly(X) :-
    bird(X),
    \+ cannot_fly(X).

check_flight(X) :-
    can_fly(X), !,
    write(X), write(' can fly.'), nl.
check_flight(X) :-
    bird(X), !,
    write(X), write(' cannot fly.'), nl.
check_flight(X) :-
    write(X), write(' is not in the bird database.'), nl.

% Sample Queries:
% ?- check_flight(sparrow).
% ?- check_flight(penguin).
% ?- can_fly(eagle).
% ?- can_fly(ostrich).
