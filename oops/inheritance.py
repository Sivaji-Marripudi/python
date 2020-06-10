# Inheritance 
class employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
class childemployee(employee):
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
e1 = employee("sivaji",21,300000)
e2 = childemployee("pavan",20,463)
print(e1.__dict__)
print(e2.__dict__)

# MULTILEVEL Inheritance
class employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
class child1(employee):
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
class child2(child1):
    def __init__(self,name,age,salary,id):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id
        #self.city = city
e1 = child1("sivaji",21,5000000,123)
e2 = child2("pavan",22,300000,462)
e3 = employee("shabari",22,30000)
print(e3.__dict__)
print(e2.__dict__)
print(e1.__dict__)
