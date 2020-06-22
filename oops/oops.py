class persons:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
    def func1(self):
        return '{} from {}'.format(self.name,self.city)
p1 = persons('sivaji',22,'bangalore')
p2 = persons('ram',22,'bangalore')
print(p1.func1())
print(p2.func1())