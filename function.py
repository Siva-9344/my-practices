values = [2,3,4,5,6,7,8,9]

print(min(values))  # build in function

print(max(values))
print(sum(values))
print(len(values))

#---------------------------------------------------------------------

# user defined functions

def demo():
    print("good morning")

demo()    #----> call the function


#-----------------------------------------------------------------------

# function without arguments and without return type

#function definition
def add():
    a = 5
    b = 6
    c = a+b
    print(c)

#function call
add()

# another eg:

def adds():
    a = int(input("Enter the value: "))
    b = int(input("Enter the value: "))
    c = (a+b)
    print(c)
adds()

#------------------------------------------------------------------------
# function with argument and without return type:

def add(a,b):
    c = (a+b)
    print(c)

add(2,3) # (i think that (2,3) arguments)

# another eg:---------

def adds (a,b):
    c = a+b
    print(c)

a1 = int(input("Enter the value a1: "))
b1 = int(input("Enter the value b1: "))
add(a1,b1)

#-------------------------------------------------------------------------

# function without arguments and with return type:

def add():
    a = 2
    b = 10
    c = a+b
    return c
print(add())

# another eg:

def add():
    a = int(input("Enter the a value: "))
    b = int(input("Enter the b value: "))

    c = a+b
    return c
print(add())

#-------------------------------------------------------------------------

# function with argument and with return type:

def add (b,c):
    d = b+c
    return d
print(add(10,10))

# another eg:

def add(b1,c1):
    d1 = b1+c1
    return d1
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
print(add(b,c))

   
    







