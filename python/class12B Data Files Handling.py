# DATA FILES
# . read-->'r'
# . write-->'w'
# . append-->'a'
# read/write-->'w+'

# METHOD1 - We have to specificially close the file
f = open('file.txt' , 'w') 
print(f.write('this is the contect of my file'))
f.close()

# METHOD2 - file will close  automatically (Recommended Method)
# using --> with --> ye automatically file closed krta ha without close method
with open('file.txt' , 'w')  as f:
    f.write('Now file will  automically close.') #this will override the content in file if file exists 

# using append --> denoted by 'a' and using escape character like line next line shifted using \n
with open('file.txt' , 'a') as f:
    f.write('Now this line will get append in the file. \n this will get append on next line')

