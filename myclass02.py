# This is a markdown cell so we ahve to follow the markdown syntax.
# This is level-1 heading
# This is level-2 heading
# This is level-3 heading
# This is level-4 heading
# This is level-5 heading
# This is level-6 heading
# Shortcuts for jupyter notebooks
# ESC + M (to convert cell into markdown)
# ESC + R (to convert cell into Raw)
# ESC + Y (to convert cell into Code)
# 1 ..... #6 ( for level-1/level-6 heading)
# ESC + A (to create cell above the present cell)
# ESC + B (to create cell below the present cell)
# ESC + DD (to delete the cell on which you're present)
# SHIFT + ENTER (to run the cell and goto next cell)
# CTRL + ENTER (to run the cell and not goto next cell)
# CRTL + SHIFT + H ( to get all jupyter noteboo shortcuts

# variables:-
my_str = "this is str"
print(my_str)
print(type(my_str))

int = 19
print(int)
print(type(int))

float = 3.14
print(float)
print(type(float))

is_present = True
print(is_present)
print(type(is_present))

# additional stuff
# 1. type() - to give you the type of the variable
# 2. id() - to give you the address of the variable

# 1.
type(float)

# 2.
id(float)
print(id(is_present)) #address
print(id(my_str)) #address
print(id(float))

# Expressions:- (PEMDAS)
# PEMDAS
# Paranthesis,
# Exponential(power),
# Multiplication,
# Division,
# Addition,
# Subtraction

print((2-3)-(4-3)-4/5) #  ---->(A)
# solve eq--(A) step by step follow The PEMDAS Rule
print(2-3) #-1
print(4-3) #-1
print(-4/5) #-0.8
print(-1 - 1 - 0.8) 

(((4+5)**2)*4)/5+(3-2) #  ---->(B)
# solve eq--(B) step by step follow The PEMDAS Rule
print(4+5) # 9
print(9 ** 2) # 81
print(81 * 4) # 324
print(3 - 2)  # 1
print(324 / 5) # 64.8
print(64.8 + 1) 

(3-2)/5+(((4+5)**2)*4) # ---->(C)
# solve eq--(C) step by step follow The 'PEMDAS' Rule
print(3 - 2) # 1
print(4 + 5) # 9
print(9 ** 2) # 81
print(81 * 4) # 324
print(1 / 5) # 0.2
print(0.2 + 324)

# y = ( m * x + b ) #now solve this formula ----> using PEMDAS RUL
x = 9
m = 6
b = 1

y1 = (m * x) # 54
y2 = (y1 + b) # 54 + 1
y = y2

print(y1)
print(y)

# dependent_var = (slop * independent_var + intercept) ---> solving this formula using PEMDAS RULE
# dependent_var = 
slop = 8
independent_var = 16
intercept = 0.001

dependent_var_1 = slop * independent_var
dependent_var = dependent_var_1 + intercept

print(f" (slop * independent_var + intercept) = {dependent_var} ")
print(f" {dependent_var} = (slop * independent_var + intercept) ")
print(f" {dependent_var_1 + intercept} is equal to (slop * independent_var + intercept) ")

# OPERATORS:-
# ADVANCE OPERATORS / AUGMENT STATEMENT:-
# +=, -=, /=, *=
x = 10
x += 20
print(x)

augment_stat = 20
augment_stat -= 50
print(augment_stat)

AugmentStatement = 100
AugmentStatement += 20
print(AugmentStatement)

x1 = 100
x1 /= 10
print(x1)

y1 = 100 
y1 //= y1
print(y1)

z1 = 100
z1 /= z1
print(z1)

int_2 = 200
int_2 //= 50
print(int_2)  #4

int_3 = 200
int_3 *= int_2
print(int_3) #800

int_2 += int_3
print(int_2) #804

int_2 //= int_3
print(int_2)  #1

int_2 /= int_3
print(int_2)  #0.00125

int_2 *= int_2
print(int_2)

x = 12
x %= 2 #reminder
print(x)

x ^= 2
print(x)

x >>= 2
print(x)

x <<= 2
print(x)

x |= 10
print(x)

x &= 10
print(x)

# COMPARISION OPERATOR:
num1 = 10
num2 = 12
print("num1 > num2 is", num1 > num2) 

print("num2 > num2 is:", num2 > num1)

print("num2 >= num1 this is :", num2 >= num1)

print(f"num2 == num1 this is: {num2 == num1}") #False

print(f'num1 == num1 this is: {num1 == num1}') #True

print(f'num2 > num2 this is absolutely wronge::{num2 > num2}') #num2 > num2 this is absolutely wronge::False

print(f'num1 < num2 this is: {num1 < num2}') #True

print(f'num1 != num2 this absolutely::{num2 != num1}') # is not equal to

# LOGICAL OPERATORS
# most usefull 1.and, 2.or, 3.not
NumberOne = 100
NumberTwo = 10

# 1. and
print("this is :", NumberOne > NumberTwo and NumberOne < NumberTwo) #this is : False

print(f"this_is_Absolutely::{NumberOne != NumberTwo and NumberOne < NumberTwo}") #this_is_Absolutely::False

print(f'is....{NumberTwo == NumberTwo and NumberOne == NumberTwo}') #is....False

print(f'is....{NumberTwo != NumberOne and NumberTwo == NumberTwo}') #is....True

print(f'is....{NumberTwo == NumberTwo and NumberOne == NumberOne}') #is....True

# 2. or
print(f"is-----{NumberOne >= NumberTwo or NumberOne <= NumberTwo}") #True

print(f'is----{NumberOne == NumberTwo or NumberOne == NumberOne}') #True 

print(f'is----{NumberOne != NumberOne or NumberOne <= NumberTwo}') #False

print(f'is----{NumberTwo > NumberOne or NumberTwo < NumberOne}') #True

# 3. not
print( "is----", not(NumberOne == NumberTwo and NumberTwo == NumberOne) )  #True

print('is----' , not(NumberOne >= NumberTwo or NumberTwo != NumberTwo))  #False

# Concatenating text strings:-
# there are three methods
f_name = "muhammad"
l_name = "umar"

# Method 1
full_name = f_name + l_name #Method 1 using + operator
print(full_name)

full_name = f_name +' '+l_name #Method 1 using + operator
print(full_name)

# Method 2 
full_name = f"{f_name} {l_name}"
print(full_name)

# Method 3
full_name = "{0} {1}".format(f_name , l_name)
print(full_name)

midd_name, l_name = "umar", "farooq"
full_name = "{0} {1} {2}".format(f_name, midd_name, l_name)
print(full_name)

full_name = "{1} {0} {2}".format(f_name, midd_name, l_name)
print(full_name)

# practice
# method 1 USING + OPERATORS
p_for, y_for, t_for, h_for, o_for, n_for = ('polynomial', 'youth', 'torque', 'histogram', 'organic', 'nested loop')
concatenate_str = p_for + y_for + t_for + h_for + o_for + n_for
print(concatenate_str)

concatenate_str = p_for +' '+ y_for +' '+ t_for +' '+ h_for +' '+ o_for +' '+ n_for 
print(concatenate_str)

apple = red = green = "FRUIT"
apple_is = apple +' '+ red
print(apple_is)

apple_is = red +' '+ green
print(apple_is)

apple_is = red +' '+ red
print(apple_is)

# method 2 f string
apple_is = f"juicy...{red} juicy...{green}"
print(apple_is)

# method 3  "{}".format()
apple_is = "this is juicy {0} color is red {1} color is green {1}".format(apple, red, green) 
print(apple_is)

# method 1 using + operator
two_plus_two = "4"
print(" the sum of two plus two is = " +' '+ two_plus_two)