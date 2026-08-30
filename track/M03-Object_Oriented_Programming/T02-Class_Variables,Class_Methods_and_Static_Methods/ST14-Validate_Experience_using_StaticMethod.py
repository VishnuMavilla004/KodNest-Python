class StudentProfile:
    def __init__(self, name, experience):
        # Store the name and experience
        self.name = name
        self.experience = experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):
        return True if 0 <= experience <= 40 else False


name = input().strip()
experience = int(input())

# Validate the experience using the class name
if StudentProfile.is_valid_experience(experience):
    student = StudentProfile(name, experience)
    print(f"Profile Created")
    print(f"Name: {student.name}\nExperience: {student.experience} years")
else:
    print("Invalid Experience")
# Create and print the profile only when valid