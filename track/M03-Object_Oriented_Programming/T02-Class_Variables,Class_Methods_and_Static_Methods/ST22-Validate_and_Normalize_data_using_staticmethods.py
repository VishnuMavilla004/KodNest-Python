class StudentProfile:
    # Create the is_valid_skill() static method
    @staticmethod
    def is_valid_skill(skill_name):
        if not skill_name.strip():
            return False
        # Every character must be a letter or a space
        for char in skill_name:
            if not (char.isalpha() or char.isspace()):
                return False
        return True

    # Create the normalize_skill() static method
    @staticmethod
    def normalize_skill(skill_name):
        return "_".join(skill_name.strip().lower().split())


skill_name = input()

# Validate the skill
if StudentProfile.is_valid_skill(skill_name):
    print("Valid Skill")
    print(f"Normalized Skill: {StudentProfile.normalize_skill(skill_name)}")
# Normalize and print it only when valid
else:
    print("Invalid Skill")