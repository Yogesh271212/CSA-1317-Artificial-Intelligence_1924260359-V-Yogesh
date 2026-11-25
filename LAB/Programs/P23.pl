% P23: Dieting System based on Disease

% Facts: diet(Disease, RecommendedDiet)
diet(diabetes, 'Low sugar, high fiber foods, whole grains, and leafy greens').
diet(hypertension, 'Low sodium diet, potassium-rich fruits, and vegetables').
diet(anemia, 'Iron-rich foods like spinach, lentils, red meat, and vitamin C').
diet(obesity, 'Calorie-controlled diet, lean proteins, fruits, and regular hydration').
diet(gastritis, 'Bland foods, non-citrus fruits, oatmeal, and avoiding spicy or fried items').
diet(heart_disease, 'Low saturated fat, omega-3 rich fish, nuts, and whole grains').

% Rule to suggest diet
suggest_diet(Disease) :-
    diet(Disease, Plan), !,
    write('Recommended diet for '), write(Disease), write(': '), nl,
    write(Plan), nl.
suggest_diet(Disease) :-
    write('No diet plan found for '), write(Disease), write('.'), nl.

% Sample Queries:
% ?- suggest_diet(diabetes).
% ?- suggest_diet(hypertension).
% ?- diet(anemia, Plan).
