class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location,
        required_skills,
        is_active
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.required_skills = required_skills
        self.is_active = is_active

    def __str__(self):
        # Return the complete formatted job description
        self.is_active = "Active" if status_input.strip().lower() == "yes" else "Closed"
        return (
            f"JOB DESCRIPTION\n"
            f"Job ID: {self.job_id}\n"
            f"Company: {self.company}\n"
            f"Role: {self.role}\n"
            f"Location: {self.location}\n"
            f"Required Skills: {', '.join(required_skills)}\n"
            f"Status: {self.is_active}"
        )


job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
skills_input = input().strip()
status_input = input().strip()

required_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_active = status_input.lower() == "yes"
# Create one JobDescription object
job = JobDescription(job_id, company, role, location, skills_input, status_input)

# Display the object using print(job)
print(job)
