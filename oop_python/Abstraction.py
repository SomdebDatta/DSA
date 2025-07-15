from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def greet(self):
        print("I will greet you now.")

    def bye(self):
        print("See you soon!")


class Dog(Animal):
    def name(self):
        print("Hi I am a dog.")

    def greet(self):
        super().greet()
        print("Woof!!")

obj = Dog()
obj.name()
obj.greet()
obj.bye()
