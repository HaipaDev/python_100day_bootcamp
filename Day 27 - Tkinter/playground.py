def add(*args):
    _sum=0
    for n in args:
        _sum+=n
    return  _sum
print(add(2,4,6))

print("\n")
def calculate(n,**kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=5)

class Car:
    def __init__(self,**kw):
        # self.make=kw["make"]
        # self.model=kw["model"]
        self.make=kw.get("make")
        self.model=kw.get("model")

my_car=Car(make="Nissan",model="GT-R")
print(f"{my_car.make} {my_car.model}")
my_car=Car(make="Nissan")
print(my_car.model)