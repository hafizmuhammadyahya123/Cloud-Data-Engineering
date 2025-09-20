#Topic: sets 
set_a = {'a' , 'b'}
set_b = {'c' , 'd'}
universal_set = {'a' , 'b' , 'c' , 'd'}

print(f'Common Element is {universal_set.intersection(set_a)}')
print(universal_set)

# Syntax
# set.add(elmnt)
# -The add() method adds an element to the set
# -If the element already exists, the add() method does not add the element.
universal_set.add('apple') 
print(universal_set)

# Try to add an element that already exists:
universal_set.add('apple')
print(universal_set)

# Syntax
# set.difference(set1, set2 ... etc.)

# -Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)
print(z)

# Example
# Use - as a shortcut instead of difference()
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

myset = b - a
print(myset)

# Example
# Join more than two sets:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}

myset = a.difference(b , c)
print(myset)

# Example
# Join more than two sets with the - operator:

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}

myset = a - b - c
print(myset)

# Syntax
# set.difference_update(set1, set2 ... etc.)
# Example:
# Remove the items that exist in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)
print(x)

# Example
# Use -= as a shortcut instead of difference_update():
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

a -= b
print(a)

# Example
# Join more than two sets with the -= operator:
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
c = {"cherry", "micra", "bluebird"}

a -= b|c # Separate the sets with | (a pipe operator).
print(myset)

# Syntax
# set.union(set1, set2...)
# Example:
# Return a set that contains all items from both sets, duplicates are excluded:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)
print(z)

# Example
# Remove a random item from the set:
f = {"apple", "banana", "cherry"}

f.pop()  #not parameter passed
print(f)

f.pop() #not parameter passed
print(f)

# Example
# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z) #True

# Example
# Remove "banana" from the set:
# using discard() method
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")
print(fruits)

# Example:
# Insert the items from set y into set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y) #insert
print(x)




