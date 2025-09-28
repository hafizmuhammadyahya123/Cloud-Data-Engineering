# Modules:

import modules as m
# call fn
sum = m.add_num(2 , 4)
print(sum)

# ---------------------OR--------------------

from modules  import add_num as add
sum = add(2,6)
print(sum)

# --------------------------------------------------------------------------
import modules as m
a , b = 1 , 5
# call fn 
int = m.my_number_display(10 , 3 , 1)
print(int(7 , 8))
