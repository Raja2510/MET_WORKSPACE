#polymorphism
class cat:
    def speak(self):
        print("meow")
class dog:
    def speak(self):
        print("woof")

def make_animal_speak(animal):
    animal.speak()



make_animal_speak(cat())
make_animal_speak(dog())
