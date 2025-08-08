# for loop used for iterate the values from sequence data type

#range with for

for i in range(10): #range(start,stop,step (default 0,10-1(9),default 21 increment))
    print(i, end=" ")
print()

for i in range(1,20,2): #forward step
    print(i, end=" ")
print()

for i in range(100,0,-10):
    print(i,end=" ")
print()

#using range iter fro list
s_list=[1,2,"Vimal",True,12.0]
print(len(s_list))
for i in range(len(s_list)-1,0,-1):
    print(s_list[i], end=" ")
print()
#FOR LOOP FOR STRING DATA TYPE

name="vimalathithan"
for i in name:
    print(i,end="^")
print()

for i in range(len(name)-1,0,-1):
    print(name[i])

#FOR LIST DATATYPE
s_list=[1,2,"Vimal",True,12.0]

for i in s_list:
    print(i)
print()
for i in ["vimal","aathi","natesan",36,48000.00]:
    print(i)
print()

#FOR tuple:

u_tup=(1,2,3,4,5,(2,3,4))

for i in u_tup:
    print(i)

#for loop dict

sample_dict={'name':"vimal",
             'l_name':"natesan"}
for i in sample_dict:
    print(i)
for i in sample_dict.values():
    print(i)
for i,j in enumerate(sample_dict.values()):
    print(i,j)

#enumerate

sam_list=["vimalathithan","natesan","namakkal",637019]

for index,addr in enumerate(sam_list):
    print(f"{index}::{addr}")

for index,addr in enumerate(sam_list,start=100):
    print(f"{index}::{addr}")

#zip -- combine two or more list 

fam_list=["vaishnavi","chellamuthu","vellakovil",637001]

for my_fam,dev_fam in zip(sam_list,fam_list):
    print(f"{my_fam}::::{dev_fam}")

#nested for loop

for i in range(10):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(3):
    print(i, "vimal")
    for j in range(3,6):
        print("this is inner loop")
    print()