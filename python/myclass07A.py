# Loops

# Syntax of for loop:
# -------
# for temp_var in itreateble():
#     loop_body

# for temp in ([1 , 2 , 3 , 4 ,5]):
#     print(temp)

# for temp in (['Qasim' , 'Hassan' , 28 , 60 , True]):
#     print(temp)  

# Task:
# Write a program that prints 'Happy Birthday!' five times on screen  
# wish = input('Birthday Wishes..')
# for ele in range(6):
    # print(ele , wish)

# OR---------------------------------------------------------------- 
# better way:-
# wish = ['Happy Birthday!\n'*5] 
# for ele in wish:
#     print(ele)   

# OR----------------------------------------------------------------
# professional work:-
# times = int(input('Enter five times:'))
# for ele in range(times):  Dynamic
#     print(ele , 'Happy Birthday!')

# OR------------------------------------------------------------------
# Hard code:-
# wish = ['Happy Birthday!','Happy Birthday!','Happy Birthday!','Happy Birthday!','Happy Birthday!']
# for ele in wish:
#     print(ele)

#Task: 
# write a program that takes a number n as an input from user and generates the first n terms 
# of the series formed by squaring the natural number
input_my_user = int(input('Enter number..'))

for ele in range(input_my_user):

    ele **= 2
    print(ele)

# ---------------------------------------------------------------------------------------
input_from_user = int(input('Enter number..'))

for ele in range(input_from_user):

    ele **= 2
    print(ele+1)

# =======================================================================================
for ele in range(1 , 5):
    ele **= 2
    print(ele)    


i = int(input('enter no#'))
for ele in range(4):

    i -= 1
    i **= 2

    print(ele , i)    


num = 2
for ele in range(11):

    if num >= 0 or num <= 0:

        num -= 1
        num **= 2

        print(ele , f'BINARY CODE = {num}') 

# Task: Write a program that prompts the user to input a number and prints its multipliction table
table = int(input('Enter Number'))
time = int(input('How many times are print in this table:'))

for temp in range(time):
    print(f"{table} * {temp} = {table * temp}\n")

# ---------------------------OR----------------------------------------------
my_table = int(input('Enter Number..'))
times = int(input('Enter times'))

for temp_var in range(times):
    print(f"{my_table} * {temp_var} = {my_table * temp_var}\n")

MyTable = int(input('Enter Number...'))
Times = int(input('Enter times'))

for temp_var in range(Times):

    temp_var += 1
    print(f"{MyTable} * {temp_var} = {MyTable * temp_var}\n")

# ---------------------------------------------------------------
tab = 5
time = 11
for temp in range(1 , time , 1):
    print(f"{tab} * {temp} = {tab * temp}")

# ---------------------------------------------------------------
Number , Times = 10 , 12
for temp in range(Times):
    print(f"{Number} * {temp} = {Number * temp}")

#----------------------------------------------------------------
# print table of 6 and 6 multiply by only even numbers.
num = 6
for  temp in range(2 , 11 , 2):
    print(f"{num} * {temp} = {num * temp}")

# # ---------------------------------------------------------------
#print table of 7 and 7 multiply by only odd numbers.
num = 7
for temp in range(1 , 11 , 2):
    print(f"{num} * {temp} = {num * temp}") 