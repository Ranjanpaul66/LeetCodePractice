def decorator_func(func):
    def wrapper_func():
        print("Wrapper func")
        func()
    print("Decorator")
    return wrapper_func

@decorator_func
def arg_func():
    print("Hello")

arg_func()

