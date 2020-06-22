class mango:
    def __init__(self):
        self.__maxprice = 100
    def sell(self):
        return ' price is {}'.format(self.__maxprice)
    def setprice(self,price):
        self.__maxprice = price
c = mango()
print(c.sell())
c._maxprice = 1000
print(c.sell())
c.setprice(10000)
print(c.sell())