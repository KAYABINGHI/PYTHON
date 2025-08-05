# Decorators in Python
# A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
# Decorators are often used to add functionality to existing functions in a clean and readable way.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    # The wrapper function is the one that gets executed instead of the original function
    return wrapper

@my_decorator
def hello():
    print("Hello, world!")

@my_decorator
def greet():
    print("Greetings from above!")

my_decorator(func=hello)()  # Applying the decorator to the hello function
my_decorator(func=greet)()  # Applying the decorator to the greet function
# hello()  # Calling the original function without the decorator
hello()  # Calling the decorated function
greet()  # Calling the greet function without a decorator
