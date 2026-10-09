from gettext import c2py
from zlib import crc32


class clac:
    def __init__(self):
        self.brand="casio"
        self.color=("black")
    def add(self,a,b):
        c=a+b
        return c
    def sub(self,a,b):
        c=a-b
        return c
    def mult(self,a,b):
        c=a*b
        return c
    def div(self,a,b):
        c=a/b
        return c
c1=clac()
print(c1.brand)
print(c1.color)
x=20
y=10
res1=c1.add(x,y)
print(res1)
res2=c1.mult(x,y)
print(res2)
res3=c1.div(x,y)
print(res3)
res4=c1.sub(x,y)
print(res4)


class calc():
    def operations(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4
c1=calc()
x=5
y=2
r1,r2,r3,r4=c1.operations(x,y)
print(r1)
print(r2)
print(r3)
print(r4)






