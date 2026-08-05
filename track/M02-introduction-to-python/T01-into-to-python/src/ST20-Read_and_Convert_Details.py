# Read the values by user input
Student_Name = input("Enter name: ")
Student_Age = int(input("Enter Age: "))
Course_Fee = float(input("Enter Course Fee: "))
Is_Enrolled = bool(input("Enter Enrollment Status (True/False): "))

# Display the details and their types.
print(f"Name : {Student_Name}")
print(f"Age : {Student_Age}")
print(f"Course Fee : {Course_Fee}")
print(f"Enrolled : {Is_Enrolled}")

# Display the data types of details
print(type(Student_Name))
print(type(Student_Age))
print(type(Course_Fee))
print(type(Is_Enrolled))