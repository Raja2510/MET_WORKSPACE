# Inheritence:  
 


class Vehicle:

    def __init__(self):

        pass

    def start(self):

        print("Vehicle started")
 
class Car(Vehicle):

    def __init__(self, price):

        self.price = price

    def start(self):

        print("car started..")

class Ferrari(Car):

    def __init__(self, price):

        self.price = price

        super().__init__(price * 2)

    def start(self):

        print("Close ur ears..")


fr = Ferrari(3)

print(fr.start())


 