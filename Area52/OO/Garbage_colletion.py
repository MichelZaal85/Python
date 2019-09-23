'''
Destroying Objects (Garbage Collection):
Python deletes unneeded objects (built-in types or class instances)
automatically to free the memory space. The process by which Python
periodically reclaims blocks of memory that no longer are in use is
termed as Garbage Collection. Python's garbage collector runs during
program execution and is triggered when an object's reference count
reaches zero. An object's reference count changes as the number of
aliases that point to it changes. An object's reference count
increases when it is assigned a new name or placed in a container
(list, tuple, or dictionary). The object's reference count decreases
when it is deleted with del, its reference is reassigned, or its
reference goes out of scope. When an object's reference count
reaches zero, Python collects it automatically.
'''

a = 40      # Create object <40>
b = a       # Increase ref. count  of <40>
c = [b]     # Increase ref. count  of <40>

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40>
c[0] = -1   # Decrease ref. count  of <40>

'''
You normally will not notice when the garbage collector destroys an orphaned
instance and reclaims its space. However, a class can implement the special
method __del__(), called a destructor, that is invoked when the instance is
about to be destroyed. This method might be used to clean up any non-memory
resources used by an instance.
'''
