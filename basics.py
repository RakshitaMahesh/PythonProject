class Fan:
    def __init__(self):
        self.brand="usha"
        self.cost=1500
        self.color="black"
        self.wings=3
    def on(self):
        print("Fan is on")
    def rotate(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is off")
f1=Fan()
print(f1.brand)
print(f1.cost)
print(f1.color)
print(f1.wings)
f1.on()
f1.rotate()
f1.off()


a=10
b=10
c=10
d=20
print(id(a))
print(id(b))
print(id(c))
print(id(d))