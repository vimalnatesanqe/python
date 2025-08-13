import random

# this is one way but not recomadned
#print(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),sep='')

otp=''
for i in range(5):
    otp=otp+str(random.randint(0,9))
print(otp)

name="vii"
name[0]='J'
print(name)
for i in "vimalathithan":
    name+=i
    print(i)
    print(name)