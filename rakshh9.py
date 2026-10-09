class farmer:
    def __init__(self,principal, time,intrest):
        self.principal = principal
        self.time = time
        self.intrest = intrest
    def loan(self):
        si=self.principal*self.time*self.intrest/100
        print(si)

f1=farmer(300000,3,2.5)
f2=farmer(100000,1,2.5)
f1.loan()
f2.loan()


class farmer:
    r=2.5
    def __init__(self,principal, time):
        self.principal = principal
        self.time = time
    def loan(self):
        si=self.principal*self.time*farmer.r/100
        print(si)

f1=farmer(300000,3)
f2=farmer(100000,1)
f1.loan()
f2.loan()
print(farmer.r)






