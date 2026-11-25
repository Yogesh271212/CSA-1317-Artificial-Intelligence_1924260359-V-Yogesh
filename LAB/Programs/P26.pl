% P26: Best First Search Algorithm

% Graph edges: edge(Node, Neighbor, Cost)
edge(a, b, 1).
edge(a, c, 3).
edge(b, d, 2).
edge(b, e, 5).
edge(c, f, 4).
edge(d, g, 3).
edge(e, g, 1).
edge(f, g, 2).

% Heuristic values: heuristic(Node, H)
heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 5).
heuristic(d, 2).
heuristic(e, 1).
heuristic(f, 2).
heuristic(g, 0).

% Entry point: best_first_search(Start, Goal, Path)
best_first_search(Start, Goal, Path) :-
    heuristic(Start, H),
    bfs([H-[Start]], Goal, RevPath),
    reverse(RevPath, Path).

% Base case: Goal reached
bfs([_-[Goal | Rest] | _], Goal, [Goal | Rest]) :- !.

% Recursive step: Expand node with lowest heuristic value
bfs([_-[Current | Rest] | Queue], Goal, Path) :-
    findall(H-[Next, Current | Rest],
            (edge(Current, Next, _),
             \+ member(Next, [Current | Rest]),
             heuristic(Next, H)),
            Children),
    append(Queue, Children, NewQueue),
    keysort(NewQueue, SortedQueue),
    bfs(SortedQueue, Goal, Path).

% Sample Query:
% ?- best_first_search(a, g, Path).
