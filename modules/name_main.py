#__name__ is special varibale
#using of this special varibal we can check the program excuted directilly or indirectly
#if it is direct excecuton then it will print main else it will retume module name
# ihave creted another file for this practice

#checking main file excecution

def add(a,b):
    print(a+b)



#o/p
'''_main__
Traceback (most recent call last):'''

#this file is called by directly so it is return main excecution

# if you want to run this file only direct excecution then set condition for that

if __name__== '__main__':
    print(__name__)




