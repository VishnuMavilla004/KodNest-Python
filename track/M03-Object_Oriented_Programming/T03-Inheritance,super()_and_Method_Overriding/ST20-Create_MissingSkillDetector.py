class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MissingSkillDetector(SkillAnalyzer):
    # Add get_missing_skills()
    def get_missing_skills(self):
        # Calculate skills that are in required_skills but not in student_skills
        missing = self.required_skills - self.student_skills
        
        if missing:
            # Sort alphabetically and join with ', '
            print(f"Missing Skills: {', '.join(sorted(missing))}")
        else:
            print("Missing Skills: None")

# Input reading
student_skills = input().split()
required_skills = input().split()

detector = MissingSkillDetector(student_skills, required_skills)
detector.get_missing_skills()

# Create the detector and display missing skills