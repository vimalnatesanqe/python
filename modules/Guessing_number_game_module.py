import random

user_value=int(input("guess a number 1 to 10:: "))
count=0
def guess_nbr():
    while True:
        system_value=random.randint(1,10)
        global count
        count+=1
        if user_value==system_value:
            print("conguratilations you won the game")
        else:
            print("sorry!!! you lost the game")
            print(f"here your value is {user_value} and our value is {system_value}")
            choice()
def choice():
    choice=input("do you want to play the game again y/n:: ")
    if choice=='y':
        global user_value
        user_value=int(input("guess a number 1 to 10:: "))
        guess_nbr()
    else:
        print("thanks for playing")
        print(f"you played this game {count} times")

guess_nbr()
