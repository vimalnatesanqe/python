#forward while

i=0
while i<=10:
    print(i, end=" ")
    i=i+1

#backward while

while i>=0:
    print(i,end=' ')
    i=i-1

#while break

while i<=10:
    if i==8:
        break
    print(i)
    i+=1

#continue:
print(i)
# while i>=0:
#     print(i)
#     if i==5:
#         continue
#     i-=1
# else:
#     print("else block excecuted")

#wap sum of naturla nbrs

sum=0
i=0
while i<=10:
    sum+=i
    i+=1
print("the total sum value is {} till{}".format(sum,i-1))

#wap get user input and sum the value and display the sum and no entries, if -1 enter progrram should stop

total=0
count=0
while True:
    user_input=int(input("enter your sum values::"))
    if user_input==-1:
        break
    total+=user_input
    count+=1
print("here your toal value is {} and no of entries is {}".format(total,count))

#count the values of posive,negative,zero

user_entry=int(input("enter your values"))
positive=0
negative=0
zero=0
while user_entry !=-1:
    if user_entry>0:
        positive+=1
    elif user_entry<0:
        negative+=1
    elif user_entry==0:
        zero+=1
    user_entry=int(input("enter your values"))

print("positivre count: {} negative count {} zero count {}".format(positive,negative,zero))

#multiplication table:

table=int(input("which table you want"))
i=1
while i<10:
    print(f"{i} * {table} = {i*table}")
    i+=1

