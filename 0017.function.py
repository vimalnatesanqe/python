# when we need to run a peice of code multiple times then go for function as method
#function created for re usability
#it will reduce duplicate codes


# normal function structure

def function_name(parameter):
    '''This is a docu string which used for decribe about the function'''
    #block of code
    for i in range(1,10):
        print("vimal",i)
    return parameter  # return the value to function

function_name("vimal") # function calling and argument passing and #after completion of block of code this funtion will return "vimal"

#type of function in-build and user defied
#in-build fun like print,count,len,min,max..etc
#user defined function we carete a function by our own

#doc string
'''doc strig basically used for about function information'''
print(print.__doc__)


#normal function
def fun_name():

    print("vimal")
fun_name() #funcation calling

#function return value
def fun_name1(a,b,c):
    '''this function used to calculate 3 values'''
    return a,b,c,a+b+c
Ref_var=fun_name1(1,2,3)
print(Ref_var)


#function with parameter
def fun_name2(a,b,c): #parameter a,b,c
    print(a+b+c)
    return("hey vimal")
Ref_var=fun_name2(1,2,3)# arguments
print(Ref_var)


#wap check the aruments values are odd or even by using function

def odd_even(para_a):
    '''this is function will check parameter value odd or even'''
    print("this is a even nbr" if para_a%2==0 else "this is odd nbr")
    return "function completed"
while True:
    arg_value=int(input("enter your checking value"))
    odd_even(arg_value)
    user_choice=input("do you want to check again y/n::")
    if user_choice=='n':
        break

#function call by value #like immutable type(numeric,string,tuple)
# if we made any changes in inside called function, this changes not reflect to outside of function

def call_by_value(para_a,para_b):
    '''this is function created for call by value checking ids before and after function call'''
    print("before changing",id(para_a),id(para_b))
    para_a,para_b=1,2
    print("after changing",id(para_a),id(para_b))
para_a,para_b=3,4
print("before function call",id(para_a),id(para_b))
call_by_value(para_a,para_b)
print("after function call",id(para_a),id(para_b)) ## it is not relect after function call still pointin thr same memory

#call by referrance ref means mutable obj like list,set,dict
#if any changes happened after function calling, this changes should refect in outside of the function also
def call_by_ref(para_ref):
    '''this programe example of call by referrance like mutable obj'''
    print("before adding",id(para_ref))
    para_ref.append(1000)
    print("after adding",id(para_ref))
mute_obj=[1,2,3,4,5,6]
print("outside of mute obj and before function call",id(mute_obj))
call_by_ref(mute_obj)
print("outside of mute obj and after function call",id(mute_obj))
print(mute_obj)

#wap calculate the sum of marks and avg marks

def cal(t,e,p,c,m,b):
    sum=t+e+p+c+m+b
    avg=sum/6
    return sum,avg
sum,avg=cal(90,95,89,67,75,80)
print(f"your sum value is {sum} and your average is{avg//1}")








