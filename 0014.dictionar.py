#dictionary is key value pair
#key is immutable and value is mutable and allow duplication
#index concept is not working

#empty dictinary

# empt_dict={}
# print(type(empt_dict))

# creatinh dictionary by dict constructor
empt_dict= dict(())
print(empt_dict)

#normal declare dictionary

my_dict={'name':'vimalathithan',
         'age':36,
         'location':'namakkal',
         'contact':9952350445}

#Accesing dictionary
print(my_dict['name']) ##passing key instead of index

#another way get method
print(my_dict.get('name')) ##get method not throw error while key is not available but others it will throw

#update values by key
print(
my_dict['name'])
my_dict['name']='vimal'
print(my_dict['name']) #updated 

#update using update method
my_dict.update({'name':'aathi','age':38}) # update multiple values at the same time
print(my_dict)

#inbuild functions

print(my_dict.keys()) #return only keys
print(my_dict.values()) #return only values
print(my_dict.items()) #return both key and values

#dictionary traversing

for key in my_dict:
    print(key)
for key in my_dict.keys(): #both are return the same result
    print(key)

for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(f"key is {key} and value is {value}")

#removing by pop and pop tem

print(my_dict.pop('name'))#it will remove the specific key value
print(my_dict)

print(my_dict.popitem())# it will remove the end of the key value pair
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
print(my_dict)