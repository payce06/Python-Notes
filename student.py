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
    print(f"Course: {self.course_name} ({self.course_code})")
        print("Enrolled Students:")
        for student in self.students:
            print(f"- {student.name} (ID: {student.student_id})")

class Student:
    def __init__(self, name, age, student_id):
        """Initialize the Student object."""
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courses = {}  # Dictionary to store courses and their grades

    def enroll_in_course(self, course):
        """Enroll the student in a course."""
     if course.course_code not in self.courses:
            self.courses[course.course_code] = []
            course.enroll_student(self)
        else:
            print(f"{self.name} is already enrolled in {course.course_name}.")

    def add_grade(self, course_code, grade):
        """Add a grade for a specific course."""
        if course_code in self.courses:
            if 0 <= grade <= 100:
                self.courses[course_code].append(grade)
            else:
                print("Invalid grade. Please enter a grade between 0 and 100.")
        else:
            print(f"Student is not enrolled in the course with code {course_code}.")