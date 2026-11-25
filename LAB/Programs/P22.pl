% P22: Family Tree

% Gender facts
male(john).
male(peter).
male(david).
male(alex).

female(mary).
female(susan).
female(lisa).
female(emma).

% Parent facts: parent(Parent, Child)
parent(john, peter).
parent(mary, peter).
parent(john, susan).
parent(mary, susan).
parent(peter, david).
parent(lisa, david).
parent(peter, emma).
parent(lisa, emma).
parent(susan, alex).

% Relationship rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).

sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).

grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandfather(X, Z) :- male(X), grandparent(X, Z).
grandmother(X, Z) :- female(X), grandparent(X, Z).

% Sample Queries:
% ?- father(john, peter).
% ?- sibling(peter, susan).
% ?- grandparent(john, david).
% ?- mother(M, emma).
