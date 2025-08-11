# aruguments are diffrent types in python
#positional
#keyword
#default
#variable length 
#key word length argument

#positional arguement
#it is working position wise

def pos_arg(a,b,c):
    sum=a+b+c
    print(sum)
    return sum
pos_arg(1,2,3)

#default argument
#default value will set if the argument value is null
def default_arg(a,b,c=0):
    sum=a+b+c
    print(sum)
    return sum
default_arg(1,2)

#keyword argument
#it is working based on the key word 
#key word argument always followed by positional argument

def keyword_arg(a,c,b):
    sum=a+b+c
    print(sum)
    return(sum)
keyword_arg(a=10,b=30,c=100)

#varible length argument 
#we can pass multiple values and collections at the same tile
#it it treat as like a tuple
#it should be always followed by positional, keyword agrumens
# using *

def var_length_arg(*a):
    sum=0
    for i in a:
        sum+=i
    print(sum)
    return sum
var_length_arg(1,2,3,4,5,6,7,8,9,10)

#keyword length argument
#it is used to store key values pairs
#** represents
# it is treat like as dictionary concepts

def key_var_length_arg(**var):
    sum=0
    count=0
    for i in var.values():
        sum+=i
        count+=1
    print(sum)
    print(count)
    return var

key_var_length_arg(one=1,two=2,three=3,four=4)

print(pos_arg(1,2,3))
print(default_arg(1,2))
print(keyword_arg(a=10,b=30,c=100))
print(var_length_arg(1,2,3,4,5,6,7,8,9,10))
print(key_var_length_arg(one=1,two=2,three=3,four=4))



