"""
`getdoc` should land before `getmodule`
"""

from inspect import (
    getmodule,
    getdoc,
)


print(getmodule(getdoc))
print(getdoc(getmodule))