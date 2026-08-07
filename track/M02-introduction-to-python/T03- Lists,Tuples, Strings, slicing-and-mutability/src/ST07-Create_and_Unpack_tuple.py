# Creating and unpacking a tuple containing student records
# Read the values of student name, Course, Score
name = input("Enter student name: ")
course = input("Enter course name: ")
score = int(input("Enter score:"))

# create a tuple and store these details in that
student_record = (name, course, score)

# Unpack the details and display them
Name = student_record[0]
Course = student_record[1]
Score = student_record[2]

print(f"Name: {Name}")
print(f"Course: {Course}")
print(f"Score: {Score}")

"""
print("\nUsing tuple unpacking (simpler):")
Name, Course, Score = student_record

print(f"Name: {Name}")
print(f"Course: {Course}")
print(f"Score: {Score}")

print("\nUsing loop (even simpler for many items):")
for detail in student_record:
    print(detail)
    
"""