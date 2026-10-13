# 09 10 2026
# dog class

class Dog:
    def __init__(self, f, b, name, age):
        self.furr_color = f
        self.breed = b
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is a {self.breed} of age {self.age} that says Woof!")

class Cat:
    def meows(self):
        print("Meooww")

my_dog = Dog("Brown","Labrador","Rex", 5) 
my_dog.bark()

your_cat = Cat()
your_cat.meows()


 