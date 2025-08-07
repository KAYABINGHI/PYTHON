# class name: First letter should be capitalized
# class name: Use CamelCase for class names
# class name: Use descriptive names for classes
# class name: Avoid using reserved keywords as class names
# class name: Use nouns for class names
# class name: Keep class names concise but meaningful
# class name: Use singular nouns for class names
# class name: Avoid abbreviations in class names
# class name: Use underscores to separate words in class names if necessary
# class name: Ensure class names are unique within the module
# class name: Use consistent naming conventions across the codebase
# class name: Avoid using special characters in class names
# class name: Use PascalCase for class names
# class name: Use clear and descriptive names that reflect the purpose of the class
# class name: Avoid using generic names like "Data" or "Info"
# class name: Use meaningful prefixes or suffixes if needed to clarify the class's role
# class name: Consider the context and functionality of the class when naming

class Student:
    name = "Daniel"
    age = 20
    country = "Kenya"

def create_student2():
    student2 = Student()
    student2.name = "Alice"
    student2.age = 22
    student2.country = "Canada"
    return student2

student1 = Student()
student2 = create_student2()

print(student1)
print("name:", student1.name)
print("age:", student1.age)
print("country:", student1.country)

print(student2)
print("name:", student2.name)
print("age:", student2.age)
print("country:", student2.country)
