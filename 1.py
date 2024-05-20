class Animal:
    def say_hello(self):
        print("Hello")

class Cat(Animal):
    def say_hello(self):
        print("maymay")

class Dog(Animal):
    def say_hello(self):
        print("afaf")

cat=Cat()
dog=Dog()

cat.say_hello()  
dog.say_hello()  