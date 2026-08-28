# Create the StudentProfile class
class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"
# Create the PlacementManager class
class PlacementManager:
    def __init__(self):
        self.student_profiles = []
        
    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    
    def filter_students_by_course(self, course):
        matching = []
        for i in self.student_profiles:
            if i.course.lower() == course.lower():
                matching.append(i)
        return matching

manager = PlacementManager()
# Read the student details
n = int(input().strip())

for i in range(n):
    Student_id = int(input().strip())
    Student_name = input().strip()
    Course_name = input().strip()

    student = StudentProfile(Student_id, Student_name, Course_name)
    manager.add_student_profile(student)
# Filter and display the matching students
filter_course = input().strip()

matching = manager.filter_students_by_course(filter_course)

if matching:
    for i in matching:
        print(i)
else:
    print(f"No students found for course: {filter_course}")
