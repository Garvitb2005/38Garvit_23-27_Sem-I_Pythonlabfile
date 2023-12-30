class Grandfather:             #parent class
    def __init__(self):
        self.name1 = 'Abc'
        self.P1 = 200
class Father(Grandfather):     #derived class have properties of Grandfather
    def __init__(self):
        self.name2 = 'Xy'
        super().__init__()     #it is used to access the Parent class method.
        self.P2 = 100
class Child(Father):           #derived class have properties of both Grandfather and Father
    def __init__(self):     
        self.name3 = 'child name'
        super().__init__()
obj1 = Grandfather()
obj2 = Father()
obj3 = Child()    
print("Assets of",obj3.name3,"are",obj1.P1+obj2.P2)