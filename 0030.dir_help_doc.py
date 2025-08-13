# using dir function we can know about memberes information inside of module

#using help function we can know about members detatils and description

import modules

print(dir(modules))

#o/p ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__', 'add', 'age', 'div', 'flor_div', 
# 'location', 'mul', 'name', 'pi', 'squire', 'sub']

print(help(modules))

'''o/p= NAME
    modules

DESCRIPTION
    #collection of class,variable and functions called modules
    #every .py file as a module

o/p==FUNCTIONS
    add(a, b)
        addition of two nbrs

    div(a, b)
        division of two nbrs

    flor_div(a, b)
        floor divi of two nbrs

    mul(a, b)
        multiplication of two nbrs

    squire(a)
        squire of two nbrs

    sub(a, b)
        subtraction of two nbrs

DATA
    age = 37
    location = 'coimbatore'
    name = 'vimal'
    pi = 3.14'''


print(print.__doc__)