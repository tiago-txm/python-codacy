"""
`getdoc` should land before `getmodule`
"""

def teste():
   if True:
       #blablabla
     return True

def teste2():
print("hello")

from inspect import (
    getmodule,
    getdoc,
)


print(getmodule(getdoc))
#blabla
print(getdoc(getmodule))