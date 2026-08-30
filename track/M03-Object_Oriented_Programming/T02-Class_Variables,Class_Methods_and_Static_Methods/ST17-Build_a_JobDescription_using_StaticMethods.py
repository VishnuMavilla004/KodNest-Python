class JobDescription:
    platform_name = "KodNest Jobs"

    def __init__(
        self,
        role,
        company,
        minimum_experience
    ):
        # Store the job information
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(experience):
        return 0<= experience <= 20

    # Create the from_text() class method
    @classmethod
    def from_text(cls, data):
        role, company, experience = data.split("|")
        role = role.strip().title()
        company = company.strip()
        experience = int(experience)
        

        if not cls.is_valid_experience(experience):
            return None
        else:
            return cls(role, company, experience)


data = input()
Job = JobDescription.from_text(data)

# Create the job using from_text()
if Job:
    print(f"Platform: {JobDescription.platform_name}")
    print(f"Role: {Job.role}")
    print(f"Company: {Job.company}")
    print(f"Minimum Experience: {Job.minimum_experience} years")    
else:
    print("Invalid Experience")
# Print the job or the invalid message
