def sum(*args):
    total =0
    for item in args:
        total =total + item
    return total

print(sum(123,256,25,6))