#tuples 
tuple1 = ("disk", 10, 1.5)
print(tuple1)

#tuple index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

#tuple negative index
print(tuple1[-3])
print(tuple1[-2])
print(tuple1[-1])

#tuple line 
print(tuple1[1:3])

#tuple sixe
print(len(tuple1))

#tuple sort
tuple2 = (1, 3, 5, 8, 2)
print(sorted(tuple2))

# LIST
l = ["Michael Jackson", 10.1, 1982, "MJ", 1]
print(l)

# List contatenate
l.extend(["pop", 10])
print(l)

# modify element from index
l[1] = 10
print(l)

# Delete element
del(l[1])
print(l)

# Separete string to a list
text = "Hello World".split
print(text)
