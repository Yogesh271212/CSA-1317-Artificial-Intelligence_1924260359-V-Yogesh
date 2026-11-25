% Experiment 3: Animal Classification System using Facts and Rules
% Classifies animals as mammal, bird, reptile, and aquatic_animal

% --- Facts: Characteristics of Animals ---
has_fur(dog).
has_fur(cat).
has_fur(lion).

gives_birth(dog).
gives_birth(cat).
gives_birth(lion).

has_feathers(sparrow).
has_feathers(eagle).
has_feathers(penguin).

has_scales(snake).
has_scales(crocodile).
has_scales(lizard).

lays_eggs(sparrow).
lays_eggs(eagle).
lays_eggs(penguin).
lays_eggs(snake).
lays_eggs(crocodile).
lays_eggs(lizard).

warm_blooded(dog).
warm_blooded(cat).
warm_blooded(lion).
warm_blooded(sparrow).
warm_blooded(eagle).
warm_blooded(penguin).

cold_blooded(snake).
cold_blooded(crocodile).
cold_blooded(lizard).

lives_in_water(shark).
lives_in_water(goldfish).
lives_in_water(octopus).

has_gills(shark).
has_gills(goldfish).
has_gills(octopus).

can_swim(shark).
can_swim(goldfish).
can_swim(octopus).

% --- Classification Rules ---
mammal(X) :-
    has_fur(X),
    gives_birth(X),
    warm_blooded(X).

bird(X) :-
    has_feathers(X),
    lays_eggs(X),
    warm_blooded(X).

reptile(X) :-
    has_scales(X),
    lays_eggs(X),
    cold_blooded(X).

aquatic_animal(X) :-
    lives_in_water(X),
    has_gills(X),
    can_swim(X).

% --- General Classification Predicate ---
classify(X, mammal) :- mammal(X).
classify(X, bird) :- bird(X).
classify(X, reptile) :- reptile(X).
classify(X, aquatic_animal) :- aquatic_animal(X).
