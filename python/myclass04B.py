#   Topic: tuple
# - Tuple are immutable
# - Given Methods are 2

student_name_tuple = ('Ali' , 'Hamza' , 'Aliyan' , 'Murtaza' , 'Andrew')

print(student_name_tuple)
print(type(student_name_tuple))

# Multiplle data types store in tuple
MultipleDataTypes = ('pytorch' , 10001 , 59e9 , True , ['LIST' , 1])

print(MultipleDataTypes)
print(id(MultipleDataTypes))

# ----------------------------------------------------------------------------------------------
MultipleDataTypes[4][1] = -1001  #yahan error nahi mila
print(MultipleDataTypes)

# Diff B/W
#                                  Tuple are immutable
# MultipleDataTypes[4] = 1000002  .TypeError: 'tuple' object does not support item assignment
# print(MultipleDataTypes)
# ----------------------------------------------------------------------------------------------

# Methods for Tuple
# 1. count() 
# 2. index() 
l = (1 , 3 , 3 , 'five' , 9 , 13)
print(f'3 is {l.count(3)} Times Repeated..')
print(f'3 is Index No# {l.index(3)}')
print(f'Index No# {l.index('five')}')

# Slicing for tuple
tup = (1 , 2 , 't' , 'f' , 5 , 5e5 , True)
print(f'Index No 3 = {tup[3]}.')
print(f'Index 1 to 5 is {tup[1:6]}')
print(f'Index 0 to 5 = {tup[:6]}')
print(f'Index 0 to nth term = {tup[0:]}')




