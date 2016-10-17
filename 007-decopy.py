import copy


class Pizza(object):
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def getPizzaInfo(self):
        return self.name, self.size, self.price

    def showPizzaInfo(self):
        print "Pizza name:" + self.name
        print "Pizza size:" + str(self.size)
        print "Pizza price:" + str(self.price)

    def changeSize(self, size):
        self.size = size

    def changePrice(self, price):
        self.price = price


class Order(object):
    def __init__(self, name):
        self.customername = name
        self.pizzaList = []
        self.pizzaList.append(Pizza("Mushroom", 12, 30))

    def ordermore(self, pizza):
        self.pizzaList.append(pizza)

    def changeName(self, name):
        self.customername = name

    def getorderdetail(self):
        print "customer name:" + self.customername
        for i in self.pizzaList:
            i.showPizzaInfo()

    def getPizza(self, number):
        return self.pizzaList[number]
customer1 = Order("zhang")
customer1.ordermore(Pizza("seafood", 9, 40))
customer1.ordermore(Pizza("fruit", 12, 35))
print "customer1 order infomation:"
customer1.getorderdetail()
print "-------------------------------"


customer2 = copy.deepcopy(customer1)
print "order 2 customer name:" + customer2.customername
customer2.changeName("li")
customer2.getPizza(2).changeSize(9)
customer2.getPizza(2).changePrice(30)
print "customer2 order infomation:"
customer2.getorderdetail()
print "-------------------------------------"

print "customer1 order information:"
customer1.getorderdetail()
