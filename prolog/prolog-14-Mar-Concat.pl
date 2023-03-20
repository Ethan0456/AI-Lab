list_concat([],L,L).
list_concat([X1|L1],L2,[X1|L3]):-list_concat(L1,L2,L3).

concat(H,H).
concat(H,[H|T]):-concat(H,T).
