#immutable 
 
a = (1, 2, 4, 3, 4, "Vivek", False )
print(type(a))

b = (1)
c=(1,)

print(type(b))
print(type(c))

#methods

no = a.count(4)
print(no)

ind = a.index(3)
print(a)
print(ind)

t = (1, 2, 3)

# Convert to list (to modify)
lst = list(t)
lst.append(4)

# Back to tuple
t = tuple(lst)

print(len(t))