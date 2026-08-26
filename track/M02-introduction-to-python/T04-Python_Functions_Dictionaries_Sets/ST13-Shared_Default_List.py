def add_student(name, students=[]):
    # Write your code here
    students.append(name)
    print(students)
    
first_name = input("Enter name: ")
second_name = input("Enter name: ")
third_name = input("Enter name: ")

add_student(first_name)
add_student(second_name)
add_student(third_name)