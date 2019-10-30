There is no performance difference, the difference is if the exported variables are brought into scope. using is nice for interactive code but for library code it is in my opinion more descriptive (at least when the code size starts to get larger) to use import.

Compare e.g.

using A, B, C # A exports p, B exports y, C exports z

foo(x) = p(x) + y(x) + z(x)
vs

import A, B, C

foo(x) = A.p(x) + B.y(x) + C.z(x)
or

import A.p, B.y, C.z

foo(x) = p(x) + y(x) + z(x)
In both the latter examples, it is easy to see where p, y and z comes from. In the first one you have to either run using A, B, C in the REPL and just see where they are defined, or search through the source code of A, B, and C.

-https://discourse.julialang.org/t/import-vs-using-v0-7/11753/2

