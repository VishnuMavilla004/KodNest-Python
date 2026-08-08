# Read the input
sentence = input("Enter any sentence: ")

# Clean and Normalize the sentence
Sentence = sentence.strip(" ")
sentence = Sentence.lower().replace(".","")

# Split the sentence and slug the sentence
Words = sentence.split(" ")
Slug_Sentence = "-".join(Words)

# Produce the uppercase form and search Result
slug_sentence =  Slug_Sentence.replace("-"," ")
Upper_Case = slug_sentence.upper()
Search_Word = Upper_Case.find("PYTHON")

# Display the Results
print(f"Cleaned: {Sentence}")
print(f"Normalized: {sentence}")
print(f"Words: {Words}")
print(f"Slug: {Slug_Sentence}")
print(f"Uppercase: {Upper_Case}")
print(f"Python Index: {Search_Word}")