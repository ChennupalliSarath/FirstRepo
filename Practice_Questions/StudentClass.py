class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get(self):
        print("Student name: ", self.name)
        print("Student age: ", self.age)
class UGStudent (Student):
    def __init__(self, name, age, dept):
        super().__init__(name, age)
        self.dept = dept
    def get(self):
        print("UGStudent name: ", self.name)
        print("UGStudent age: ", self.age)
        print("UGStudent Department: ", self.dept)


name = input("Enter name: ")
age = int(input("Enter age: "))
dept = input("Enter department: ")
# obj = Student(name, age)
# obj.get()
child_obj = UGStudent(name, age, dept)
child_obj.get()