#!/usr/bin/python


class Employee:
    '''Common base class for all employees'''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __str__(self):
        return '\nName: ' + self.name + '\nSalary:' +\
            str(self.salary) + '\nEmployeeCount: ' + str(self.empCount)

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)

print(emp2)
