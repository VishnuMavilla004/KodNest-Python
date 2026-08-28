class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        experience,
        skills
    ):
        # Store all received values as instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.experience = experience
        self.skills = skills


student_id = int(input())
name = input().strip()
course = input().strip()
experience = int(input())
skills = input().split()

# Create one StudentProfile object
Student_One = StudentProfile(student_id,name,course,experience,skills)
# Print the data stored in the object
print(f"Student ID: {Student_One.student_id}")
print(f"Name: {Student_One.name}")
print(f"Course: {Student_One.course}")
print(f"Experience in Years: {Student_One.experience}")
print(f"Skills: {', '.join(Student_One.skills)}")