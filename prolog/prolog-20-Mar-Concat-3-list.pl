concat([H1|L1],L2,L3,[H1|A]):-concat(L1,L2,L3,A).
concat([],[H2|L2],L3,[H2|A]):-concat([],L2,L3,A).
concat([],[],L3,L3).

con([H1|L1],[H1|X],A):-add(L1,X,A).
con([],X,A):-add(X,A).

add(L1,[U|V],[U|W]):-add(L1,V,W).
add(L1,[],A):-con(L1,[],A).
add([],_,_).