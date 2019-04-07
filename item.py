class Item(object):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    
    def ToString(self):
        str1="Name: "+self.name+"Price: "+str(self.price)
        return str1