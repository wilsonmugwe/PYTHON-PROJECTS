class Employee:
    def eat(self):
        print("Eating")


class Manager(Employee):
    def task(self):
        print("Co-ordinating")



class Cook(Manager):
    def role(self):
        print("Cooking")


m = Manager()
m.eat()

n = Cook()
n.task()
print(isinstance(m,Manager))
print(issubclass(Cook,Employee))

