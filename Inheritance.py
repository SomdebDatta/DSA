class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age

        super().__init__("Piku", 69)

    def displayInfo(self):
        print(self.sName, self.sAge)


# obj = Student("Somdeb", 23)
# obj.display()
# obj.displayInfo()


class Mother:
    def __init__(self):
        self.human = True

    def nose(self):
        print("I have a blunt nose.")

    def age(self):
        print("My age is 45 years")


class Father:
    def __init__(self):
        self.human = True

    def __neck(self):
        print("I have an Adam's apple.")

    def age(self):
        print("My age is 50 years")


class Son(Mother, Father):
    def __init__(self):
        super().__init__()
        print(f"Am I a human? - {self.human}")

    def neck(self):
        print("Since I'm a male,")
        super()._Father__neck()


# print(Son())
my_obj = Son()
my_obj.neck()
