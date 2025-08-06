my_name="****       vimalathithan        "
my_age=36
my_location='''2/64 mariyamman kovil street
sellappampatty(po)
Namakkal (dt)
pin=637019
9952350445
'''
my_company="nalla's software sollution pvt ltd"
my_salary=50000.00

# print(my_name.capitalize(),my_age,my_company.casefold(),my_salary,sep='--')
# print(my_location.upper())
# print(type(my_location))
# print(type(my_salary))

# x=my_location.split()
# for i in x:
#     if i.isnumeric():
#         print(f"hey {i.center(100,"*")} this is numeric values")
#     else:
#         print(i.center(100,'*'), end='😁😁😁😁\n')

# print(my_company.center(100,"*"))


# strip() -- removing space-default
# split()- split the word  based on the - 
# center()-allign
# is fun-checking alpha numeric -return true or false

sentence = "Python is powerful"

print(sentence.find("is"))       # 7 (returns -1 if not found)
print(sentence.rfind("p"))       # 10 (last occurrence)
print(sentence.index("is"))      # 7 (raises ValueError if not found)
print(sentence.rindex("p")) 
