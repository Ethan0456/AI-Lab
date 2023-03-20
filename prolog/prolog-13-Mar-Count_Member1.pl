count([],0).
count([_|T],N):-count(T,N1),N is N1+1.

count1(0,[]).
count1(X,[_|Y]):-count1(X1,Y), X is X1+1.
