# arguments
# default arguments


# function dfinition:

def details(name = "Arun",age = 23):
    print("Name: ",name)
    print("Age: ", age)
details()

#-------------
# another type:


def details (id,name = "siva", age = 23):
    print("Name: ",name)
    print("Age: ",age)
    print("id: ",id)
details(101)

#------------
# another type:

def details (id,name,age):
    print("name: ", name)
    print("Age: ", age)
    print("id",id)

details(12,"siva",3)    

