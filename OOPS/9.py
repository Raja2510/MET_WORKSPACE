from abc import ABC ,abstractmethod

 # inherating abstract module
    #cant initialize abstract class 
    # it must have base class implementing it
    # abstract classs excepts init intilized fully#
    # abstract methodcant initilaze abstracr class with out impllementing method

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def move(self):
        pass
class dog(animal):
    def sound(self):
        return "bark"
    

a=dog()
print(a.sound())








































#class Book(ABC):
#     def __init__(self, name, stock, id):
#         self.id = id
#         self.name = name
#         self.stock = stock
#     @abstractmethod
#     def read_name(self):# abstract methodcant initilaze abstracr class with out impllementing method
#         return self.name
# class Atomicstructure(Book):
    
#     def read_name(self):
#         print("working")


# book_1 =Atomicstructure()
# book_1.read_name()