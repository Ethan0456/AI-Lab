count_member(X,[]):-write(X).
count_member(X,[_|Y]):-count_member(X+1,Y).
