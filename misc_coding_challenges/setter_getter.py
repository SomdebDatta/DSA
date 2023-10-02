"""
Create a Student class with the following attributes:
student_id
first_name
last_name
email
age
grades (a list to store the student's course grades)
Implement the following methods in the Student class:
__init__(self, student_id, first_name, last_name, email, age): Initialize the student object with the provided information.
get_full_name(self): Return the full name of the student.
Implement a @property decorator for the get_full_name method to make it accessible as an attribute
get_average_grade(self): return the average grade
Implement a @property decorator for the get_average_grade method that calculates and returns the average of all grades in the grades list.
get_student_id(self): Return the student's ID.
get_age(self): Return the student's age.
get_email(self): Return the student's email.
set_email(self, new_email): Set a new email address for the student
add_grade(self, grade): Add a grade to the student's list of grades.
[$, %, #]
validate_email(self): characters and numbers - @ - mycompany. / mycompany.in?
"""
from typing import List


class Student:
    def __init__(
        self,
        student_id: int,
        first_name: str,
        last_name: str,
        email: str,
        age: int,
        grades: List,
    ) -> None:
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.grades = grades

    @property
    def get_full_name(self) -> str:
        return " ".join([self.first_name, self.last_name])

    @property
    def get_student_id(self) -> int:
        return self.student_id

    @property
    def get_age(self) -> int:
        return self.age

    @property
    def get_email(self) -> str:
        return self.email

    @get_email.setter
    def set_email(self, new_email) -> None:
        self.email = new_email

    def add_grade(self, grade: int) -> None:
        self.grades.append(grade)

    @property
    def get_avg_grade(self) -> float:
        return sum(self.grades) / len(self.grades)


my_obj = Student(123, "Som", "Datta", "abc@gmail.com", 345, [1, 2, 3])
# print(my_obj.student_id)
# print(my_obj.grades)
# print(my_obj.get_full_name)
# print(my_obj.get_avg_grade)
print(my_obj.email)
my_obj.email = "cba@gmail.com"
print(my_obj.email)
print(my_obj.grades)
print(my_obj.get_avg_grade)
my_obj.add_grade(25)
print(my_obj.grades)
print(my_obj.get_avg_grade)
