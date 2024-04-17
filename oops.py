# OOPS or function
class computer:
    def config (self):
        print("i5","16gb","1Tb")

com1 = computer()
com2 = computer()

computer.config(com1)
computer.config(com2)

com1.config() # this is the the easy for the print output
com2.config()

#-------------------------------------------

'''class computer:
    def config(self,cpu,ram):
        print(cpu,ram)

com1 = computer() # object creation



com1.config("8gp",6)'''

# constructor,self and comparing objects in python
#oops concepts(object,clss,init)

class computer:
    def config(self):
        print("5gb")
        
com1 = computer() #==> constructor is used to allocate the memory 
com2 = computer()
print(id(com1)) # this id is used to find data store location
print(id(com2))
com1.config()



        
