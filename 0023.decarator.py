# decarator used for modify or extrend from the base function.
#this changes can achive by with out touch by base function

#when we a pass a function as a prameter to another function and perform the update or extend 


#base function
def base_fun(a,b):
    '''base function'''
    print(f"the total value is {a+b}")



#decarator function
def decr_fun(fun):
    def changes(para1,para2):
        print(para1.center(50,"*"))
        fun(100,100)
        print(para2.center(50,"*"))
    return changes
copy_base=decr_fun(base_fun)
copy_base("start","end")

#there is another way to write this program


#decarator function
def decr_fun(fun):
    def changes(para1,para2):
        print("start".center(50,"*"))
        fun(para1,para2)
        print("end".center(50,"*"))
    return changes
#copy_base=decr_fun(base_fun)  #remove these lines--no need to specify isted of using @
#copy_base("start","end")

@decr_fun # it will assign the decarator function
def base_fun(a,b):
    '''base function'''
    print(f"the total value is {a+b}")

base_fun(1000,2000)

def fun1(a=0):
    def fun2(b,c):
        print(a+b+c)
    return fun2
x=fun1(100)
print(x(200,300))

