#
#  import_example.py
#
#
#
# if you parse many tkinter examples you'll see different forms of 'import'
#   used.  This example, using the familiar random.randint() function, shows
#   how it's possible to cause an error if you use the 'from library import *'
#   construct by inadvertently naming a variable or function the same as
#   an existing function in the library
#
#  to check this run it as-is and it will pass, then comment out the first
#   block of code (from import to print), uncomment the 2nd block and run it
#   and it will pass, then comment everything except the block beginning
#   'from random import *' and run it to generate a fail due to a name collision
#
#  there's also a fourth example using 'from random import randint', i.e., just
#    grabbing one function name, and this fails too


import random       # safest but more typing since every call to this
                    #  library will be preceeded by the full library name.
                    #   Also, if the spelling changes (tkinter <-> Tkinter)
                    #   every line must be changed

rand_num = random.randint(1,6)   # note randint is a function name here, but ...
                                 #
randint = rand_num**2            #   an integer variable name on this line
rand_num2 = random.randint(1,3)
rand_out = randint -1
print (rand_out)


"""
import random as r      # less typing since you shorten the lib name.
                        #  potential problem if somehow two libraries are given
                        #  the same replacement name ('r') by mistake

rand_num = r.randint(1,6)  # note we can type r.randint
randint = rand_num**2
rand_num2 = r.randint(1,3)
rand_out = randint -1
print (rand_out)
"""

"""
from random import *       # less typing but names can overwrite functions
                           #   this one fails
rand_num = randint(1,6)
randint = rand_num**2
rand_num2 = randint(1,3)   # generates TypeError: 'int' object is not callable
rand_out = randint -1
print (rand_out)
"""
# the above block fails because randint = rand_num**2 redefines 'randint' as
#   an integer variable.  Then when randint is used in the next line the
#   program no longer recognizes it as the random.randint function


# this block below also fails for a similar reason
"""
from random import randint   # imports just the functions you need so no
                             # name space pollution, but still can fail

rand_num = randint(1,6)
randint = rand_num**2
rand_num2 = randint(1,3)
rand_out = randint -1
print (rand_out)
"""

# from the Python style guide at
#   http://code.google.com/p/soc/wiki/PythonStyleGuide#Module_and_package_imports
#
#    Imports: Import only modules and only by name (no wildcard imports)
#       http://code.google.com/p/soc/wiki/PythonStyleGuide#Imports
