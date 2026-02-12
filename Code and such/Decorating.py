def simple_decorator(func):
    def wrapper():
        print("Before the function runs!")
        func()
        print("After the function runs!")
    return wrapper

@simple_decorator
def say_hello():
    print("Hi :)")

say_hello()