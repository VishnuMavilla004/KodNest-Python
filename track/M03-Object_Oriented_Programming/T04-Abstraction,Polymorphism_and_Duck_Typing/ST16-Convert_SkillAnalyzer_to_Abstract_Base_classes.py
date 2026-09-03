from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    def __init__(self, student_skills, required_skills):
        self.student_skills = set(student_skills)
        self.required_skills = set(required_skills)

    def get_matched_skills(self):
        return self.student_skills & self.required_skills

    # Add abstract analyze()
    @abstractmethod
    def analyze(self):
        pass


class MatchScoreCalculator(SkillAnalyzer):
    def calculate_match_score(self):
        matched = len(self.get_matched_skills())
        required = len(self.required_skills)
        result = matched / required * 100
        return f"Match Score: {result:.2f}%"

    # Implement analyze()
    def analyze(self):
        return self.calculate_match_score()


class MissingSkillDetector(SkillAnalyzer):
    def get_missing_skills(self):
        result = self.required_skills - self.student_skills
        if not result:
            return "Missing Skills: None"
        else:
            return f"Missing Skills: {', '.join(result)}"
    # Implement analyze()
    def analyze(self):
        return self.get_missing_skills()


student_skills = input().split()
required_skills = input().split()

# Create both analyzers and print their analyze() results
score = MatchScoreCalculator(student_skills, required_skills)
skill = MissingSkillDetector(student_skills, required_skills)

print(score.analyze())
print(skill.analyze())