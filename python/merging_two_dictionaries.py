# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
print(z, "is of type", type(z))

#z
#{'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
#z = dict(x, **y)
#z
#{'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.
