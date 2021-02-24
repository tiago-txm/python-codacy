"""
`getdoc` should land before `getmodule`
"""
class teste():
    
from inspect import (
    getmodule,
    getdoc
)
def teste():
   if True:
       #blablabla
     return True

def teste2():
print("hello")




print(getmodule(getdoc))
#blabla
print(getdoc(getmodule))