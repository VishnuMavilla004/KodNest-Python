class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        score,
        skills
    ):
        # Create safe private starting values
        # Initialize the properties and skills
        self.__student_id = student_id
        self.__name = name
        self.__score = score
        self.__skills = skills

        cleaned_skills = []
        for skill in skills:
            s = skill.strip()
            if s and s not in cleaned_skills:
                cleaned_skills.append(s)
        self.__skills = cleaned_skills

    @property
    def student_id(self):
        # Return the read-only student ID
        return self.__student_id

    @property
    def name(self):
        # Return the private name
        return self.__name

    @name.setter
    def name(self, new_name):
        # Clean and validate the name
        if new_name and new_name.strip():
            self.__name = new_name.strip()

    @property
    def score(self):
        # Return the private score
        return self.__score

    @score.setter
    def score(self, new_score):
        # Accept only scores from 0 to 100
        if 0 <= new_score <= 100:
            self.__score = new_score

    @property
    def skills(self):
        # Return a tuple containing the skills
        return tuple(self.__skills)

    def add_skill(self, new_skill):
        # Add a cleaned, non-empty and non-duplicate skill
        skill = new_skill.strip()
        if skill and skill not in self.__skills:
            self.__skills.append(skill)

    def __str__(self):
        # Return the complete formatted profile
        skills_str = ", ".join(self.__skills)
        return (
            f"STUDENT PROFILE\n"
            f"Student ID: {self.__student_id}\n"
            f"Name: {self.__name}\n"
            f"Score: {self.__score}\n"
            f"Skills: {skills_str}"
        )


student_id = int(input())
name = input().strip()
initial_score = int(input())
skills_input = input().strip()
new_score = int(input())
new_skill = input().strip()

initial_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

# Create one StudentProfile object
student = StudentProfile(student_id, name, initial_score, initial_skills)

# Update the score through the property
student.score = new_score
# Add the skill through the method
student.add_skill(new_skill)
# Print the final object
print(student)