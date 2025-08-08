#tuple is immutable, we cannot modify and update once it is created
#tuple is ordered
#we can access by through idex and slicing, for loop

#tuple creation

empty_tuple=tuple()
print(type(empty_tuple))
print(empty_tuple)

#single value tuple

single_value_tuple=(1,)  #, should be present after the value then only it is treated like tuple else it is treat like int val
print(single_value_tuple)

#mixed tuple

mixed_tuple=(1,True,[1,2,3],29.0,{'name':"Vimal",'age':36})
print(id(mixed_tuple))

#Accessing tuple

#by index
print(mixed_tuple[2])
print(mixed_tuple[-1])

#by slicing
print(mixed_tuple[:])
print(mixed_tuple[::-1])
print(mixed_tuple[2:len(mixed_tuple):2])

# we can update the tuple when it is hold mutable data
mixed_tuple[2].append(100)
print(mixed_tuple)

#by for loop

for values in mixed_tuple:
    print(values)

for index,values in enumerate(mixed_tuple):
    print(mixed_tuple[index])
    print(f"index is {index} and values is {values}")

#tuple functions
print(len(mixed_tuple))
print(mixed_tuple[2].count(2))