#merging collection means concat one to another list
# there two ways we can achive

#list merging

l1=list(range(1,11))
l2=list(range(11,21))
#concat by + operator
l3=l1+l2
print(l3)
#concat another way
l4=[*l1,*l2]
print(l4)

#tuple merging

t1=tuple(range(1,11))
t2=tuple(range(11,21))
t3=t1+t2
print(t3)
#concat another way
t4=(*t1,*t2)
print(t4)

#set merging

s1=set(range(1,11))
s2=set(range(11,21))
 # we canot use +
 # we can use only * method
s3={*s2,*s1}
print(s3)

#dict merging

d1={i:i*i for i in range (1,11)}
d2={j:j*j for j in range (11,21)}

# use ** insted of *
d3={*d1,*d2} # only return key values
print(d3)
d4={**d1,**d2}
print(d4)
