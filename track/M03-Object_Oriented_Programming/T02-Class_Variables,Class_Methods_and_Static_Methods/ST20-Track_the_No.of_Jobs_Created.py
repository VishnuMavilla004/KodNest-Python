class JobDescription:
    # Create the class-level job counter
    job_count = 0

    def __init__(self, role, company):
        # Store the job information
        # Increase the shared counter
        self.role = role
        self.company = company
        
        JobDescription.job_count += 1


n = int(input())
jobs = []

# Read n job records and create n objects
for i in range(n):
    role = input()
    company = input()
    Job = JobDescription(role, company)
    jobs.append(Job)

# Print the total number of created jobs
print(f"Jobs Created: {JobDescription.job_count}")