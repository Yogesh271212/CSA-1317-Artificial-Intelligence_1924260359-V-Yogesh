% =============================================================================
% Sum of Integers from 1 to N
% =============================================================================

% Base case: sum from 1 to 0 is 0
sum_to_n(0, 0) :- !.

% Recursive case:
% For N > 0, compute Sum of (N - 1) as SubSum, then Sum is SubSum + N.
sum_to_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_to_n(N1, SubSum),
    Sum is SubSum + N.
