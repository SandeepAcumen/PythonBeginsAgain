'''
def decorator(func):
     def wrapper():
        print("befor Hello!!!!")
        func()
        print("After Hello!!!!")
        func()
     return wrapper


def say_hello():
    print("hello!")

f = decorator(say_hello)
f()

def deco(func):
    def wrapper():
        print("Hello")
        func()
        print ("To you All")
        func()
    return wrapper()



def world():
    print("world")

deco(world)

'''
#Decorators with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)

        return wrapper()
    return decorator()

@repeat(7)
def say_hello(a):
    print(f"hello  {a}" )

say_hello("harry")


