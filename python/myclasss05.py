# LIST 
# 1. list are mutable
# Mutable data structure main variable main address assign hota ha.
# 2. list -->  multiple data types store are allowed
# 3. list k under dictionaary or dictionary k under list store kr skty hain
# 4. nested list bhi create kr skty hain 
num_list = [1,2,3,4,5]
print(f"list {num_list}")
print('DATA TYPE IS',type(num_list) , 'ADDRESS = ' , id(num_list))

ListString = ['A' , 'P' , 'P' , 'L' , 'E']
print('list',ListString)
print('DATA TYPE =' , type(ListString) ,'ADDRESSS =' , id(ListString))

float_list = [3.14 , 72.76 , 1.1]
print(f"list {float_list}")

bool_list = [True]
print(type(bool_list))

# multiple data type store
MutipleDataTypesList = ['py', 1, 3.14, True, (1,4,6), {'C#' : 'programming'}, ['julia'], {2,4,6}]

print(f"my_multiple_data_type_list {MutipleDataTypesList}...") 

print('DATA TYPE = ' , type(MutipleDataTypesList) , '\n' 'ADDRESS = ' , id(MutipleDataTypesList))

# nested list
nest_list = [ 1, 24, 56, ['py','R',{'py':'prog', 'R':'prog'}]]
print(nest_list)

print('index no#3 is equal to',nest_list[3])

print('index no#3 ka index no#1 is equal to \t',nest_list[3][1])

print('index no#3 ka index no#2 =' , nest_list[3][2])

nest_list.append('julia')
print(nest_list)

nest_list.extend(['C++' , 'C##'])
print(nest_list)

nest_list.insert(0 , 'Neural Network')
print(nest_list)

# Mutable data structure main variable main address assign hota ha.
# Value by refrence
a = [1 , 2  , 3 , 4]
a[0] = 1001 
b = a 
print(b,a)
print(id(b) , id(a))

b[0] = 20001
print(b , a)
print(id(b) , id(a))

b = 12
c = b
print(c , b)
print(id(c) , id(b))

