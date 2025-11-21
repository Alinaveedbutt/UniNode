class Person:
    def __init__(self, name = "", personID = 0):
        self.name = name
        self.personID = personID

    def display(self):
        print(f"Name: {self.name}")
        print(f"Person ID: {self.personID}")

    def write_to_file(self, file):
        file.write(f"Name: {self.name}\n")
        file.write(f"Person ID: {self.personID}\n")

class Student(Person):
    def __init__(self, name = "", personID = 0, programEnrolled = "", semester = 0):
        super().__init__(name, personID)
        self.programEnrolled = programEnrolled
        self.semester = semester

    def display(self):
        super().display()
        print(f"Program Enrolled: {self.programEnrolled}")
        print(f"Semester : {self.semester}")

    def write_to_file(self,file):
        file.write(f"Program Enrolled : {self.programEnrolled}\n")
        file.write(f"Semester : {self.semester}\n")

class Faculty(Person):
    def __init__(self, name = "", personID = 0, department = "", coursesTeaching = 0):
        super().__init__(name, personID)
        self.department = department 
        self.coursesTeaching = coursesTeaching
    
    def display(self):
        super().display()
        print(f"Department : {self.department}")
        print(f"Courses Teaching : {self.coursesTeaching}")

    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f"Department: {self.department}\n")
        file.write(f"Courses Teaching: {self.coursesTeaching}\n")

class Visitor(Person):
    def __init__(self, name = "", personID = 0, visitPurpose = "", visitDuration = 0):
        super().__init__(name, personID)
        self.visitPurpose = visitPurpose
        self.visitDuration = visitDuration

    def display(self):
        super().display()
        print(f"Visit Purpose: {self.visitPurpose}")
        print(f"Visit Duration: {self.visitDuration} day(s)")
        
    def write_to_file(self, file):
        super().write_to_file(file)
        file.write(f"Visiting Purpose: {self.visitPurpose}\n")
        file.write(f"Visiting Duration: {self.visitDuration} day(s)\n")
        
def main():
    people = []

    while True:
        print("\n Menu: \n")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. Add Visitor")
        print("4. Display All")
        print("5. Save to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            personID = int(input("Enter person ID: "))
            programEnrolled = input("Enter program enrolled: ")
            semester = int(input("Enter semester: "))
            student = Student(name, personID, programEnrolled, semester)
            people.append(student)

        elif choice == "2":
            name = input("Enter name: ")
            personID = int(input("Enter person ID: "))
            department = input("Enter department: ")
            coursesTeaching = int(input("Enter number of courses teaching: "))
            faculty = Faculty(name, personID, department, coursesTeaching)
            people.append(faculty)

        elif choice == "3":
            name = input("Enter name: ")
            personID = int(input("Enter person ID: "))
            visitPurpose = input("Enter visiting Purpose: ")
            visitDuration = int(input("Enter visitng Duration (in days): "))
            visitor = Visitor(name, personID , visitPurpose, visitDuration)
            people.append(visitor)
        
        elif choice == "4":
            for person in people:
                person.display()

        elif choice == "5": 
            with open("people.txt", "w" ) as file:
                for person in people:
                    person.write_to_file(file)
                    file.write("\n")
            print("Data saved to people.txt")
        
        elif choice == "6":
            print("Exiting the program....")
            break
    
        else:
            print("Invalid choice. Please try again")
    
main()
