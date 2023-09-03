class Base:
    def __init__(self):
        print("This is the base class.")

        self.__a = 2


# class Derived(Base):
#     def __init__(self):
#         print("This is the Derived class.")

#         Base.__init__(self)

#         print(f"Now calling the protected member of the Base class - {self._a}")

#         print(
#             f"Now calling changing modifying the value of the protected member of the Base class to 3"
#         )

#         self._a = 3

#         print(
#             f"Modified value of the protected member of the parent class is - {self._a}"
#         )


obj1 = Base()

# obj2 = Derived()

print(f"Accessing the protected member of the Base class - {obj1.__a}")
# print(f"Accessing the protected member of the Derived class - {obj2._a}")
