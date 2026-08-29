class StudentProfile:
    # Create the class-level object counter
    profile_count = 0

    def __init__(self, name):
        # Store the name
        # Increase the shared counter
        self.name = name
        StudentProfile.profile_count += 1


n = int(input())
students = []

# Read n names and create n StudentProfile objects
for i in range(n):
    name = input().strip()
    students = StudentProfile(name)

# Print the number of created profiles
print(f"Profiles Created: {StudentProfile.profile_count}")