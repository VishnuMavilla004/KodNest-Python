skills = []

# Read and store five skills
for i in range(5):
    skills.append(input())

# Convert the list into a tuple
skill_record = tuple(skills)

# Create the required slices
slice1 = skill_record[:]
slice2 = skill_record[0:3]
slice3 = skill_record[3:5]
slice4 = skill_record[0:5:2]
slice5 = skill_record[::-1]

# Display all required results
print(f"Skill Record: {slice1}")
print(f"First Three: {slice2}")
print(f"Last Two: {slice3}")
print(f"Alternate Skills: {slice4}")
print(f"Reversed Skills: {slice5}")