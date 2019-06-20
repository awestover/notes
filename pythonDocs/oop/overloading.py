def f(*x):
    if len(x) == 1:
        return x[0] + 42
    elif len(x) == 2:
        return x[0] - x[1] + 5
    else:
        return 2 * x[0] + x[1] + 42
print(f(3), f(1, 2), f(3, 2, 1))
