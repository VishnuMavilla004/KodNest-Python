class SkillAnalyzer:
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills


class MatchScoreCalculator(SkillAnalyzer):
    # Add calculate_match_score()
    def calculate_match_score(self):
        return (len(self.get_matched_skills()) / len(self.required_skills))*100


student_skills = input().split()
required_skills = input().split()

# Create the calculator and display the score
calculator = MatchScoreCalculator(student_skills, required_skills)

print(f"Match Score: {calculator.calculate_match_score():.2f}%")