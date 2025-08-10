#wap to display repeted char count in a string

user_string=input("enter your string values")
my_dict={}

for i in user_string:
    my_dict[i]=my_dict.get(i,0)+1
else: 
    sum=0   
    for key,value in my_dict.items():
        print(f"{key} is presented and it count id {value}")
        sum+=value
    else:
        print("the total count is ::",sum)

#wap take two inputs from user 

couple_dict={}
while True:
    boy_name=input("enter boy friend name:: ")
    girl_name=input("enter girl name:: ")
    couple_dict[boy_name]=girl_name
    choice=input("do you want to add more y/n::")
    if choice=='n':
        break
while True:
    get_name=input("enter your boy fried name:::")
    gf_name=couple_dict.get(get_name,"no boy friend name available")
    print(f"hey {get_name} your girl fried name is {gf_name}")
    choice=input("do you want to add more y/n::")
    if choice=='n':
        break

#iterating nested list

students={
    101:{'name':"vimal",'email':"abc@gmail.com",'address':'nkl'},
    102:{'name':"kimal",'email':"abc@gmail.com",'address':'nkl'},
    103:{'name':"jimal",'address':'nkl'}
}

for s_id, value in students.items():
    print(f"student id is {s_id}")
    for personal in value:
        print(f"{personal}:{value.get(personal,'no value')}")
    print("*"*30)
    