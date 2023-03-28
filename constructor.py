# Parameterized
class Employee:
    def  __init__(self,firstname,lastname,id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def info(self):
        print(self.firstname,self.lastname,self.id)


e = Employee("Wilson","Mugwe",3)
e.info()
print(getattr(e,"firstname"))
print(getattr(e,"lastname"))
print(hasattr(e,"age"))


#Non-parameterized
class Student:
     def __init__(self):
         print("No parameter available")
     def display(self,name,course,age):

         self.name = name
         self.course = course
         self.age =  age

         print(self.name,self.course,self.age)

p = Student()
p.display("Mugwe","MIT",18)
print(getattr(p,"course"))