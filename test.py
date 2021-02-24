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