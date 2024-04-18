class laptop:
    price = 0
    ram = ""
    def _init_(self):# _init_ is the constructor its mean(A constructor is a unique functon thata gets called automatically when an object is created of a class)
        print("demo") #but unfortunately this constructor is not working for me, workin on while calling the function 

    def display(self):
        print("display")
        
hp = laptop()

hp.price = 50000
hp.ram = "8gp"
hp.processor ="i5"

print(hp.processor)


