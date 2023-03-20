list_member(X,[X|_]).
list_member(X,[_|Y]):-list_member(X,Y).
