# Methods for str
# strings are immutable

# 1. str.capitalize() 
text_str = 'my text str'  
print(text_str.capitalize()) #first char convert capital
#output My text str

# 2. str.len()
print(len(text_str)) #output 11

# 3. str.center() str length increase starting to ending 
print(text_str.center(15,'_'))  #__my text str__

text_str_1 = 'this is py'
print(text_str_1.center(16,'W'))  # WWWthis is pyWWW 

text_str_2 = 'python'
print(text_str_2.center(12 , '@')) 
#output @@@python@@@

print(len(text_str_2.center(12 , '@')))
# 12

print(text_str_2) # python

print(len(text_str_2)) # 6


# 4. str.count()
text_str_3 = 'java script'
print(text_str_3.count('j')) #1

print(text_str_3.count('a')) #2

# str.upper()  this is case conversion method
text_str_4 = 'julia'
print('small_convert_to_capital-->',text_str_4.upper())

# str.lower() this is case conversion method
text_str_5 = 'MIKE HERTZ'
print('capital_convert_to_small-->',text_str_5.lower())

# str.strip()
text_str_6 = '   string   '
print(text_str_6.strip())  #left to right whitespaces eleminate

# str.lstrip()   this is leading strip method
text_str_7 = '   !!!Julia   ''  g  ''    andrew   '
print(text_str_7.lstrip())  #right side ka whitespace kha gya hr aik str ka 
print(text_str_7)

# str.lstrip()  this is trailing strip method
text_str_8 = '   Julia!!!      j   '
print(text_str_8.lstrip()) #copy main change


# str.strip()
text_str_9 = 'civic'
print(text_str_9.strip('c')) #copy main change
print(text_str_9) #actual main not change, reason--> str are immutable

# str.lstrip()
text_str_a = '   string   ''   hello   ''  string   '
print(text_str_a.lstrip()) #copy main change
print(text_str_a) # actual main not change, reason--> str are immutable

# strip() 
text_str_b = '10001'
print(f'#start sy or end sy equal elimination {text_str_b.strip('1')}') 

print(f' # actual main not change, reason--> str are immutable {text_str_b}')  

# strip()
int_str_c = '  10001  '

print('start or end sy white space remove',int_str_c.strip())

print(f'actual main not change, reason--> str are immutable {int_str_c}')

text_str_d = 'civic'
print(f'first or last character remove jb ho k str palindrome ho ::{text_str_d.strip('c')}')

# removeprefix() 
text_str_e = 'How are you'

print(text_str_e.removeprefix('How'))

print(text_str_e)

print(text_str_e.removeprefix('How are'))

# removesuffix()
text_str_f = 'hello py'
print(text_str_f.removesuffix('py'))

text_str_f = 'hello'
print(f'last sy {text_str_f.removesuffix('llo')}')

# replace()
text_str_g = 'anaconda'
print(text_str_g.replace('anaconda' , 'pycharm'))
print(f"old string main not change ---> {text_str_g}")

text_str_g = 'googlecolab'
print(text_str_g.replace('' , ' '))

text_str_g = 'ANDREW NG IS FOUNDER OF DEEP LEARNING' 
print(text_str_g.replace(' ' , '_'))

print(text_str_g.replace('' , ' '))

print(text_str_g.replace('DEEP LEARNING' , ' D E E P   L E A R N I N G...'))

# find()  
print(f'This particular word start from index number = {text_str_g.find('ANDREW NG')}')
# output --> This particular word start from index number = 0

print(f'index number {text_str_g.find('MACHINE LEARNING')} is not exist...')
# output --> index number -1 is not exist...

print(f'This-particular-word-start-from--index--no# {text_str_g.find('NG')} !!!but-G-is-index-no# 8')
# output --> This-particular-word-start-from--index--no# 7 !!!but-G-is-index-no# 8

# isalnum()  alpha numeric string means A to Z, a to z, 0 to 9
# output = boolean
int_str = '1001'
print('This is alphanumeric char =',int_str.isalnum()) 

int_str = '2'
print('This is alphanumeric char =',int_str.isalnum())

text_str = 'z'
print(f'This is alphanumeric char = {text_str.isalnum()}')

text_str = 'Z'.isalnum()
print('This is alphanumeric char =',text_str)

int_str = '10'.isalnum()
print(f'This is alphanumeric char = {int_str}')

float_str = '3.14'.isalnum()
print('This is not alphanumeric char = ' , float_str)
print('float != alpha numeric character',float_str)