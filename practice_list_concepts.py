#wap display the list values and index revrese

my_list=[1,2,3,4,5,6,7]
len_lst=len(my_list)
for i in range(len_lst):
    print(f"{my_list[i]} value present in / {i-len_lst}")
    print("*"*10)

#wap check your lucky nbr present in the list or not
while True:
    lucky_nbr=int(input("enter your lucky nbr:: "))
    lucky_list=[1,3,5,6,7,8]
    if lucky_nbr in lucky_list:
        print(f"your nbr {lucky_nbr} in our lucky-list")
        break
    else:
        print("your nbr not a lucky nbr")

# find the min value not using min

user_list=eval(input("enter your list values here:  "))
len_user_list=len(user_list)
min_value=[]
for tra in range(len_user_list):
    if min_value==[]:
        min_value.append(user_list[tra])
    elif min_value[0]>= user_list[tra]:
        min_value[0]=user_list[tra]
print(f"the min value is {min_value}")

#another way

user_list=eval(input("enter your list values here:  "))
min=user_list[0] #23
for i in user_list:
    if i<min:
        min=i
print(min)


#wap search a values from the list based user input and count no of times it is present

list1=[1,2,3,4,5,6,12,34,2,2,2,3,2,3,2,3,23,1,1,4,5,6,5,4,5]

user_input=int(input("enter your serach value"))
i=0
count=0
while i<len(list1):
    if user_input==list1[i]:
        print(f"{user_input} value is present in the idex of {i}")
        count+=1
    i+=1
print(f"{user_input} value is present in {count} times in this list")