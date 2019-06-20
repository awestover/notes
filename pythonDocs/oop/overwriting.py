def f(x):
    return x + 42
print(f(3))
# f will be overwritten (or redefined) in the following:
def f(x):
    return x + 43
print(f(3))
