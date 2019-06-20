class A:
    pass
class B(A):
    pass
class C(B):
    pass
x = C()
print(isinstance(x, A))

## note the difference between type(x) and isinstance(x, class)
## if you are a subclass then you are still an instance of the super class, but your type is the msot specific class that you belong too
