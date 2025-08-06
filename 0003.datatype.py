# there are diffrent data type available in python
"""
1. buid in data type
2. user defined data type

1. build in data type

1. numeric:
    1.int
    2.float
    3.complex
2. boolean
    1.True
    2.False
3. sequence
    1.str
    2.list
    3.tuple
    4.set
4. Mapping
    1.dictionary
5. None
6.Binary
"""
# binary data type -0,1
#decimal data type - 0-9
# octal data type - 0-7
# hexadecimal data type - 0-9, A-F

#type conversion
#decimal to binary


def dec_to_bin(x):
    bin_value=bin(x)
    oct_value=oct(x)    
    hex_value=hex(x)
    print(bin_value)
    print(oct_value)
    print(hex_value)
dec_to_bin(15)

#int
import math
a=10
print(type(a))
print(float(a))
print(type(a))
b=10.6
print(int(round(b)))
print(int(math.floor(b)))
print(int(math.ceil(b)))

#boolean
""" True mean 1 and false mean 0"""
print(True+True+False)
print(True*True*False)
a=100
b=200
result=a>b
print(result)