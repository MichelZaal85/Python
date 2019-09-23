#!/usr/bin/python3


class Employee:
    '''Common base class for all employees'''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def explain(self):
        print("the 'self' binds the func. to the Class")


# This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
explain = Employee('Class', 101001)
print('\n\n')
explain.explain()
print('\n\n')
print("Total Employee %d" % Employee.empCount)


hasattr(emp1, 'salary')         # Returns true if 'salary' attribute exists
getattr(emp1, 'salary')         # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000)   # Set attribute 'salary' at 7000
delattr(emp1, 'salary')         # Delete attribute 'salary'

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
