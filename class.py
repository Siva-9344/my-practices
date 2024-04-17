class goa: # this is the class
    drink = ""
    name = ""
    def party(self): # this is the function
        print("Lets party.....")

    def beach(self):
        print("Enjoying the beach")

ramesh = goa() # ramesh is the object, object is the key to access the class.
suresh = goa() # sursh is the object, object is the key to access the class.

ramesh.name = "Ramesh"
suresh.name = "suresh"

ramesh.drink = "yes"
suresh.drinks = "No"




print(ramesh.name)
ramesh.party() # call the party function.
print("drink: ",ramesh.drink)


print(suresh.name)
suresh.beach() # this is call the function of beach.
print("drink: ",suresh.drinks)
