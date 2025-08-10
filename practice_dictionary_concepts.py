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

