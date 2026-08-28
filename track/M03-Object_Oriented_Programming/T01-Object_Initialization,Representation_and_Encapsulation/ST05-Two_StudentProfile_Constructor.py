class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance variables
        self.student_id = student_id
        self.name = name
        self.course = course


first_id = int(input())
first_name = input().strip()
first_course = input().strip()

second_id = int(input())
second_name = input().strip()
second_course = input().strip()

# Create the first StudentProfile object
First_Student = StudentProfile(first_id, first_name, first_course)
# Create the second StudentProfile object
Second_Student = StudentProfile(second_id, second_name, second_course)
# Print the first student's data
print("Student 1")
print(f"ID: {First_Student.student_id}")
print(f"Name: {First_Student.name}")
print(f"Course: {First_Student.course}")
# Print the second student's data
print("Student 2")
print(f"ID: {Second_Student.student_id}")
print(f"Name: {Second_Student.name}")
print(f"Course: {Second_Student.course}")