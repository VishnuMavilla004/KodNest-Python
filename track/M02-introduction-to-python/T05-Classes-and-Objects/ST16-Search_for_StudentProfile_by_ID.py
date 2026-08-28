class StudentProfile:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.student_id} - {self.name} - {self.course}"


class PlacementManager:
    def __init__(self):
        self.student_profiles = []

    def add_student_profile(self, student_profile):
        self.student_profiles.append(student_profile)

    def find_student_by_id(self, student_id):
        # Search for and return the matching object
        # Return None if no match is found
        self.student_id = student_id
        for i in self.student_profiles:
            if i.student_id == student_id:
                return i
        
        return None


manager = PlacementManager()

n = int(input())

for _ in range(n):
    student_id = int(input())
    name = input().strip()
    course = input().strip()

    student = StudentProfile(student_id, name, course)
    manager.add_student_profile(student)

required_id = int(input())
result = manager.find_student_by_id(required_id)

if result is not None:
    print(result)
else:
    print(f"Student profile with ID {required_id} not found")