#while loop is working based on the condition
#if the condition is true it will run the block of code untill fail.

a=0 #start value
while a<=100: #condition
    print (a,"vimal")
    a+=2 #step value

#if the condition fails then it will stop

#infinite loop with control statements --break

#loop with break
while True:
    print("vimal")
    user_input=input("enter your input value else exit")
    if user_input=='exit':
        break
#loop with continue
a=0 
while a<5:
    a+=1
    if a==2:
        continue
    print(a)

#while with else
a=True
count=0
sum=0
while a:
    print("vimal")
    u_i=int(input("enter if you want to exit"))

    if u_i<=0:
        a=False
    elif u_i>0:
        count +=1
        sum +=u_i

else:
    print("else block is exceuted")
    print(f"your total enterd time{count} and sum of the number is {sum}")

#nested while loop


a=1
while a<=10:
    b=1
    while b<=a:
        print("*",end=' ')
        b+=1
    print()
    a+=1


    
   


