delete([],_,[]).
delete([X|T],X,L):-delete(T,X,L).
delete([H|T],X,[H|L]):-delete(T,X,L).

is_sorted([]).
is_sorted([_]).
is_sorted([X,Y|T]):-X<=Y, is_sorted([Y|T]).

deleteFirst([],[],[]).
deleteFirst([X|T],X,L):-deleteFirst(T,[],L).
deleteFirst([H|T],X,[H|L]):-deleteFirst(T,X,L).
