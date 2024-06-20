class Vehicle:
    land = True
    fuel = "Petrol"


class Car(Vehicle):
    tyre = 4
    doors = 5


obj = Car()
print(obj.land)  # True
print(obj.fuel)  # Petrol

# is same as

Vehicle = type('Vehicle', (), {"land": "True", "fuel": "petrol"})
Car = type('Car', (Vehicle,), {"tyre": 4, "doors": 5})

obj = Car()
print(obj.land)  # True
print(obj.fuel)  # Petrol


class VoteMeta(type):
    _instances = []

    def __call__(cls, x):
        print('a')
        if not cls._instances:
            cls._instances.append(super().__call__(x))
        return cls._instances[0]

    def __new__(self, cls, bases, attrs):
        print('b')
        print(cls, bases, attrs)
        return type(cls, bases, attrs)

class Vote(metaclass=VoteMeta):
    print('c')
    def __init__(self, x):
        self.x = x

print('st')
obj1 = Vote(2)
obj2 = Vote(1)
obj3 = Vote(3)
print("First:", obj1.x, "Second:", obj2.x, "Third", obj3.x, sep=" ")
