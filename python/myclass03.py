# Concatenation:-
# METHOD -1 (using + operator)
# METHOD -2 (using f-string)
# METHOD -3 (using .format()

# str_1 = "sunlo"
# str_2 = "dehan sy"

# print(str_1 +' '+ str_2) # concatenate using + operator
# print(str_1 + str_2)

# print(f"{str_1} {str_2}") # f string

# print("Acha meri baat sunlo {0} {1}".format(str_1, str_2)) # .format()

# # input from user:-
# name = (input("ENTER YOUR NAME:"))
# print(name)

# int_num = int(input("ENTER YOUR NUMBER.."))
# print(int_num)

# float_num = float(input("ENTER YOUR FLOAT NUMBER..."))
# print(float_num)

# # TASK : input from user & concatenate 
# f_name = input("ENTER YOUR FIRST NAME:")
# midd_name = input("ENTER YOUR MIDDLE NAME:") 
# l_name = input("ENTER YOUR LAST NAME:")

# print('MY_NAME_IS_' +' '+ f_name +'-'+ midd_name +'-'+ l_name) #USING METHOD1: + OPERATOR

# CONDITIONAL STATEMENT
# if elif else

# using if else
eid = False
if eid:
    print("TOMORROW IS HOLIDAY...")
else:
    print("TOMORROW IS WORKING DAY---")     

# TASK: Make a program that tell if you're eligible for certificate or not based on pass/fail.
student_marks = float(input("ENTER_YOUR_MARKS::"))


if student_marks >= 50.00 and student_marks <= 99.99:
    print('you\'re eligible for certificate------')

else:
    print("SORRY__you\"re not eligible")    

# using if elif elase now & show the grades through  
input_from_user = float(input("Enter_your_marks------"))

if (input_from_user >= 90 and input_from_user <= 99.99):
    print("GRADE A+")
elif (input_from_user >= 85 and input_from_user <= 89.99):
    print("GRADE A")
elif (input_from_user >= 80 and input_from_user <= 84.99):
    print("GRADE A-")
elif (input_from_user >= 75 and input_from_user <= 79.99):
    print("GRADE B+")
elif (input_from_user >= 70 and input_from_user <= 74.99):
    print("GRADE B-")    
elif (input_from_user >= 60 and input_from_user <= 69.99):
    print("GRADE C")    
else:
    print("OTHER WISE GRADE = (D E F)")  

# nested if-else
shop_open = True

if shop_open:
    print("shop is open have to check rice now")
    basmati_rice = input("check for basmati:")
    if basmati_rice:
        print("BUY 1KG..")
    else:
        print("Buy Nothing..")
else:
    print("shop_is_closed----")                        

''' Write a program to check whether a person is eligible 
for voting or not. (accept age from user) if age is greater 
than 17 eligible otherwise not eligible'''
req_age = int(input("PLEASE ENTER YOUR CURRENT AGE..."))

if req_age >= 18:
    print("you are eligible for voting me---")
    print("THANK YOU FOR VOTING ME..")
else:
    print("SORRY yor are not eligible.....")   

# --------------------------------------------------------------------------

# Trafic light system using conditional statement
signal_A = False
signal_B = True

if signal_A:
    print("After one kilometer distance cover by a car....")
    print("I see one trafic lights signal")
    light = input("ENTER LIGHT COLOR..")
    if light == "Red":
        print("strictly_stoped_now")
        if light == "Yellow":
            print("(yellow or amber) means proceed with caution, but stop if it is safe to do so.")
            if light == "Green":
                print("Go or Crossing.....")
    
    elif signal_B:
        print("save_driving")
else:
    print("After one kilometer distance cover by a car....")  
    print("I see not any traffic light signal")      
            
#-----------------------------------------------------------------
my_car_is = input("Enter yiur car color..")

if my_car_is == "blue":
    print(f"My_car_is: {my_car_is}")
else:
    print("ye car meri nahi ha")    

# ----------------------------------------------------------------
# how to create weather condition using conditional statement
today_weather_condition = input("TODAY_WEATHER_IS..")

if (today_weather_condition == "rainy"):
    print("apny_outdoor_work_krlain")
    save = input("stay_home:")
    if save == "stay_save":
        print("ENJOY_RAINY_DAY")
        lunch_dinner = input("cooked...")
        if (lunch_dinner == "ghrr_prr"):
            print("Germs_sy_bachna_possible_ha.")
        else:
            print("weather_is_normal")   

elif (today_weather_condition == "sunny"):         
    print("time_serve_krein_normal_routine_k_hisaab_sy...")
else:
    print("Temperature_is_normal----")     

#----------------------------------------------------------------------
tomorrow_weather_condition  = bool(input("Eneter_prediction...."))

if tomorrow_weather_condition == True:
    print("apni_life_normal_serve_krein")
else:
    print("apny_outdoor_k_kaam_aaj_hi_kr_lain")
       
