delete([],_,[]).
delete([X|T],X,L):-delete(T,X,L).
delete([H|T],X,[H|L]):-delete(T,X,L).

sort(_,[]).
sort(X,[Y|T]):-sort(X,T),X<=Y.

deleteFirst([],[],[]).
deleteFirst([X|T],X,L):-deleteFirst(T,[],L).
deleteFirst([H|T],X,[H|L]):-deleteFirst(T,X,L).
