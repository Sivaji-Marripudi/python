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
