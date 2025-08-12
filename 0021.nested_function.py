# # a function wiritten inside of another function called nested function

# #Example1:

# def outerfun():
#     print("this is outer function")
#     def innerfun():
#         print("this is inner function")
#     innerfun()
# outerfun()
# #innerfun() -- we cannnot call inner function out side

# #Example2
# def outerfun1(a,b):
#     print(a+b)
#     def innerfun1(a,b):
#         print(a+b)
#     in_fun=innerfun1
#     in_fun(20,20)
# out_fun=outerfun1
# out_fun(10,10)

# #Example 3
# #A function returning another function
# #here we can aceess the inner function from outside 

# def out():
#     print("this is outer")
#     def inn():
#         print("this is inner")
#     return inn
# ref=out()
# ref()

# #example 4

# def fn1(abc):
#     return abc
# def fn2(a):
#     print(a)
# ref=fn1(fn2)
# ref("vimal")

# #a function calling by inself it is called recursion
# # def fn1():
# #     print("vimal")
# #     fn1()
# # fn1()

#decarotor


def outr(fun):
    def warp(a,b):
        if a<b:
            a,b=b,a
        fun(a,b)
    return warp

@outr
def div (a,b):
    c=a//b
    print(f"value swapped:: and performed divison function",c)

div(3,99)
