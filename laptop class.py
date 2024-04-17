class laptop: # this is the class
    price = 0
    processor = ""
    ram = ""

hp = laptop() #hp is the variable so athula assign pannrathu(athavthu laptop nu) ellathiyum sethu object sollalam
Dell = laptop() # this is the object it is used to acess the class.

hp.price = 50000
hp.processor = "i5"
hp.ram = "8gp"

Dell.price = 60000
Dell.processor = "i7"
Dell.ram = "16gp"

print(hp.price)
print(Dell.price)
