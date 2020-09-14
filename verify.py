def insert(d, k, c):
    if k in d:
        d[k] += c
    else:
        d[k] = c
    if k in d and d[k] == 0:
        del d[k]

d1 = {}
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if (i,j,k) in [(1,2,3),(2,3,1),(3,1,2)]:
                mul = 1
            elif (i,j,k) in [(3,2,1),(1,3,2),(2,1,3)]:
                mul = -1
            else:
                mul = 0
            # The expansion of the left hand side
            insert(d1, (1,j,k,1,i), 2*mul)
            insert(d1, (2,j,k,2,i), 2*mul)
            insert(d1, (3,j,k,3,i), 2*mul)
            insert(d1, (1,1,j,k,i), 1*mul)
            insert(d1, (2,2,j,k,i), 1*mul)
            insert(d1, (3,3,j,k,i), 1*mul)
            insert(d1, (1,j,1,k,i), -1*mul)
            insert(d1, (2,j,2,k,i), -1*mul)
            insert(d1, (3,j,3,k,i), -1*mul)

d2 = {}
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if (i,j,k) in [(1,2,3),(2,3,1),(3,1,2)]:
                mul = 1
            elif (i,j,k) in [(3,2,1),(1,3,2),(2,1,3)]:
                mul = -1
            else:
                mul = 0
            # The expansion of the right hand side
            insert(d2, (i,j,k,i,i), 2*mul)
            insert(d2, (i,i,j,k,i), 1*mul)
            insert(d2, (i,i,j,i,k), 1*mul)
            insert(d2, (i,j,i,k,i), -1*mul)
            insert(d2, (i,j,i,i,k), -1*mul)

for k in d1:
    if k not in d2:
        assert False, "Not Equal"
for k in d2:
    if k not in d1:
        assert False, "Not Equal"
for k in d1:
    if d1[k] != d2[k]:
        assert False, "Not Equal"
print("Equal")
