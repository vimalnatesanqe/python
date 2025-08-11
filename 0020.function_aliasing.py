# function aliasing means we are changing the function name one to another
#  but all the chenged names are pointing the same object

#example1:

#wap change the function name

def alias(a,b):
    '''this function used for alias concept'''
    print(a+b)
    print(a-b)
    print(a*b)
    print(a**b)
    print(a/b)
    print(a//b)
alias(10,20)
change_fun_name=alias
change_fun_name(10,20)
print(alias is change_fun_name)

print(id(alias))
print(id(change_fun_name))

change=change_fun_name
print(id(change)) #name only diffrent but all the names are pointing the same object
