#fillter function used for fillter the values from sequence type
#fillter function need 2 arguments
#one is function another one is iterable obj


#fillter function with out lambda function

# syntaxt :: filter(fun,sequence type)

def check (x):
    if x%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8,9,12,23,45,65,44,56]

data=filter(check,l)
for i in data:
    print(i)

#with lambda function 

data=list(filter(lambda x:x%2==0,l))
print(data)

