#python has inbuiild data structure
#1.list
#2.tuple
#3.set - frozen set
#dictionary

#########################
#LIST
########################
# 1.list is mutable
# 2.it is orederd
# 3.allow duplicates 

#list creation

#empty list

empty_list=[]
empty_list1=list()

print(empty_list)
print(empty_list1)
print(id(empty_list))
print(id(empty_list1))
##########
b=empty_list
print(id(empty_list))
print(id(b))
#########

mixed_list=[1,True,2.0,"Vimal",[1,2,3,5],(6,7)]

#Accessing by index
print(mixed_list[0])
print(mixed_list[-1])
print(mixed_list[4][2])
print(mixed_list[5][1])
#modifyning by index
mixed_list[4][2]=100
#mixed_list[5][0]=200 --this is failed because tuple obj cant modify it it immutable
print(mixed_list)

#accessing by slicing method

print(mixed_list[:])
print(mixed_list[::-1])
print(mixed_list[2:len(mixed_list):2])

#accesing by for loop
#only value
print("list traversing".center(50,"*"))
for l_value in mixed_list:
    print(l_value)
print("list traverse by range using len".center(50,'*'))
#by range
for l_value in range(len(mixed_list)):
    print(mixed_list[l_value])

#by enumerate - index creation and value
for l_index,l_value in enumerate(mixed_list):
    print(f"index is {l_index} and value is {l_value}")

normal_list=list([1,2,3,4,5,6,7,8,9])
#concat two list
concat_list=mixed_list + normal_list
print(concat_list)

#by zip traverse two list paralel processes

for m_li,n_li in zip(mixed_list,normal_list):
    print(f"{m_li},and,{n_li}") 
########################################################
#list functions
########################################################

print(mixed_list)
print(normal_list)
print(len(mixed_list))
print(min(normal_list))
print(max(normal_list))
#########################################################
#list accessing function
temp_list=[1,2]
#adding new data
temp_list.append(3)     #it will add end of the list
print(temp_list)            
temp_list.insert(1,3)   #it will add by index value
print(temp_list)
print(temp_list.count(3)) #it will return no counts
print(temp_list.index(3))   #it will return index posiion no
temp_list.sort()
print(temp_list)
temp_list.sort(reverse=True)
print(temp_list)
temp_list1=[100,200,300]
temp_list.extend(temp_list1)
print(temp_list)

temp_list.pop()  # it will remove last element
print(temp_list)

temp_list.remove(100)# it will remove by value

print(temp_list)

temp_list.clear() #it will clear all the data

print(temp_list)

del temp_list #temp list will be delete

print(temp_list)