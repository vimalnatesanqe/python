#missing topic

#bytes and byte array

#byte conversion
# it is always allow (0-255)

new_list=[1,2,3,4,5]
conversion=bytes(new_list)
print(conversion[0])
print(conversion[::])
'''drawback-it will allow only numeric 0-255 range, we cannot modify the values
list1=[1,2,3,"vimal"]
con2=bytes(list1)
print(con2[1])'''

# byte array we can modify and it is hold 0-255 values only

list3=[1,2,3,4,5,6,254]
conv=bytearray(list3)
print(conv[4])
conv[5]=255
for i in conv:
    print(i,sep=" ",end='*')

### RNAGE

x=range(10)
print(x)
print(range(1,10))
print(range(1,100,2))
print(list(range(1,1000,3)))

for i in range(1,100):
    print(i)

for i in range(1,100,2):
    print(i)