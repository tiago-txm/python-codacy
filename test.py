"""
`getdoc` should land before `getmodule`
"""

from inspect import (
    getmodule,
    getdoc,
)


print(getmodule(getdoc))
#blabla
print(getdoc(getmodule))

def teste():
    if True:
        #blablabla
        return True

def teste2():
 print("hello")