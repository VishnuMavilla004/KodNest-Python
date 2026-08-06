# Read marks, attendance and project completion status by user input
Marks = int(input("Enter your marks: "))
Attendance = int(input("Enter your attendance: "))
Project_status = input("Enter your Project_status(yes/no): ")

# Check academic requirements
# Marks >= 60 and Attendance >= 75% and Project_status == "yes"
if Marks >= 60 and Attendance >=75 :
    #check project status
    if Project_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")