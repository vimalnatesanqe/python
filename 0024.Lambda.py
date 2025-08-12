#lambda is a high order function
#labda can recive multiple aruguments but it will only return one value

#normal function adding two nbr

def add(a,b):
    return a+b
print(add(100,200))

#lambda function
fun=lambda a,b:a+b  
print(fun(100,200))

#we can write this code to one line
print((lambda a,b:a+b)(100,200))

#checking grater ot not
print((lambda a,b: a if a>b else b)(10,2))


ref=lambda:[i if i%2==0 else "odd_nbr" for i in range(1,100)]
print(ref())