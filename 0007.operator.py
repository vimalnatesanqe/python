# diffrent type of opreators available
# 1.arithamatic
# 2.assignment
# 3.relational
# 4.logical
# 5.unary minus
# #special operator
# 1.identy opreator
# 2.membership opreator

#arithmatic operator

a,b=100,10
#addition
print(a+b)
#subtraction
print(a-b)
#multiplication
print(a*b)
#divison
print(a/b)
#floor division
print(a//b)
#modules
print(a%b)
#power
print(a**2)
#####################

#assignment operator
a=b=c=10
print(a,b,c)
a,b,c=10,20,30
print(a,b,c)
a+=1
print(a)
a-=1
print(a)
a/=b
print(a)
b*=c
print(b)

#relational operator

a,b,c=10,20,30

print(a<10)
print(a>10)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)

#logical operator

print(a and b)
print(a or b)
print(not a)

#unary minus operator

a=100
a=-a
print(a)

#special operator

a=100
b=100

#identy operator

print (a is b)
print( a is not b)
print(id(a))
print(id(b))
#checking memory address

#membership operator in and not
#checkig wether the data present in sequence data type

a="vimalathithan" 
print('t' in a)
print('k' not in a)
print('k' in a)
