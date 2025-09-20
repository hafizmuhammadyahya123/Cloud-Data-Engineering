# Classes

# class initialize with proper name
# constructors
        # attributes 
# Method
# ------------------------------------------------------

# Topic: Oops (Obj Ori Prog)
#    Pillers 4
# - Inheritence:
# - Abstraction:
# - Polymorphisam:
# - Encapsulation: 
class parents():
    def __init__(self , eye_color , hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color

    def can_paint(self):
        print(f"have ability to draw /paint arts")

par_ob:parents = parents('brown' , 'brown')

print(par_ob.eye_color)
print(par_ob.hair_color)
par_ob.can_paint()

class child(parents):
    def __init__(self, eye_color , hair_color , skin_color):
        super().__init__(eye_color, hair_color) #for single class
        self.skin_color = skin_color

    def can_drive(self):
        print(f'child can drive')

child_obj = child('brown' , 'brown' , 'white')
print(child_obj.skin_color)


# class father:
#     def __init__(self , height , color):

#         self.height = height
#         self.color = color

#     def behavior(self):
#         print('Good')
# obj:father = father('5ft 4 inch' , 'white')
# obj.behavior()
# print(f"Height is {obj.height} and color is{obj.color}")      

# class mother:
#     def __init__(self , skin_color):

#         self.skin_color = skin_color

# obj_m:mother = mother('fair')    
# print(obj_m.skin_color)

# class child(father , mother):

#     def __init__(self, height, color): constructor overriding

#         father.__init__(self, height, color)
#         mother.__init__(self, skin_color)
# to be continue ....

# OVERRIDING:
class Animals:
    def eating(self):
        print('Animals can eat')

class Birds(Animals):
    def eating(self):
        print('Birds can eat')

obj:Birds = Birds()
obj.eating()        
      
# OVERLOADING:
from types import overload

class Adder():

    @overload
    def add(self , x:int , y:int): 
        ...

    @overload
    def add (self , x:str , y:str):
        ...

    @overload
    def add (self , x:float , y:float):  

        ...

    #Actual Functionality
    def add (self , x , y):






