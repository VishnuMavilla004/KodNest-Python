class Course:
    # Add the constructor and display_course()
    def __init__(self, course_name):
        self.course_name = course_name

    def display_course(self):
        print(f"Course: {self.course_name}")


class CodingCourse(Course):
    def __init__(self, course_name):
        super().__init__(course_name)


course_name = input().strip()

# Create a CodingCourse object and display the course

course = CodingCourse(course_name)

course.display_course()