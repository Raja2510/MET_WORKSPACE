class Ac:
    # temp=0
    # brand="samsung"
    # color="white"

    def __init__(self,brand):
        self.brand=brand
    def turn_on(self):
        print(f"{self.brand} Ac is turned on")
    def turn_off(self):
        print("Ac is turned off")
    def change_temp(self):
        pass


# ac=Ac("samsung") #ac is instance if Ac class
# print(ac.brand)
# # ac.turn_on()
# my_list=[Ac("samsung"),Ac("sonic"),Ac("Lg")]
# print(my_list)
# for ac in my_list:
#     ac.turn_on()

class light:
    def __init__(self,brand):
        self.brand=brand
    def turnon(self):
        print(f"{self.brand} light is turned on" )
class room:
    def __init__(self,ac,lit):
        self.temp=24
        self.ac=ac
        self.lit=lit

ac=Ac("samsung")

lit=[light("lg"), light("philps"), light("led")]
rom=room(ac,lit)
  
rom.ac.turn_on()

for l in rom.lit:
    l.turnon()