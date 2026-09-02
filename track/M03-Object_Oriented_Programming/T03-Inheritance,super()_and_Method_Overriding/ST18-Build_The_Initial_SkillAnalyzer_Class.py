class SkillAnalyzer:
    # Add the constructor and get_matched_skills()
    def __init__(self, student_skills, job_skills):
        self.student_skills = set(student_skills)
        self.job_skills = set(job_skills)

    def get_matched_skills(self):
        return self.student_skills & self.job_skills


student_skills = input().split()
required_skills = input().split()

# Create the analyzer and display matched skills
analyzer = SkillAnalyzer(student_skills, required_skills)

matched = analyzer.get_matched_skills()
if matched:
    print(f"Matched Skills: {', '.join(sorted(matched))}")
else:
    print("Matched Skills: None")