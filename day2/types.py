#!/usr/bin/env python

# Integer
i = 10000

# Float point / real number
f = 0.333

i_as_f = float(i) #i is now float
f_as_i = int(f) #rounds up to an integer
 
#Always use spaces instead of TAB

# String , can be single or double quoted
s = "A String"

#Boolean
truthy = True
falsy = False

#Dictionary
d1 = {"key1":"values",
"key2" : "value2"}
d2 = dict(key1 = "value1", key2 = "value2")
d3 = dict([("key1","value1"),("key2","value2")]) #you have tuples inside the list???

#Lists
l =[1, 2, 3, 4 ,5] #convention can only contain one type
l.append(7)

# Tuple
t = (1, "foo", 5.0) #elements can have different types (immutable: cannot append anything to it)


for value in [i, f, s,truthy, l, t, d1, d2, d3]:
    print value, type(value) #type()??? 