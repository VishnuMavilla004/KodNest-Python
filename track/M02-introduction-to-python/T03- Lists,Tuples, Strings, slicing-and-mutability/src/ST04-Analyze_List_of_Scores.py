# Read the number of scores
n = int(input("Enter no. of scores: "))

# Create a empty list.
Scores = []

# Read and store the values in list and also a searching score input
for i in range(n):
    score = int(input("Enter each score: "))
    Scores.append(score)
search_score = int(input("Enter the score to search:"))

# Analyze the list and Display the Highest, Lowest, and Total Scores
print(f"Highest Score: {max(Scores)}")
print(f"Lowest Score: {min(Scores)}")
print(f"Total Score: {sum(Scores)}")

# Now analyze the list and search for a required score
if search_score in Scores:
    print(f" SearchScore: Found")
else:
    print(f"Search Score: Not Found")
