#--------- Python Functions
# Creating a function
def my_function():
     print("Hello from function")

# calling a function
my_function()     

#parameters

def my_function(fname):
     print(fname + " Refsnes")

my_function("Email")
my_function("Broader")

#Default parameters

def my_function(country = "pakistan"): print("I am from "+ country)
my_function("Sweden")
my_function("US")
my_function()
my_function("bartania")

# passing a list as parameter

def my_function(food):
    for x in food:
        print(x)

food = ["apple","banana","cherry"]
my_function(food)        

# Return Values

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(6))
print(my_function(9))

# keyword arguments

def my_function(child3,child2,child1):
    print("The youngest child is " + child3)

my_function(child1="Emil",child2="Tobias",child3="Linus")  