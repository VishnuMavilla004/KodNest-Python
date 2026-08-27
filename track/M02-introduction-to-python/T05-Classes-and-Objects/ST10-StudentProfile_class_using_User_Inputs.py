class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        is_placed
    ):
        # Store all received values as instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.is_placed = is_placed

    def __str__(self):
        # Return the complete profile in the required format
        placement_status = "Placed" if self.is_placed else "Not Placed"
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Course: {self.course}\n"
            f"Score: {self.score:.1f}\n"
            f"Placement Status: {placement_status}"
            )


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
placement_input = input().strip().lower()

# Convert placement_input into a Boolean value
is_placed = False
if placement_input == "yes":
    is_placed = True
elif placement_input == "no":
    is_placed = False
else:
    is_placed = None
    
# Create a StudentProfile object using keyword arguments
student = StudentProfile(student_id, name, course, score, is_placed)
print(student)