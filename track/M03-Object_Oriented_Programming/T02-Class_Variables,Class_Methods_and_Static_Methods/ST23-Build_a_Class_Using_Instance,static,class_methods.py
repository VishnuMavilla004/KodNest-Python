class TrainingBatch:
    batch_name = "Python Batch 1"
    student_count = 0

    def __init__(self, student_name, attendance):
        # Store the student data
        # Increase the shared student count
        self.student_name = student_name
        self.attendance = attendance
        TrainingBatch.student_count += 1

    def get_details(self):
        # Return the formatted student details
        return (f"{self.student_name}: {self.attendance}%")

    # Create the update_batch_name() class method
    @classmethod
    def update_batch_name(cls, new_batch_name):
        cls.batch_name = new_batch_name

    # Create the is_valid_attendance() static method
    @staticmethod
    def is_valid_attendance(attendance):
        return 0 <= attendance <= 100


n = int(input())
students = []

# Read n records
# Validate attendance and create valid objects
for i in range(n):
    name = input().strip()
    attendance = int(input())
    if TrainingBatch.is_valid_attendance(attendance):
        student = TrainingBatch(name, attendance)
        students.append(student)

new_batch_name = input().strip()

# Update the shared batch name
TrainingBatch.update_batch_name(new_batch_name)
# Print the batch, count and valid student details
print(f"Batch: {TrainingBatch.batch_name}")
print(f"Valid Students: {TrainingBatch.student_count}")
for s in students:
    print(s.get_details())