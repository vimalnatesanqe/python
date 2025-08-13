#whenever we access the function, var from another file we need to import that file

import modules
print(modules.add(1,2))

#modules alias name setting
import modules as cal
print(cal.sub(108,56))

#import using from 
from modules import squire
print(squire(5))

#alisaing 
from modules import flor_div as fl_div
print(fl_div(23,2))

#accesing all var,class, function using * keywoord

from modules import *

print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))
print(flor_div(1,2))
print(squire(20))

#naming confilict testing

from modules import *
from modules_nc import *

print(name)
print(age)
print(location)

#both modules variable names are same when we accessing these getting naming comfilict in these 
# we can use alias name or use module.name

import modules
import modules_nc
print(modules.name)
print(modules_nc.name)