
#encapsulation-> data hiding , controlled access / protected data
# 
# # 
class AC:

    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        self.__serial_number="s1"# __ variable (double underscore) is protected / private variable
        self.access_member=[23,24,25]
    def get_serial_number(self,id):
        if id in self.access_member:
            return self.__serial_number
        else:
            return "you dont have "

ac2=AC("samsung","white")
print(ac2.color)
print(ac2.brand)
print(ac2.get_serial_number(id=23))





