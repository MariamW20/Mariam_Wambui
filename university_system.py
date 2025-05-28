from datetime import datetime


class UniversityMember:
    """Base UniversityMember class - similar to BankAccount"""
    
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.join_date = datetime.now().strftime("%Y-%m-%d")
        self.status = "Active"
    
    def display_info(self):
        """Display basic member information"""
        print(f'Member ID: {self.member_id}')
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Join Date: {self.join_date}')
        print(f'Status: {self.status}')
    
    def update_status(self, new_status):
        """Update member status"""
        self.status = new_status
        print(f'Status updated to: {self.status}')
    
    def send_notification(self, message):
        """Send notification to member"""
        print(f'Notification sent to {self.name}: {message}')


# Child class: Student
class Student(UniversityMember):
    def __init__(self, member_id, name, email, student_number, major):
        super().__init__(member_id, name, email)
        self.student_number = student_number
        self.major = major
        self.gpa = 0.0
        self.credits = 0
        self.courses = []
    
    # Override display_info method
    def display_info(self):
        print("=== STUDENT INFORMATION ===")
        super().display_info()
        print(f'Student Number: {self.student_number}')
        print(f'Major: {self.major}')
        print(f'GPA: {self.gpa:.2f}')
        print(f'Credits: {self.credits}')
        print(f'Enrolled Courses: {", ".join(self.courses) if self.courses else "None"}')
    
    # New method specific to students
    def enroll_course(self, course_name, credit_hours):
        """Enroll student in a course"""
        self.courses.append(course_name)
        self.credits += credit_hours
        print(f'Enrolled in {course_name} ({credit_hours} credits). Total credits: {self.credits}')
    
    def update_gpa(self, new_gpa):
        """Update student's GPA"""
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
            print(f'GPA updated to: {self.gpa:.2f}')
        else:
            print('Invalid GPA. Must be between 0.0 and 4.0')
    
    # Override send_notification for students
    def send_notification(self, message):
        print(f'Student notification to {self.name} ({self.student_number}): {message}')


# Child class: Lecturer
class Lecturer(UniversityMember):
    def __init__(self, member_id, name, email, employee_id, department, salary):
        super().__init__(member_id, name, email)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.courses_taught = []
        self.research_hours = 0
    
    # Override display_info method
    def display_info(self):
        print("=== LECTURER INFORMATION ===")
        super().display_info()
        print(f'Employee ID: {self.employee_id}')
        print(f'Department: {self.department}')
        print(f'Salary: ${self.salary:,.2f}')
        print(f'Research Hours: {self.research_hours}')
        print(f'Courses Taught: {", ".join(self.courses_taught) if self.courses_taught else "None"}')
    
    # New method specific to lecturers
    def assign_course(self, course_name):
        """Assign a course to lecturer"""
        self.courses_taught.append(course_name)
        print(f'Course {course_name} assigned to {self.name}')
    
    def add_research_hours(self, hours):
        """Add research hours"""
        self.research_hours += hours
        print(f'Added {hours} research hours. Total: {self.research_hours} hours')
    
    def calculate_bonus(self, bonus_rate=0.1):
        """Calculate research bonus based on hours"""
        bonus = self.research_hours * self.salary * bonus_rate / 100
        print(f'Research bonus calculated: ${bonus:.2f} (based on {self.research_hours} hours)')
        return bonus
    
    # Override send_notification for lecturers
    def send_notification(self, message):
        print(f'Faculty notification to Prof. {self.name} ({self.department}): {message}')


# Child class: Staff
class Staff(UniversityMember):
    def __init__(self, member_id, name, email, employee_id, position, salary):
        super().__init__(member_id, name, email)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.overtime_hours = 0
        self.tasks = []
    
    # Override display_info method
    def display_info(self):
        print("=== STAFF INFORMATION ===")
        super().display_info()
        print(f'Employee ID: {self.employee_id}')
        print(f'Position: {self.position}')
        print(f'Salary: ${self.salary:,.2f}')
        print(f'Overtime Hours: {self.overtime_hours}')
        print(f'Assigned Tasks: {", ".join(self.tasks) if self.tasks else "None"}')
    
    # New method specific to staff
    def assign_task(self, task_name):
        """Assign a task to staff member"""
        self.tasks.append(task_name)
        print(f'Task "{task_name}" assigned to {self.name}')
    
    def add_overtime(self, hours):
        """Add overtime hours"""
        self.overtime_hours += hours
        print(f'Added {hours} overtime hours. Total: {self.overtime_hours} hours')
    
    def calculate_overtime_pay(self, hourly_rate=25):
        """Calculate overtime pay"""
        overtime_pay = self.overtime_hours * hourly_rate
        print(f'Overtime pay calculated: ${overtime_pay:.2f} ({self.overtime_hours} hours × ${hourly_rate}/hour)')
        return overtime_pay
    
    # Override send_notification for staff
    def send_notification(self, message):
        print(f'Staff notification to {self.name} ({self.position}): {message}')


# Create objects and test functionality
def main():
    print("=== UNIVERSITY MANAGEMENT SYSTEM DEMO ===\n")
    
    # Create different types of university members
    student = Student("STU001", "Alice Johnson", "alice@university.edu", "S12345", "Computer Science")
    lecturer = Lecturer("LEC001", "Dr. Bob Smith", "bob@university.edu", "E67890", "Computer Science", 75000)
    staff = Staff("STA001", "Carol Brown", "carol@university.edu", "E54321", "Administrator", 45000)
    
    # Test Student functionality
    student.display_info()
    student.enroll_course("Data Structures", 3)
    student.enroll_course("Algorithms", 4)
    student.update_gpa(3.7)
    student.send_notification("Assignment due tomorrow!")
    print("\n" + "="*50 + "\n")
    
    # Test Lecturer functionality
    lecturer.display_info()
    lecturer.assign_course("Introduction to Programming")
    lecturer.assign_course("Database Systems")
    lecturer.add_research_hours(120)
    lecturer.calculate_bonus()
    lecturer.send_notification("Faculty meeting at 2 PM")
    print("\n" + "="*50 + "\n")
    
    # Test Staff functionality
    staff.display_info()
    staff.assign_task("Process student applications")
    staff.assign_task("Update course catalog")
    staff.add_overtime(15)
    staff.calculate_overtime_pay()
    staff.send_notification("New policy updates available")
    print("\n" + "="*50 + "\n")
    
    # Test status updates (common functionality)
    print("=== STATUS UPDATES ===")
    student.update_status("On Probation")
    lecturer.update_status("On Sabbatical")
    staff.update_status("Part-time")


if __name__ == "__main__":
    main()

