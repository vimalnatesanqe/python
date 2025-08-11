#two types of variable in functional programming approch
#local var
#global var

#local variable

#local variables are created in inside of the function
#we can not access this variable out side of the function

def loc_var():
    name="vimal" #this is a local varibale
    print(name)
loc_var()

#global variable
#global variable created out side of the function
#we can use this varibale any location

GLOBAL_VAR="Vimalathithan"

def acces_globl_var():
    print(GLOBAL_VAR)
acces_globl_var()
print(GLOBAL_VAR)

##create a global variable inside of the function
#using global keyword we can achive this
#once it is defied we can use this variable through out the program

def cte_gl_var():
    name="vimal"
    global last_name
    last_name="natesan"
    print(name+"  "+last_name)
cte_gl_var()
print(last_name)

#if you want to modify the global value inside of the function then use global keyword

glob_var="vimal"
print(glob_var)
def glob_update():
    global glob_var
    glob_var="vimalathithan"
    print(glob_var+" "+last_name)
glob_update()
print(glob_var)

#when global and local var name are same in that time we have to use global function

name="vimalathithan"

def glob_fun():
    name="ram"
    print(name)
    print(globals().get(name))

glob_fun()


