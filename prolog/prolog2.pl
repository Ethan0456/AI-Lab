teacher(saleh).
teacher(nora).
father(saleh,jaber).
mother(nora,jaber).
father(hamza,saleh).

parent(Person1,Person2):-father(Person1,Person2);mother(Person1,Person2).
grandparent(Person1,Person2):-parent(Person1,Person3),parent(Person3,Person2).
