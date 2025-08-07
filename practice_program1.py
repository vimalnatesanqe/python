#check nbr positive or negative or zero

user_value=int(input("enter your value:: "))
if user_value>0:
    print(f"hey user you entered positive value, the value is {user_value}")
elif user_value<0:
     print(f"hey user you entered negative value, the value is {user_value}")
else:
     print(f"hey user you entered zero value, the value is {user_value}")


#check odd or even

if user_value %2==0:
    print(f"your number {user_value} is even number")
else:
    print(f"your number {user_value} is odd number")

#which one is gratter

a=int(input("enter your a value:: "))
b=int(input("enter your b value:: "))
c=int(input("enter your c value:: "))

if a>b and a>c:
    print("a is gratter than b and c")
elif b>a and b>c:
    print("b is gratter than a and c")
else:
    print("b is gratter than a and c")
    
#calculate the values based on the user input option(sum or multiply)

user_input=int(input("enter your a value:: "))
user_input1=int(input("enter your b value::"))
user_oppinon=input("enter your oppinion (addition,sub,mul,divi)")

if user_oppinon=='add':
    print(f"here you addion value is {user_input+user_input1}")
elif user_oppinon=='sub':
    print(f"here you addion value is {user_input-user_input1}")
elif user_oppinon=='mul':
    print(f"here you addion value is {user_input*user_input1}")
elif user_oppinon=='div':
    print(f"here you addion value is {user_input//user_input1}")
else:
    print("please choose correct input values")

           
