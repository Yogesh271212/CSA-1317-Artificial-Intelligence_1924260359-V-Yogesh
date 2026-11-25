% P20: Towers of Hanoi

hanoi(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source),
    write(' to '), write(Target), nl.

hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    M is N - 1,
    hanoi(M, Source, Auxiliary, Target),
    write('Move disk '), write(N),
    write(' from '), write(Source),
    write(' to '), write(Target), nl,
    hanoi(M, Auxiliary, Target, Source).

% Sample Query:
% ?- hanoi(3, left, right, center).
