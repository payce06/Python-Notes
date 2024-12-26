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
        
        def calculate_gpa(self):
        """Calculate and return the GPA."""
        total_grades = 0
        total_courses = 0
        for grades in self.courses.values():
            if grades:
                total_grades += sum(grades)
                total_courses += len(grades)
        if total_courses == 0:
            return 0
        return total_grades / total_courses

    def display_info(self):
        """Display the student's information."""
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

        print("Courses and Grades:")
        for course_code, grades in self.courses.items():
            print(f"  {course_code}: {grades} (Average: {sum(grades) / len(grades) if grades else 0:.2f})")
        print(f"GPA: {self.calculate_gpa():.2f}")

class StudentManagementSystem:
    def __init__(self):
        """Initialize the Student Management System."""
        self.students = {}
        self.courses = {}

    def add_student(self, student):
        """Add a student to the system."""
        if student.student_id not in self.students:
            self.students[student.student_id] = student
            print(f"Student {student.name} added to the system.")
        else:
            print(f"Student ID {student.student_id} already exists.")
        
        def add_course(self, course):
        """Add a course to the system."""
        if course.course_code not in self.courses:
            self.courses[course.course_code] = course
            print(f"Course {course.course_name} added to the system.")
        else:
            print(f"Course Code {course.course_code} already exists.")

    def search_student(self, student_id):
        """Search for a student by their ID."""
        return self.students.get(student_id, None)

    def display_all_students(self):
        """Display all students in the system."""
        for student in self.students.values():
            student.display_info()

# Main Program
if __name__ == "__main__":

    
    # Create the management system
    sms = StudentManagementSystem()

    # Create courses
    course1 = Course("Mathematics", "MATH101")
    course2 = Course("Computer Science", "CS101")

    # Add courses to the system
    sms.add_course(course1)
    sms.add_course(course2)

    # Create students
    student1 = Student("Alice Johnson", 20, "S12345")
    student2 = Student("Bob Smith", 22, "S67890")

    # Add students to the system
    sms.add_student(student1)
    sms.add_student(student2)

    # Enroll students in courses
    student1.enroll_in_course(course1)
    student1.enroll_in_course(course2)
    student2.enroll_in_course(course1)

    # Add grades
    student1.add_grade("MATH101", 95)
    student1.add_grade("CS101", 88)
    student2.add_grade("MATH101", 72)

    # Display information
    print("\nAll Students:")
    sms.display_all_students()

    print("\nStudents in Mathematics:")
    course1.display_students()