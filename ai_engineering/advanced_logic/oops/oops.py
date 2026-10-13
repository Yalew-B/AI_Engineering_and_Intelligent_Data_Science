# OOPs in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name}.")

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id  # private attribute

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.__student_id}."

    def get_student_id(self):
        return self.__student_id


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary  # protected attribute

    def greet(self):
        print(f"Good morning! I am {self.name} and my salary is {self._salary}.")

    def get_salary(self):
        return self._salary


# Polymorphism: same method name with different implementations
people = [Person("Alice", 30), Student("Bob", 20, "S101"), Employee("Charlie", 35, 50000)]

for person in people:
    print(person.introduce())
    person.greet()

# Encapsulation example
student = Student("Diana", 22, "S202")
print(student.get_student_id())

# Inheritance example
employee = Employee("Ethan", 28, 60000)
print(employee.introduce())
print(employee.get_salary())
