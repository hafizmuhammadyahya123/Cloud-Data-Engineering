# DICTIONARY 
# 1.KEY VALUE PAIRS
# 2.Curly brackets
# 3.All pairs comma seprated
# syntax: {key : value}

my_dic = {"name" : "Andrew NG" , "gender" : "Male" , "Andrew NG":"Founder_Of_Deep_Learning"}
print(my_dic)
print(f"Data Type = {type(my_dic)} \nAddress = {id(my_dic)}")

fruits_dic = {}
fruits_dic['apple','banana','orange'] = 'is_red','is_yellow','is_orange'

print(fruits_dic)
print(type(fruits_dic))

vegies_dic = {}
vegies_dic['lady_finger'] = 'is_green'
vegies_dic['tomato'] = 'is_red'

print(vegies_dic)


fruits_dic = {}
fruits_dic['apple' 'banana' 'orange'] = 'is_red' 'is_yellow' 'is_orange'

print(fruits_dic)
print(type(fruits_dic))

my_diction = {"Weather_is":'sunny',
              "weather_is_rainy":True,
              "weather_is_hot":False,
              "today_is_rainy_day":1,
              "one_is":True,
              "zero_is":False,
              "Binary":[1 , 0],
              "Binary_classification":[True,False,'Male','Female','Yes','No','+ive','-ive','spam','not_spam'],
              "classification":["categorical_data","only_English"],
              "Regression":["numerical_data","only_numbers"],
              "Types_Of_Supervised_Leraning":{"Two_types":['1.Classification','2.Regression']}
              }

print(my_diction)
my_diction['weather_is_hot'] = 'Agree'  #key ki value change 

# -----------------------Methods for diction-------------------------

print(f"All_Keys = {my_diction.keys()}\n") #Returns a list containing the dictionary's keys

print(f"All_values = {my_diction.values()}\n") #Returns a list of all the values in the dictionary

print(f"Returns a list containing a tuple for each key value pair {my_diction.items()}\n")

# Syntax pop()
# dictionary.pop(keyname)
my_diction.pop('Weather_is') #The pop() method removes the specified item from the dictionary.
print(f"{my_diction}")
print(f"{type(my_diction)}\n")

# Syntax
# dictionary.popitem()
x = my_diction.popitem()  #The popitem() method removes the item that was last inserted into the dictionary.
                          
print(x)
print(type(x))

# The update() method inserts the specified items to the dictionary
my_diction.update({'Unsupervised Learning is':'Algo'})
print(my_diction)
print(type(my_diction))

# Looping Dictionaries--------------------------------------------
for temp in my_diction:  #only keys pass ki
    print(temp) 

for temp in my_diction.values(): #only values pass ki
    print(temp)

for temp in my_diction.items(): #all pairs print but tuple ki form main
    print(temp)    

for key , value in my_diction.items(): #key value pairs pss but not tuple form main
    print(f"{key}---->{value}")   

# ==========================================
#Home.Work all dictionary methods apply... 
#Home.Work all list methods apply... 
# ==========================================

