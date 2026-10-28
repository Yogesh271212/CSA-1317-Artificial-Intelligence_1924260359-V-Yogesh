% =============================================================================
% Database with Name and Date of Birth (DOB)
% =============================================================================

% Facts: person(Name, dob(Day, Month, Year))
person('Arun Sharma', dob(15, 8, 1995)).
person('Priya Patel', dob(22, 11, 2001)).
person('Rahul Verma', dob(5, 3, 1998)).
person('Ananya Iyer', dob(15, 8, 2003)).
person('Vikram Singh', dob(30, 1, 1990)).

% Helper rule: Retrieve full DOB for a person
get_dob(Name, Day, Month, Year) :-
    person(Name, dob(Day, Month, Year)).

% Helper rule: Find people born in a specific year
born_in_year(Name, Year) :-
    person(Name, dob(_, _, Year)).

% Helper rule: Find people born in a specific month
born_in_month(Name, Month) :-
    person(Name, dob(_, Month, _)).

% Helper rule: Check if two people share the exact same birthday (day and month)
same_birthday(Person1, Person2) :-
    person(Person1, dob(Day, Month, _)),
    person(Person2, dob(Day, Month, _)),
    Person1 \= Person2.
