% P27: Medical Diagnosis System

% Patient symptoms: symptom(Patient, Symptom)
symptom(john, fever).
symptom(john, cough).
symptom(john, body_ache).

symptom(alice, sneezing).
symptom(alice, runny_nose).
symptom(alice, sore_throat).

symptom(bob, fever).
symptom(bob, rash).
symptom(bob, red_eyes).

symptom(emma, headache).
symptom(emma, nausea).
symptom(emma, sensitivity_to_light).

% Diagnostic rules
disease(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, body_ache).

disease(Patient, common_cold) :-
    symptom(Patient, sneezing),
    symptom(Patient, runny_nose),
    symptom(Patient, sore_throat).

disease(Patient, measles) :-
    symptom(Patient, fever),
    symptom(Patient, rash),
    symptom(Patient, red_eyes).

disease(Patient, migraine) :-
    symptom(Patient, headache),
    symptom(Patient, nausea),
    symptom(Patient, sensitivity_to_light).

% Helper predicate
diagnose(Patient) :-
    disease(Patient, Disease), !,
    write(Patient), write(' is diagnosed with '), write(Disease), write('.'), nl.
diagnose(Patient) :-
    write('Unable to diagnose '), write(Patient), write(' based on current symptoms.'), nl.

% Sample Queries:
% ?- diagnose(john).
% ?- diagnose(alice).
% ?- disease(bob, D).
