class laptop:
    def _init_(self):
        self.ram = ""
        self.processor = ""
    def display(self):
        print("ram :",self.ram)
        print("processor :",self.processor)

hp = laptop()
hp.ram = "8gp"
hp.processor = "i5"

hp.display()
