'''
Data Hiding
An object's attributes may or may not be visible outside the class definition.
You need to name attributes with a double underscore prefix, and those
attributes then will not be directly visible to outsiders.

Example
'''
# !/usr/bin/python3


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)

# Will not work:
try:
    print(counter.__secretCount)
except AttributeError as AE:
    print(AE)


''''
When the above code is executed, it produces the following result:
1
2
2
'JustCounter' object has no attribute '__secretCount'

Python protects those members by internally changing the name to include the
class name. You can access such attributes as object._className__attrName.
'''
