#!/usr/bin/python3
# Class Inheritance.py

'''
Instead of starting from a scratch, you can create a class by deriving it
from a pre-existing class by listing the parent class in parentheses after
the new class name. The child class inherits the attributes of its parent
class, and you can use those attributes as if they were defined in the
child class. A child class can also override data members and methods
from the parent.
'''


class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):  # constructor
        print("Calling parent constructor")

    def parentMethod(self):  # self connects function to parent Classname
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

# When the above code is executed, it produces the following result
'''
Calling child constructor
Calling child method
Calling parent method
Parent attribute : 200

You can use issubclass() or isinstance() functions to check a
relationships of two classes and instances.
The issubclass(sub, sup) boolean function returns True, if the
given subclass sub is indeed a subclass of the superclass sup.

The isinstance(obj, Class) boolean function returns True, if
obj is an instance of class Class or is an
instance of a subclass of Class

Overriding Methods
You can always override your parent class methods. One reason
for overriding parent's methods
is that you may want special or different functionality in your subclass.
'''


class Parent:  # define parent class
    def myMethod(self):
        print('Calling parent method')


class Child(Parent):  # define child class
    def myMethod(self):
        print('Calling child method')


c = Child()   # instance of child
c.myMethod()  # child calls overridden method

'''
Base Overloading Methods
The following table lists some generic functionality
that you can override in your own classes

S.No. Method, Description & Sample Call
1  __init__ ( self [,args...] )
   Constructor (with any optional arguments)
   Sample Call : obj = className(args)

2  __del__( self )
   Destructor, deletes an object
   Sample Call : del obj

3  __repr__( self )
   Evaluatable string representation
   Sample Call : repr(obj)

4  __str__( self )
   Printable string representation
   Sample Call : str(obj)

5  __cmp__ ( self, x )
   Object comparison
   Sample Call : cmp(obj, x)
'''
