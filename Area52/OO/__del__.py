# Example
# This __del__() destructor prints the class name
# of an instance that is about to be destroyed −


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

# When the above code is executed, it produces the following result −
# 3083401324 3083401324 3083401324
# Point destroyed

'''
# Note − Ideally, you should define your classes in a separate file,
# then you should import them in your main program file using import statement.
# In the above example, assuming definition of a Point class is contained in
# point.py and there is no other executable code in it.
'''

import point
p1 = point.Point()
