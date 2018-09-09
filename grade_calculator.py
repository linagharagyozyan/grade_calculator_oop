class Student:
    def __init__(self, first_name, last_name, student_ID, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.student_ID = student_ID
        self.username = username
        self.password = password

    def displayUsername(self):
        self.username = self.first_name + "." + self.last_name


    def displayStudent(self):
        print "First name:", self.first_name ,"\n", "Last name:", self.last_name ,"\n", "ID:", self.student_ID ,"\n", "Username:", self.username


student = Student ("Lina", "Gharagyozyan", "A0987645", "student.displayUsername", "")
student.displayUsername()
student.displayStudent()

class Grade:
    min = 0
    max = 100
    def __init__(self, grade):
     self.grade = grade

    def set_grade(self):
        return 0

    def get_grade(self):
        print self.grade

    def checkIfValidGrade(self):
        if self.grade >= 0 and self.grade <= 100:
            pass
        else:
            print "Please, enter a grade in range 0-100"

grade1 = Grade(96)
Grade.get_grade(grade1)
Grade.checkIfValidGrade(grade1)

class Assignment:
    min = 0
    max = 100
    def __init__(self, name, percentage, grade, deadline, status, description):
        self.name = name
        self.percentage = percentage
        self.grade = grade
        self.deadline = deadline
        self.status = status
        self.description = description

    def getInfo(self):
        print "Name:", self.name ,"\n", "Percentage:", self.percentage ,"\n", "Grade:", self.grade ,"\n", "Deadline:", self.deadline ,"\n", "Status:", self.status ,"\n", "Description:", self.description

    def checkIfValidPercentage(self):
        if self.percentage >= 0 and self.percentage <= 100:
            pass
        else:
            print "Please, enter a percentage in range 0-100"

assignment1 = Assignment ("Homework", 15, 96,"2018.15.10", "Submitted", "Find technical specification document for your laptop")
assignment1.getInfo()
assignment1.checkIfValidPercentage()

class Course:
    def __init__(self, coursename, course_ID, credits, lecturer, assignment):
        self.coursename = coursename
        self.course_ID = course_ID
        self.credits = credits
        self.lecturer = lecturer
        self.assignment = assignment

    def getInfo(self):
           print "Course Name:", self.coursename ,"\n", "Course ID:",self.course_ID ,"\n", "Credits:", self.credits ,"\n", "Lecturer:", self.lecturer ,"\n", "Assignment:", self.assignment

    def checkIfValidCourseID(self):
        if len(course1.course_ID) == 7:
            pass
        else:
            print "Please, enter valid ID"

    def checkIfValidCredits(self):
        if self.credits >= 1 and self.credits <= 4:
            pass
        else:
            print "Please, enter valid number of credits in a range 1-4"

course1 = Course ("Data Structures and Algorithms", "ENGS115", 3, "Satenik Mnatsakanyan", "Homework")
course1.getInfo()
course1.checkIfValidCourseID()
course1.checkIfValidCredits()











