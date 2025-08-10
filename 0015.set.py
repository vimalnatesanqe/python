#set is mutable type
#it will wont duplicates
#it is un ordered
#we cannot do idex and slicing

#empty set

e_set=set()
print(type(e_set))

#set with diffrent values

my_set={1,2,3,4,5,7}
print(my_set)
print(type(my_set))

#set creation by list

list1=[2,4,6,7]
my_set=set(list1)
print(my_set)
#set creation by tuple
my_tup=1,2,3,4,5
my_set=set(my_tup)
print(my_set)
#set creation by range
my_set=set(range(1,100))
print(my_set)


#set add, update concepts
#we can not do indexing

my_set=set(range(1,10,2))
s_add=my_set.add(11) # we can add only single element
print(my_set)
m_update=my_set.update((11,12,34),[233,334,445],range(1,20)) #adding iter obejects only
print(my_set)

#remove
my_set.remove(233) #if value is not find then i will rise value not found error
print(my_set)
#discard # it will not throw the error
my_set.discard(234)
print(my_set)

#set important functions
#union
#intersection
#diffrence
#symetric diff
#is subset
#is super ser
#dis join

set_a=set(i for i in range(1,100) if i%2==0)
set_b=set(i for i in range(1,100) if i%5==0)

print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))
print(set_a.isdisjoint(set_b))