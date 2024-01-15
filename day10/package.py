
## Create a package (no nesting, no sub-packages) and import a function or object from any of the modules.

from package.greet import squareroot as S
from package.fun import average as A, power as P

print ( S(48))
print ( A(21,3),P(5,6))

