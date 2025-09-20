# Topic: Classes 
# - Every thing belongs to some specific **class**
# - Every class can have its **obj**
# - Every class have its own **methods**
# - Class main (constructor / magic method) 1 times create hota hain.
# - behavior/method ko call krty time () ki need ha--->call krty time and print() not use
# - Attributes call krty time () use nahi hoga and print() USE hoga. 
# - constructor class main obj create krny pr amll main aata ha.
# - Object ki 2 characteristics/properties hoti hain .
# 1. Attributes (name , age , color , gender , etc...)
# 2. Behaviors/Actions (walk , eating , talking , drinking , crying , start , run , end , etc...) 
# 

# e.g: class car
#  Attributes (color, model, year_of_manufacture, etc...)
#  Behaviors/Actions (start , end)
class Car():
    def __init__(self , color, model, year_of_manufacture): #Constructor

        self.color = color
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        
    def start(self): #Method

        """
        start object belongs to class car
        arg: No Argument
        return: No Return

        """ 
        print('Car is Started...') 

    def stop(self): #Method
        
        """
        stop object belongs to class car
        arg: No Argument
        return: No Return
        
        """ 
        print('Velocity is zero.')   

obj_c:Car = Car('black' , 'Honda' , '2020')

obj_c.start() #behavior/method k liyay () ki need ha--->call krty time and print() not use
obj_c.stop() #behavior/method k liyay () ki need ha--->call krty time  and print() not use
print(obj_c.color)  #attributes ko call krny k liyay () ki need nahi and print() USE hoga     

# TASK:Create a class of humans that have atleast 2 attributes and methods
class human():
    def __init__(self , name , age , gender , color):

        self.name = name
        self.age = age
        self.gender = gender
        self.color = color

    def walking(self):

        # documentation
        """
        Walking obj/method is belongs to class human
        arg: No Arg
        return: No Return.
        """

        print(f'{self.name} is walking for Half Hours')

    def talking(self):

        # documentation
        """
        talking obj/method is belongs to class human
        arg: No Arg
        return: No Return.
        """

        print(f'{self.name}_is_talking_to_me..')

    def drinking(self):

        # documentation
        """
        drinking obj/method is belongs to class human
        arg: No Arg
        return: No Return.
        """

        print(f'{self.name} is drinking Banana_Shake..')         

    def happy(self):

        # documentation
        """
        happy obj/method is belongs to class human
        arg: No Arg
        return: No Return.
        """  

        print(f'I_wish_you_HAPPY_BIRTHDAY_{self.name}_{self.age}_BIRTHDAY_MUBARAK..')     
#TypeHunting 
person:human = human('Ali' , 27 , 'Male' , 'Fair')


person.walking() #behavior method use krty time () use hoga and print() not use
person.talking() #behavior method use krty time () use hoga and print() not use
person.drinking() #behavior method use krty time () use hoga and print() not use
person.happy() #behavior method use krty time () use hoga and print() not use

print('Age is ',person.age) #Attributes use krty time () use nahi hoga and USE print() 
print('Color is ',person.color)