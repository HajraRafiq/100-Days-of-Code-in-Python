# #Unlimited arguments

# #Positional Arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3,4,5,6,7,8))
        

#Keyword Arguments

def calculate(n , **kwargs): #its a dictionary typer
    n+= kwargs["multiply"]
    print(kwargs)
    print(n)

calculate(5, add=3,multiply=5)

class Car:
    def __init__(self , **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make = "Toyota" , model = "Civic")
print(my_car.model)

class Student:
    def __init__(self , **kw):
        self.name = kw.get("name")
        self.age = kw.get("age")

student = Student(name = "Hajra" , age = "23")
print(student.name)





