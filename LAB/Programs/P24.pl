% P24: Monkey Banana Problem

% State representation: state(MonkeyPos, MonkeyStatus, BoxPos, HasBanana)

% Action 1: Grasp the banana
move(state(middle, onbox, middle, hasnot),
     grasp,
     state(middle, onbox, middle, has)).

% Action 2: Climb onto the box
move(state(P, onfloor, P, H),
     climb,
     state(P, onbox, P, H)).

% Action 3: Push the box from P1 to P2
move(state(P1, onfloor, P1, H),
     push(P1, P2),
     state(P2, onfloor, P2, H)).

% Action 4: Walk from P1 to P2
move(state(P1, onfloor, B, H),
     walk(P1, P2),
     state(P2, onfloor, B, H)).

% Goal state
canget(state(_, _, _, has), []).

% Recursive search collecting the sequence of moves
canget(State1, [Move | RestMoves]) :-
    move(State1, Move, State2),
    canget(State2, RestMoves).

% Helper predicate to run and print the solution
solve_monkey :-
    canget(state(atdoor, onfloor, atwindow, hasnot), Moves),
    write('Solution steps: '), write(Moves), nl.

% Sample Queries:
% ?- solve_monkey.
% ?- canget(state(atdoor, onfloor, atwindow, hasnot), Moves).
