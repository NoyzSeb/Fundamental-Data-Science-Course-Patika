a=set()
b=set()
a={1,2,2,2,1,4,5}
b={1, 2, 3, 10}
a.add(6)
a.discard(1)
c=a.union(b)

print(c)
print(a.intersection(b))
print(a)
print(c.isdisjoint(b)) #c ∩ b ≠ Ø
print(b.issubset(c))
print(c.issuperset(b)) 
