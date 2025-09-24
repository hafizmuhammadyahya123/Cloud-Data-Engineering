# function
def add (num1 , num2):
    return num1*num2

# Lamda Function
# - without name
# - never been called before or after 
# - No Return Keyword
(lambda x , y : x + y) (8 , 9)

fn = lambda x,y : x+y
print(fn(8 , 9))

criteria = lambda marks: "pass" if marks > 50 else "fails"
print(criteria(51))
print('Your Status is = ',criteria(40))

# Classes
class saylani():
    helpline = '000099012809'


    def __init__(self , campus , staff_acc , courses_acc):

        self.campus = campus
        self.staff = staff_acc
        self.course = courses_acc

    def details(self):
        print(f"{self.campus} have {self.staff} and courses are {self.course}")

za = saylani("ZA IT PARK" , 10 , 5)
print(za.details())
print(za.helpline)

# Task:
# create a class of a cars with atleast 3 attributes and two methods such that once method should be static.Also
# class  should have 2 class variables and one should  dynamic

class car:
    def __init__(self , color , car_type , model_year):

        self.color = color
        self.car_typ = car_type
        self.model_year = model_year

    def details(self):
