# A course record contains three values
# Read three values called course name, current week, course status

Course_name = input("Enter course name: ")
Current_week = input("Enter current week of course: ")
Course_status = input("Enter course status: ")

# Create a tuple and store the values in it
course_details = (Course_name, Current_week, Course_status)

# add a updated week to the tuple without modifying it
Updated_week = input("Enter the updated week: ")

# Create a new tuple and store values in it
Course_details = (Course_name, Updated_week, Course_status)

# Display the course details
print(Course_details)