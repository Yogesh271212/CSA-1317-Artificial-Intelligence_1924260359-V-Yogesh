% P25: Fruit and its Color using Backtracking

% Facts: fruit_color(Fruit, Color)
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(grape, green).
fruit_color(orange, orange).
fruit_color(strawberry, red).
fruit_color(lemon, yellow).
fruit_color(watermelon, green).

% Print all fruit-color pairs using backtracking
list_all_fruits :-
    fruit_color(Fruit, Color),
    write(Fruit), write(' is '), write(Color), nl,
    fail.
list_all_fruits.

% Find all fruits of a specific color using backtracking
find_by_color(Color) :-
    fruit_color(Fruit, Color),
    write(Fruit), nl,
    fail.
find_by_color(_).

% Sample Queries:
% ?- list_all_fruits.
% ?- find_by_color(red).
% ?- fruit_color(Fruit, Color).   % Press ';' to backtrack through all results
