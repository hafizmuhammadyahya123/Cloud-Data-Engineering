# Dictionary Comprehension
# syntax: 
# dict = {expresion for temp_var in iteration}
# or 
# dict = {key : value for temp_var in iteration}

diction = {i : i**2 for i in range(6)}
print(f'Exponent for keys-->{diction}')

result = {'john':89 , 'Andrew':60 , 'Emily':92 , 'johnson':68}

passed = {name:marks for name,marks in result.items() if marks > 70}
print(passed)

# Topic: List Comprehension

# This is Normal way Not list comprehension 
list = []
for temp_var in range(10):
    list.append(temp_var)
print(list)
# ------------------------
# similarly, above & below. 
# ------------------------
# But,
# Using list comprehension
lst_comp = [temp_var for temp_var in range(10)]
print(lst_comp)

# TASK: using list compreghension using range() method use for iteration
# but, print numbers is even 
lst_comp = [temp_var for temp_var in range(12) if temp_var % 2 == 0]
print(f'Even Numbers Only---->{lst_comp}')


ListComprehension = [num for num in range(12) if num % 2 == 1]
print(f'Odd Numbers Only--->{ListComprehension}')


ListComprehension = [num for num in range(12) if num % 2 == 1 or num % 2 == 0]
print(f'Mix-->Even & Odd Numbers--->{ListComprehension}')


ListComprehension = [num for num in range(12) if num % 2 == 1 or num % 2 == 2]
print(f'Odd Numbers Only--->{ListComprehension}')


ListComprehension = [num for num in range(12) if num % 2 != 1 or num % 2 == 0]
print(f'Even Numbers--->{ListComprehension}')


ListComprehension = [num for num in range(12) if num % 2 == 2 or num % 2 == 3]
print(f'NULL = {ListComprehension}')

ListComprehension = [num for num in range(12) if num % 2 == 2 or num % 2 == 3 or num == 0]
print(f'NULL = {ListComprehension}')
print('index number = ' , ListComprehension[0])
print(id(ListComprehension))

