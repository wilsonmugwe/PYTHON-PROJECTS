class Animal:
    alive = True

    def eat(self):
        print("It is eating")

    def sleep(self):
        print("It is sleeping")


class Fish(Animal):
    pass

fish = Fish()
fish.eat()



class Mansion:
    def build(self):
        print("It is built")








class mansionette(Mansion):
    def cook(self):
        print("It is cooked")
pato=mansionette()


pato.cook()
