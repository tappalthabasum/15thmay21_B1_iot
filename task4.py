class Mystr:
    
    def__init__(self,var):
        self.var = var
    def__sub__(self,other):
        for i in other.var:
            if i in self.var:
                b = (self.var).find(i)
self.var = self.var[0:b]+self.var[b+1:]
print(self.var)

d = Mystr(input('first string:' ))
e = Mystr(input('second string:'))
f = d-e
print(f)
