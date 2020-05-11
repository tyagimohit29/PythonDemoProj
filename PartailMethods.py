from functools import partial

def multiply(x,y):
    return x * y

def1 = partial(multiply,2)

print(def1(4))
