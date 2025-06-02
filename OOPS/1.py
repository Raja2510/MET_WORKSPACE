# 1indentify objects in your system
#2 identify properties of each object
#3 identify action of each object 
#4 assmble objects in a system

### -- objects here Ac, light, Desk, fan shutter--------
#       Ac- temp , brand , color , capacity
#   light- watt color , brand shape
#  desk height color is_wheeled
# 
# #


class Ac:
    temp=0
    brand="samsung"
    color="white"
    capacity=4 #tons        
        
    def turn_on(self):
        print("Ac is turned on")
    def turn_off(self):
        print("Ac is turned off")
    def change_temp(self):
        pass

class light:
    watt=30
    color="white"
    brand="lg"
    shape="tube"
    def turn_on(self):
        print("lights are turned on")
    def turn_off(self):
        print("lights are turned off")
    def intensity(self):
        pass


class desk:
    height=100 #cm
    color="brown"
    is_wheeled=True
    def change_height(self,height):
        self.height=height

class fan:
    max_speed=10
    brand="cello"


class shutter:
    size=30
    def open(self):
        print("shutters are open")
    def close(self):
        print("shutters are close")


ac=Ac() #ac is instance if Ac class
print(ac.temp)
print(ac.brand)
print(ac.capacity)
ac.turn_on()

bulb=light()
print(bulb.watt)
print(bulb.brand)
print(bulb.shape)
bulb.turn_on()
bulb.turn_off()


table=desk()

table.change_height(30)
print(table.height)


Fan=fan()
print(Fan.max_speed)
print(Fan.brand)

curtains=shutter()
print(curtains.size)
curtains.open()


