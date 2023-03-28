class Dog:
    def speak(self):
        print("Barking")

class Puppy(Dog):
    def play(self):
        print("Playing")


d = Dog()
e = Puppy()
e.play()
e.speak()
d.speak()

print(issubclass(Puppy,Dog))
print(isinstance(d,Dog))
print(isinstance(d,Puppy))