# print table 2 to 5 but print (2 by 10,3 by 9, 4 by 8, 5 by 7)

table_2 = 2
for temp in range(10):

    temp += 1
    print(f"{table_2} * {temp} = {table_2 * temp}")

print("TABLE OF 2 IS COMPLETED...\n")   

table_3 = 3
for temp in range(9):

    temp += 1
    print(f"{table_3} * {temp} = {table_3 * temp}")    

print("TABLE OF 3 IS COMPLETED...\n")   

table_4 = 4
for temp in range(8):
    temp += 1
    print(f"{table_4} * {temp} = {table_4 * temp}")

print("TABLE OF 4 IS COMPLETED...\n")       

table_5 = 5
for temp in range(7):

    temp += 1
    print(f"{table_5} * {temp} = {table_5 * temp}")    

print("------------FINALLY TABLE OF 5 IS COMPLETED--------------")     

# -----------------------------------------------------------------------
# Task:print table 2 to 5 but print (2 by 10,3 by 9, 4 by 8, 5 by 7)
times = 11
for table in range(2 , 6):
    for temp in range(times):
        print(f"{table} * {temp} = {table * temp}")  
    times -= 1 

# better way
#Convert Dynamic way in above  code
start = int(input('Enter starting table'))
end = int(input('Enter stop table')) 
times = int(input('Enter times..'))

for table in range(start , end):
    for temp_var in range(times):

        print(f"{table} * {temp_var} = {table * temp_var}")
    times -= 1    

#----------------------OR----------------------- 
start_table = int(input('Enter start table'))
stop_table = int(input('Enter end table'))
times = int(input('Enter times..'))

for tables in range(start_table , stop_table):
    for temp_var in range(times):
        print(f"{tables} * {temp_var} = {tables * temp_var}")
    times -= 1

    
      


