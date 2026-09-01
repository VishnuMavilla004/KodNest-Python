class Person:
    # Create display_name() here
    def display_name(name):
        print(f"Student Name: {name}")


class Student(Person):
    pass


name = input("Enter the student name: ").strip()

# Create a Student object and call display_name()
Student.display_name(name)