class C1:

    a = 20
   def amethod(self):
       print("~~~~",C1.x)
       print(C1.__var)

   # def bmethod(int a, list blist):
       # print(a,"~~",blist)


print(C1.__var)


print(C1.x)
#C1.amethod()
# print(C1.__var)  -- implicitly a private variable at the class level
# _var2 -- variable with a single


class C2:
    def __init__(self,n):
        self.x = n



c2_instance = C2(35)
print("X =",c2_instance.x)

class C3:
    a = None
    b = None
    c = None


c3i = C3()
c3i.a = 20
c3i.b = 30
c3i.c = 40

print(c3i.a,c3i.b,c3i.c)
c3i.__dict__['c'] = 47
print(c3i.a,c3i.b,c3i.c)


class Singleton:
    _singletons = {}
    def __new__(cls, *args, **kwds):
        if cls not in cls._singletons:
            cls._singletons[cls] = obj = super().__new__(cls)
            obj._initialized = False
        return cls._singletons[cls]
