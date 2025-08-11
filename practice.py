# my_name="****       vimalathithan        "
# my_age=36
# my_location='''2/64 mariyamman kovil street
# sellappampatty(po)
# Namakkal (dt)
# pin=637019
# 9952350445
# '''
# my_company="nalla's software sollution pvt ltd"
# my_salary=50000.00

# # print(my_name.capitalize(),my_age,my_company.casefold(),my_salary,sep='--')
# # print(my_location.upper())
# # print(type(my_location))
# # print(type(my_salary))

# # x=my_location.split()
# # for i in x:
# #     if i.isnumeric():
# #         print(f"hey {i.center(100,"*")} this is numeric values")
# #     else:
# #         print(i.center(100,'*'), end='😁😁😁😁\n')

# # print(my_company.center(100,"*"))


# # strip() -- removing space-default
# # split()- split the word  based on the - 
# # center()-allign
# # is fun-checking alpha numeric -return true or false

# sentence = "Python is powerful"

# print(sentence.find("is"))       # 7 (returns -1 if not found)
# print(sentence.rfind("p"))       # 10 (last occurrence)
# print(sentence.index("is"))      # 7 (raises ValueError if not found)
# print(sentence.rindex("p")) 


# text = "banana"

# print(text.count("a"))          # 3
# print(text.count("na"))         # 2
# print(text.replace("a", "o"))   # "bonono"
# print(text.replace("na", "xy")) # "baxyxa"


# #split()
# #strip()
# #upper()
# #is
# #center()
# #count
# #replcae
# #find
# #index


# print("vimal".find('l'))
# print("vimal".replace('l','ll').replace('v','KK'))

# x="pal-lap"
# y=x.replace('-','')
# z=y[::-1]
# print(z)
# if y==z:
#     print("This is a palindrome")
# else:
#     print("This is not palindrome")

# lis=[1,2,3,4,5,6,7]


# lis_prac=[1,2,3,4,5,6,7,[[[1,2,3]]]]
# print(lis_prac[0])
# print(lis_prac[-1])
# print(lis_prac[-1][0][0][1])

# li1=[[[1,2]],[[3,4]],[[5,6]]]
# for i in li1:
#     print(i)
#     for j in i:
#         print(j)
#         for k in j:
#             print(k)
tup=(1,2,3,4,5,6,7,8,9)
# for i in tup:
#     print(i)
# tup1=((1,2),(3,4),(5,6))
# print(tup1[0])

# print(tup1[0][1])
# for i in tup1:
#     print(i)
#     for j in i:
#         print(j)

dict={
    101:{'name':"vimal",
    'age':36,
    'location':'nkl'},
    102:{
    'brand':'audi',
    'model':'2030',    
    'is_true':'yes'        
    }
}

for i,j in dict.items():
    for k in j:
        print(f"hey {k} {j.get(k)}")

#short hand if and comprehension

list1=list(range(1,11))
print('True' if 10 in list1 else 'false')
a=10
b=11
print(a if a<b else b)
print(list1)
x=[i if i%2==0 else 'odd' for i in list1]
print(x)

