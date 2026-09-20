#Task01   Comments in python

x =1
# The initial value of x is 1.
"""The initial value of x is 1.
   The initial value of x is 1"""
if x>0:
    print("These are two comments") #print a string

y = input("Enter a number: ")
print(y)    


#Task02   Multiple statements on single line

print("First entity")
print("Second entity")
# we can also write these statements on a single line
print("First entity"); print("Second entity")


#Task03   Indentation

x=1
if x>0:
#print("This statement has no indentation") #no indentation error
  print("This statement has double space indentation")

x=1
if x>0:  
    print("This statement has a single tab indentation")

x=1
if x>0:    
     print("This statement has a single space+tab indentation")


#Task04   Data types and Type casting

a = 1223
print(type(a))   #output <class 'int'>
b = (-123)
print(type(b))   #output <class 'int'>
c = 1.54
print(type(c))   #output <class 'float'>
d = -23.44
print(type(d))   #output <class 'float'>
e = .45
print(type(e))   #output <class 'float'>
f = 3.12e-10
print(type(f))   #output <class 'float'>
g = 5E330
print(type(g))   #output <class 'float'>
x = True
print(type(x))
y = False
print(type(y))


#Task05    Strings

str1 = "String" #string start and end with double quotes
print(str1)
str2 = 'String' #string start and end with single quotes
print(str2)

# str3 = "String' #syntax error 
# str4 = 'String" #syntax error 

str5 = "Day's"  
print(str5)
str6 = 'Day"s'
print(str6)


#Task06    Special characters in strings

print("This is a tab \t key")
print("This is are \' single quote \'")
print("This is are \" double quotes \"")
print("This is a new line\nNew line")


#Task07    String indices & accessing & slicing string

string1 = "PYTHON TUTORIAL"
print(string1[0])     #print first character
print(string1[-15])   #print first character
print(string1[14])    #print last character
print(string1[-1])    #print last character
print(string1[2])     #print third character
print(string1[-13])   #print third character
print(string1[17])    #Out of index range


#Task08    Lists

mylist1 = [4,3,34,66] #list contains all integers values
print(mylist1)
mylist2 = ['red','blue','green'] #list contains all string values
print(mylist2)
mylist3 = ['red', 34, 34.22] #list contains a string, an integer and a float values
print(mylist3)


#Task09    List indices

mylist = []
print(mylist)
color_list = ['red','green','blue','Orange']
print(color_list[0]) #print first element
print(color_list[-3]) #print first element
#print(color_list[8])  #The index is out of range


#Task10   List slicing and conditional statements

print(color_list[0:2])  #cut first two items
print(color_list[1:2])  #cut second item
print(color_list[:3])   #cut first three items
print(color_list[:])    #creates copy of original list



