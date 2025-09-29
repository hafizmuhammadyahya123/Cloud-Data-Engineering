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

# Normal Way.. 
# not use list comprehension
# using conditins(if, else)
list = []
for temp_var in range(10):

    if temp_var % 2 == 0:
        list.append(temp_var)
    else:
        list.append('odd')

print(list)        
# ---------------------------
# similarly, above and below
# ---------------------------
# list comprehension & using condition(if, else)
# .Jb more then 1 conditions use ho tB conditions pehly store & phir loop

lst_comp = [temp_var if temp_var % 2 == 0 else "odd" for temp_var in range(10)]
print(lst_comp)

# List comprehension & using 1 condition only 
# .Jb 1 condition use ho tb loop pehly and condition baad main store hogi List comprehension main
lst_comp = [temp for temp in range(10) if temp % 2 == 0]
print(lst_comp)

lst_comp = [i if i % 2 == 1 else 'Even_Number' for i in range(12)]
print(lst_comp)
# -----------------------------------------------------------------
lst_comp = [i if i % 2 == 0 else [i , 'is_odd'] for i in range(12)]
print(lst_comp)
print(lst_comp[1])

lst_comp = [i if i % 2 == 1 else {i : 'even_no#'}  for i in range(7)]
print(lst_comp)
print(f'index number = 0 = {lst_comp[0]}')

# . List Comprehension main elif nhi use hota only 2 conditions allowed(if , else) 
# --------------------------------------------------------------------------------

# Topic: Dictionary Comprehension

# Normal way of coding without Dict Comp
lst1 = ['Name' , 'Age' , 'Gender' , 'Salary']
lst2 = ['Qasim' , 28 , 'Male' , 6000000]

bio_data = {}
for temp_var in zip(lst1 , lst2):

    bio_data[temp_var[0]] = temp_var[1]

print(f'BIO_DATA{bio_data}')

# Use Dictionary Comprehension
dic_comp = {i[0]:i[1]  for i in zip(lst1 , lst2)}
print(f'Write Bio Data uing Dictionary Comprehension {dic_comp}.')



