class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
class Employee(User):
    def __init__(self, name, age, salary, role):
        super().__init__(name, age)
        self.salary = salary
        self.role = role

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"
class Admin(User):
    def __init__(self, name, age, role = "Administrator"):
        super().__init__(name, age)
        self.role = role

abu = Admin("Abu", 25, "Super Admin")
print(abu) # Name: Abu, Age: 25