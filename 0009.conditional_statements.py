# there are three types conditional statments available
# 1. if
# 2.if and else
# 3.if and elif and else

#if statement alone
#while True:
user_mark=int(input("enter your mrak:: "))
if user_mark > 33:
    print("cong'ss you passed the exam".center(50,'-'))
if user_mark < 33:
    print("sorry you failed the exam".center(50,"*"))

#if else:
if user_mark >= 33:
    print("you passed the exam")
else:
    print("you failed the exam")

#if elif else

user_lucky_nbr=int(input("enter your lucky number(0-9)::"))
if user_lucky_nbr >0 and user_lucky_nbr <4:
    print(f"you choosed in between 0 to 4 and your number {user_lucky_nbr} is lucky number")
elif user_lucky_nbr >=4 and user_lucky_nbr <=8:
    print(f"you choosed in between 4 to 8 and your number {user_lucky_nbr} is lucky number")
else:
    print("your number not in our lucky list")





