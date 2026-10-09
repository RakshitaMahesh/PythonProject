#ways to declare instance variables
class book:
    def __init__ (self) :
        self.name="doms"
        self.cost=60
    def help(self):
        print("raksh reads book")
        self.color="black"
b1=book()
print(b1.name)
print(b1.cost)
b1.help()
print(b1.color)
b1.nop=200
print(b1.nop)

