#inheritance
class cse:
    def __init__(self,a):#constructor
        self.a=a
    def fun(s):
        print("hello",s.a)
o=cse(2)
b=cse(5)
b.fun()
#------------------------------------
class cse:
    def fun1(s):
        print("fun1")
    
    def fun2(s):
        print("fun2")
class two:
    def fun3(self):
        cse.fun1(self)
        print("fun3")
        
    
    def fun4(s):
        print("fun4")
    
o=cse()
a=two()
a.fun3()
#----------------------------------------------------------
#polymorphism

class cse:
    def fun1(s):
        print("fun1")
    
    def fun2(s):
        print("fun2")
class two:
    def fun1(self):
        cse.fun1(self)
        print("fun3")
    
    def fun4(s):
        print("fun4")
    
o=cse()
o.fun1()
a=two()
a.fun1()

#----------------------------------------
class one:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
        
class two:
    
    def fun3(self):
        print("fun3")
    def fun4(s):
        print("fun4")
        
class three(one):
    
    def fun5(self):
        print("fun5")
    def fun6(s):
        print("fun6")
    
o=one()
o.fun1()
o.fun2()
a=two()
a.fun3()
a.fun4()
b=three()
b.fun5()
b.fun6()
#-----------------------------------------------------------
class one:
    def fun1(self):
        two.fun3(self)
        print("fun1")
    def fun2(self):
        
        #three.fun6(self)
        print("fun2")
        
class two:
    
    def fun3(self):
        #one.fun1(self)
        print("fun3")
    def fun4(s):
        #three.fun5(self)
        print("fun4")
        
class three(one):
    
    def fun5(self):
        #one.fun1(self)
        print("fun5")
    def fun6(s):
        
        #two.fun3(self)
        print("fun6")
    
o=one()
o.fun1()
o.fun2()
a=two()
a.fun3()
a.fun4()
b=three()
b.fun5()
b.fun6()


#------------------------------------------------
class cse:
    def fun1(s):
        print("fun1")
    
    def fun2(s):
        print("fun2")
class two(cse):
    def fun3(self):
        cse.fun1(self)
        print("fun3")
    
    def fun4(s):
        print("fun4")
    
b=cse()
b.fun1()
a=two()
a.fun3()
a.fun4()
#-----------------------------------------------------------------------
class cse:
    def fun1(s):
        print("fun1")
    
    def fun2(s):
        print("fun2")
class two(cse):
    def fun3(self):
        #super().fun1()
        print("fun3")
    
    def fun4(s):
        print("fun4")
    
b=cse()
b.fun1()
a=two()
a.fun1()
a.fun3()
a.fun4()

