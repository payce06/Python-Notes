class Course:
    def __init__(self, course_name, course_code):
        """Initialize the Course object."""
        self.course_name = course_name
        self.course_code = course_code
        self.students = []  # A list to store enrolled students

    def enroll_student(self, student):
        """Enroll a student in the course."""
        if student not in self.students:
            self.students.append(student)
            print(f"{student.name} has been enrolled in {self.course_name}.")
        else:
            print(f"{student.name} is already enrolled in {self.course_name}.")

    def display_students(self):
        """Display all students in the course."""