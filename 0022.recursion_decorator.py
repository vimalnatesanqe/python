# a function call by it self it is called recursion
# recustion do a task untill the condition failed
#recusion alwyays shold have terminatin condition if it is not then i will act as infinte loop

#example 1

# def recur():
#     '''this is recursion function example'''
#     #here there is no termination conditin so it is treat as infinite
#     print("vimal")
#     recur() #function call by it self

# recur()# function call

#example 2 "with condition"

#forward

def recur_e1(num):
    if num==6:
        return
    else:
        print(num)
        recur_e1(num+1) # recurson tail approch 
recur_e1(1)

#backwrd
def recur_e1(num):
    if num==6:
        return
    else:
        recur_e1(num+1) #recursion head approch
        print(num)
recur_e1(1)

#start pattern

def rec_star(num):
    '''star 1 to 10 pattern'''
    if num==10:
        return
    else:
        print("*"*num)
        rec_star(num+1)
rec_star(1)

#star patern reverse order

def rec_star(num):
    '''start 10 to 1 pattern'''
    if num==10:
        return
    else:
        rec_star(num+1)
        print("*"*num)
rec_star(1)


#find sum of natural numbers using recusion

def recu_sum(num):
    if num==1:
        return num
    return num+recu_sum(num-1)
recu_sum(10)
print(recu_sum(10))

#factorial number

def rec_fact(num):
    if num==1:
        return 1
    return num*rec_fact(num-1)
print(rec_fact(5))


#recursion types:
#1.direct Recursion
#2.indirect recurion
#3.head
#4.tail

#direct recursion
#recusion function calling happened inside the same the function

def direct_recur(num):
    if num==0:
        return
    else:
        print(num)
        direct_recur(num-1)  #this is called inside of the func directly

#indirect recrusion
#function calling happened another function in directly

#example
def indir_recur(num):
    if num<=6:
        print(f"this is recur::=={num*num}")
        indir_recur1(num+1)
    return num
def indir_recur1(num):
    if num<=10:
        print(f"this is recur1::=={num**num}")
        indir_recur(num+1)
    return num
x=indir_recur(1)
print(x)

#tail recurion there is no action after function call
#non_tail recur after the function call additional opreations happen then it it non tail recursions
    
    

