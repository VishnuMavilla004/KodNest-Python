class JobDescription:
    def __init__(
        self,
        role,
        company,
        minimum_experience,
        required_skills
    ):
        # Store all job information
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience
        self.required_skills = required_skills

    # Create the from_text() alternative constructor
    @classmethod
    def from_text(cls, data):
        role, company, minimum_experience, required_skills = data.split(";")
        minimum_experience = int(minimum_experience)
        
        # Split by comma and strip extra spaces from each individual skill 'i'
        skills_list = [i.strip() for i in required_skills.split(",")]
        
        role = role.strip().title()
        company = company.strip()
        return cls(role, company, minimum_experience, skills_list)


data = input()

# Create the JobDescription using from_text()
Job = JobDescription.from_text(data)

required_skills = ", ".join(Job.required_skills)

# Print the stored job information
print(f"Role: {Job.role}\n"
      f"Company: {Job.company}\n"
      f"Minimum Experience: {Job.minimum_experience} years\n"
      f"Required Skills: {required_skills}")