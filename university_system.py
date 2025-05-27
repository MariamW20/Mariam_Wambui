"""
University System - User can input and manage Person, Student, Lecturer, Staff
Demonstrates inheritance, method overriding, and polymorphism with user interaction
"""

from datetime import datetime
from typing import List
import os


class Person:
    """Base Person class - parent class for all university members"""
    
    def __init__(self, person_id: str, name: str, age: int, email: str):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email
        self.join_date = datetime.now().strftime("%Y-%m-%d")
    
    def display_info(self):
        """Display basic person information"""
        print(f"Person ID: {self.person_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Join Date: {self.join_date}")
    
    def get_role(self):
        """Return the role of the person"""
        return "Person"
    
    def __str__(self):
        return f"{self.get_role()}: {self.name} (ID: {self.person_id})"


class Student(Person):
    """Student class - inherits from Person"""
    
    def __init__(self, person_id: str, name: str, age: int, email: str, 
                 student_number: str, major: str, year: int, gpa: float = 0.0):
        super().__init__(person_id, name, age, email)
        self.student_number = student_number
        self.major = major
        self.year = year
        self.gpa = gpa
        self.enrolled_courses = []
    
    def display_info(self):
        """OVERRIDDEN: Display student-specific information"""
        print("=" * 50)
        print("STUDENT INFORMATION")
        print("=" * 50)
        super().display_info()
        print(f"Student Number: {self.student_number}")
        print(f"Major: {self.major}")
        print(f"Year: {self.year}")
        print(f"GPA: {self.gpa:.2f}")
        if self.enrolled_courses:
            print(f"Enrolled Courses: {', '.join(self.enrolled_courses)}")
        else:
            print("Enrolled Courses: None")
        print("=" * 50)
    
    def get_role(self):
        return "Student"


class Lecturer(Person):
    """Lecturer class - inherits from Person"""
    
    def __init__(self, person_id: str, name: str, age: int, email: str,
                 employee_id: str, department: str, salary: float, 
                 specialization: str):
        super().__init__(person_id, name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.specialization = specialization
        self.courses_taught = []
    
    def display_info(self):
        """OVERRIDDEN: Display lecturer-specific information"""
        print("=" * 50)
        print("LECTURER INFORMATION")
        print("=" * 50)
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Specialization: {self.specialization}")
        if self.courses_taught:
            print(f"Courses Taught: {', '.join(self.courses_taught)}")
        else:
            print("Courses Taught: None")
        print("=" * 50)
    
    def get_role(self):
        return "Lecturer"


class Staff(Person):
    """Staff class - inherits from Person"""
    
    def __init__(self, person_id: str, name: str, age: int, email: str,
                 employee_id: str, department: str, salary: float, 
                 position: str, work_hours: int = 40):
        super().__init__(person_id, name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
        self.position = position
        self.work_hours = work_hours
        self.responsibilities = []
    
    def display_info(self):
        """OVERRIDDEN: Display staff-specific information"""
        print("=" * 50)
        print("STAFF INFORMATION")
        print("=" * 50)
        super().display_info()
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:,.2f}")
        print(f"Work Hours/Week: {self.work_hours}")
        if self.responsibilities:
            print(f"Responsibilities: {', '.join(self.responsibilities)}")
        else:
            print("Responsibilities: None assigned")
        print("=" * 50)
    
    def get_role(self):
        return "Staff"


class UniversitySystem:
    """ University Management System"""
    
    def __init__(self, university_name: str):
        self.university_name = university_name
        self.members: List[Person] = []
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display system header"""
        print("=" * 60)
        print(f"🎓 {self.university_name.upper()} MANAGEMENT SYSTEM 🎓")
        print("=" * 60)
        print(f"Total Members: {len(self.members)}")
        students = len([m for m in self.members if isinstance(m, Student)])
        lecturers = len([m for m in self.members if isinstance(m, Lecturer)])
        staff = len([m for m in self.members if isinstance(m, Staff)])
        others = len([m for m in self.members if type(m) == Person])
        print(f"Students: {students} | Lecturers: {lecturers} | Staff: {staff} | Others: {others}")
        print("=" * 60)
    
    def main_menu(self):
        """Display main menu and handle user choice"""
        while True:
            self.clear_screen()
            self.display_header()
            
            print("\n MAIN MENU:")
            print("1. Add New Member")
            print("2. View All Members")
            print("3. Search Member")
            print("4. View by Role")
            print("5. Remove Member")
            print("6. Exit System")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                self.add_member_menu()
            elif choice == '2':
                self.view_all_members()
            elif choice == '3':
                self.search_member()
            elif choice == '4':
                self.view_by_role_menu()
            elif choice == '5':
                self.remove_member()
            elif choice == '6':
                print("\n Thank you for using the University System!")
                break
            else:
                print("\n Invalid choice! Please try again.")
                input("Press Enter to continue...")
    
    def add_member_menu(self):
        """Menu for adding new members"""
        self.clear_screen()
        self.display_header()
        
        print("\n ADD NEW MEMBER")
        print("1. Add Student")
        print("2. Add Lecturer")
        print("3. Add Staff")
        print("4. Add Person")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            self.add_student()
        elif choice == '2':
            self.add_lecturer()
        elif choice == '3':
            self.add_staff()
        elif choice == '4':
            self.add_person()
        elif choice == '5':
            return
        else:
            print("\n Invalid choice!")
            input("Press Enter to continue...")
    
    def get_basic_info(self):
        """Get basic person information from user"""
        print("\n Enter Basic Information:")
        
        while True:
            person_id = input("Person ID: ").strip()
            if person_id and not self.find_member(person_id):
                break
            elif not person_id:
                print(" Person ID cannot be empty!")
            else:
                print(" Person ID already exists!")
        
        name = input("Full Name: ").strip()
        while not name:
            print(" Name cannot be empty!")
            name = input("Full Name: ").strip()
        
        while True:
            try:
                age = int(input("Age: "))
                if age > 0:
                    break
                else:
                    print(" Age must be positive!")
            except ValueError:
                print(" Please enter a valid number!")
        
        email = input("Email: ").strip()
        while not email:
            print(" Email cannot be empty!")
            email = input("Email: ").strip()
        
        return person_id, name, age, email
    
    def add_student(self):
        """Add a new student"""
        self.clear_screen()
        self.display_header()
        print("\n ADD NEW STUDENT")
        
        try:
            person_id, name, age, email = self.get_basic_info()
            
            print("\n Student Specific Information:")
            student_number = input("Student Number: ").strip()
            while not student_number:
                print(" Student number cannot be empty!")
                student_number = input("Student Number: ").strip()
            
            major = input("Major: ").strip()
            while not major:
                print(" Major cannot be empty!")
                major = input("Major: ").strip()
            
            while True:
                try:
                    year = int(input("Year (1-4): "))
                    if 1 <= year <= 4:
                        break
                    else:
                        print("Year must be between 1 and 4!")
                except ValueError:
                    print("Please enter a valid number!")
            
            while True:
                try:
                    gpa = float(input("GPA (0.0-4.0): "))
                    if 0.0 <= gpa <= 4.0:
                        break
                    else:
                        print("GPA must be between 0.0 and 4.0!")
                except ValueError:
                    print("Please enter a valid number!")
            
            student = Student(person_id, name, age, email, student_number, major, year, gpa)
            self.members.append(student)
            
            print(f"\n Student {name} added successfully!")
            
        except KeyboardInterrupt:
            print("\n Operation cancelled!")
        
        input("Press Enter to continue...")
    
    def add_lecturer(self):
        """Add a new lecturer"""
        self.clear_screen()
        self.display_header()
        print("\n ADD NEW LECTURER")
        
        try:
            person_id, name, age, email = self.get_basic_info()
            
            print("\n Employment Information:")
            employee_id = input("Employee ID: ").strip()
            while not employee_id:
                print("Employee ID cannot be empty!")
                employee_id = input("Employee ID: ").strip()
            
            department = input("Department: ").strip()
            while not department:
                print("Department cannot be empty!")
                department = input("Department: ").strip()
            
            while True:
                try:
                    salary = float(input("Salary: $"))
                    if salary > 0:
                        break
                    else:
                        print("Salary must be positive!")
                except ValueError:
                    print("Please enter a valid number!")
            
            specialization = input("Specialization: ").strip()
            while not specialization:
                print("Specialization cannot be empty!")
                specialization = input("Specialization: ").strip()
            
            lecturer = Lecturer(person_id, name, age, email, employee_id, department, salary, specialization)
            self.members.append(lecturer)
            
            print(f"\n Lecturer {name} added successfully!")
            
        except KeyboardInterrupt:
            print("\n Operation cancelled!")
        
        input("Press Enter to continue...")
    
    def add_staff(self):
        """Add a new staff member"""
        self.clear_screen()
        self.display_header()
        print("\n ADD NEW STAFF")
        
        try:
            person_id, name, age, email = self.get_basic_info()
            
            print("\n Employment Information:")
            employee_id = input("Employee ID: ").strip()
            while not employee_id:
                print("Employee ID cannot be empty!")
                employee_id = input("Employee ID: ").strip()
            
            department = input("Department: ").strip()
            while not department:
                print("Department cannot be empty!")
                department = input("Department: ").strip()
            
            while True:
                try:
                    salary = float(input("Salary: $"))
                    if salary > 0:
                        break
                    else:
                        print("Salary must be positive!")
                except ValueError:
                    print("Please enter a valid number!")
            
            position = input("Position: ").strip()
            while not position:
                print("Position cannot be empty!")
                position = input("Position: ").strip()
            
            while True:
                try:
                    work_hours = int(input("Work Hours per Week (default 40): ") or "40")
                    if work_hours > 0:
                        break
                    else:
                        print("Work hours must be positive!")
                except ValueError:
                    print("Please enter a valid number!")
            
            staff = Staff(person_id, name, age, email, employee_id, department, salary, position, work_hours)
            self.members.append(staff)
            
            print(f"\n Staff {name} added successfully!")
            
        except KeyboardInterrupt:
            print("\n Operation cancelled!")
        
        input("Press Enter to continue...")
    
    def add_person(self):
        """Add a basic person"""
        self.clear_screen()
        self.display_header()
        print("\n ADD NEW PERSON")
        
        try:
            person_id, name, age, email = self.get_basic_info()
            
            person = Person(person_id, name, age, email)
            self.members.append(person)
            
            print(f"\n Person {name} added successfully!")
            
        except KeyboardInterrupt:
            print("\n Operation cancelled!")
        
        input("Press Enter to continue...")
    
    def view_all_members(self):
        """View all members in the system"""
        self.clear_screen()
        self.display_header()
        
        if not self.members:
            print("\n No members in the system yet!")
            input("Press Enter to continue...")
            return
        
        print(f"\n ALL MEMBERS ({len(self.members)} total):")
        print("-" * 60)
        
        for i, member in enumerate(self.members, 1):
            print(f"\n[{i}] {member}")
            member.display_info()
        
        input("\nPress Enter to continue...")
    
    def search_member(self):
        """Search for a specific member"""
        self.clear_screen()
        self.display_header()
        
        if not self.members:
            print("\n No members in the system yet!")
            input("Press Enter to continue...")
            return
        
        search_id = input("\n Enter Person ID to search: ").strip()
        
        member = self.find_member(search_id)
        if member:
            print(f"\n Member Found:")
            member.display_info()
        else:
            print(f"\n No member found with ID: {search_id}")
        
        input("Press Enter to continue...")
    
    def view_by_role_menu(self):
        """Menu to view members by role"""
        self.clear_screen()
        self.display_header()
        
        print("\n VIEW BY ROLE:")
        print("1. Students")
        print("2. Lecturers") 
        print("3. Staff")
        print("4. Others")
        print("5. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        role_map = {
            '1': 'Student',
            '2': 'Lecturer',
            '3': 'Staff',
            '4': 'Person'
        }
        
        if choice in role_map:
            self.view_by_role(role_map[choice])
        elif choice == '5':
            return
        else:
            print("\n Invalid choice!")
            input("Press Enter to continue...")
    
    def view_by_role(self, role: str):
        """View members by specific role"""
        self.clear_screen()
        self.display_header()
        
        if role == 'Student':
            role_members = [m for m in self.members if isinstance(m, Student)]
        elif role == 'Lecturer':
            role_members = [m for m in self.members if isinstance(m, Lecturer)]
        elif role == 'Staff':
            role_members = [m for m in self.members if isinstance(m, Staff)]
        else:  # Person
            role_members = [m for m in self.members if type(m) == Person]
        
        print(f"\n {role.upper()}S ({len(role_members)} found):")
        print("-" * 60)
        
        if not role_members:
            print(f"No {role.lower()}s found in the system.")
        else:
            for i, member in enumerate(role_members, 1):
                print(f"\n[{i}]")
                member.display_info()
        
        input("Press Enter to continue...")
    
    def remove_member(self):
        """Remove a member from the system"""
        self.clear_screen()
        self.display_header()
        
        if not self.members:
            print("\n No members in the system yet!")
            input("Press Enter to continue...")
            return
        
        remove_id = input("\n Enter Person ID to remove: ").strip()
        
        member = self.find_member(remove_id)
        if member:
            print(f"\n Are you sure you want to remove:")
            member.display_info()
            
            confirm = input("\nType 'YES' to confirm removal: ").strip().upper()
            if confirm == 'YES':
                self.members.remove(member)
                print(f"\n {member.name} removed successfully!")
            else:
                print("\n Removal cancelled!")
        else:
            print(f"\n No member found with ID: {remove_id}")
        
        input("Press Enter to continue...")
    
    def find_member(self, person_id: str):
        """Find a member by person ID"""
        for member in self.members:
            if member.person_id == person_id:
                return member
        return None


def main():
    """Main function to start the university system"""
    print(" Welcome to the University System! ")
    
    university_name = input("Enter University Name: ").strip()
    if not university_name:
        university_name = "Tech University"
    
    system = UniversitySystem(university_name)
    system.main_menu()


if __name__ == "__main__":
    main()