% Experiment 4: Forward Chaining in Prolog
% Rules:
%   1. If a person studies, then the person gains knowledge.
%   2. If a person gains knowledge, then the person passes the examination.
% Initial Fact:
%   Ravi studies.
% Goal:
%   Prove that Ravi passes the examination.

:- dynamic fact/1.

% --- Initial Known Fact ---
fact(studies(ravi)).

% --- Production Rules ---
% rule(Condition, Conclusion)
rule(studies(X), gains_knowledge(X)).
rule(gains_knowledge(X), passes_examination(X)).

% --- Forward Chaining Inference Engine ---
forward_chain :-
    rule(Condition, Conclusion),
    fact(Condition),
    \+ fact(Conclusion),
    assertz(fact(Conclusion)),
    write('Derived new fact: '), write(Conclusion), nl,
    forward_chain.

forward_chain :-
    write('Forward chaining complete. No more new facts can be derived.'), nl.

% --- Proof Verification Predicate ---
prove(Goal) :-
    write('Starting Forward Chaining...'), nl,
    forward_chain,
    ( fact(Goal) ->
        write('PROVED: '), write(Goal), nl
    ;
        write('NOT PROVED: '), write(Goal), nl
    ).
