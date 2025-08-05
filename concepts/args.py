# def stuff(name, age,gender, is_student):
#     print("Name:", name)
#     print("Age:", age)
#     print("Gender:", gender)
#     print("Is Student:", is_student) 

def greet(*args):
    for value in args:
        print("Name is", value)
        print("Hello", value)

greet("Daniel", "Alice", "Bob")

def sum(*args):
    total = 0
    for value in args:
        total += value

    print("Total is", total)
    return total

sum(1, 2, 3, 4, 5)

