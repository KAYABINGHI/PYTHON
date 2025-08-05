# kwargs [keyword arguments]
# This file demonstrates the use of kwargs in Python functions.
# kwargs allows you to pass a variable number of keyword arguments to a function.
# kwargs is a dictionary that collects all keyword arguments passed to the function.


# def greet(name, nationality):
#     print("Name is:", name)
#     print("from:", nationality)

# # kwargs solves the mixup of positional and keyword arguments
  
# greet(name="Alice", nationality="Kenya") 

# kwargs profile
# def employee(**kwargs):
#     print(kwargs)

# employee(name="Alice", age=30, position="Engineer")
# employee(name="Bob", age=25, position="Designer", country="USA")
# employee(name="Charlie", age=28, position="Manager", country="UK", experience=5)

def mixed(*args, **kwargs):
    print("Keyword arguments:", kwargs)
    print("Positional arguments:", args)

mixed(1, 2, 3, name="Alice", age=30, country="Kenya")