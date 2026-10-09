# no parameter no return value
class calc:
    def __init__ (self):
        self.brand="casio"
        self.color="black"
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
c1=calc()
print(c1.brand)
print(c1.color)
c1.add()

# no parameter with return value
class calc:
    def __init__ (self):
        self.brand="casio"
        self.color="black"
    def add(self):
        a=10
        b=20
        c=a+b
        return(c)
c1=calc()
print(c1.brand)
print(c1.color)
res=c1.add()
print(res)

#with parameter no return value
class calc:
    def __init__ (self):
        self.brand="casio"
        self.color="black"
    def add(self,a,b):
        c=a+b
        print(c)
c1=calc ()
print(c1.brand)
print(c1.color)
x=10
y=20
c1.add(x,y)

#with parameter with return value
class calc:
    def __init__ (self):
        self.brand="casio"
        self.color="black"
    def add(self,a,b):
        c=a+b
        return c
c1=calc()
print(c1.brand)
print(c1.color)
x=10
y=20
c1.add(x,y)
res=c1.add(x,y)
print(res)




