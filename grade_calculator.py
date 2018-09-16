class Assignment:
    __min__ = 0
    __max__ = 100
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

class User(object):
    def __init__(self, first_name, last_name, ID, password):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.password = password


    def displayUsername(self):
        print self.first_name.lower() + "_" + self.last_name.lower()


    def displayInfo(self):
        print "First name:", self.first_name ,"\n", "Last name:", self.last_name ,"\n", "ID:", self.ID ,"\n", "Username:", User.displayUsername(self),"\n", "Email: ", User.displayEmail(self)

    def displayEmail(self):
        print self.first_name.lower() + "_" + self.last_name.lower() + "@edu.aua.am"

class Student(User):
    def __init__(self, first_name, last_name, ID, password):
        super(Student, self).__init__(first_name, last_name, ID, password)
        self.courses = [ ]


    def addCourse(self, course):
        self.courses.append(course)

    def printCourses(self):
         for k in self.courses:
             k.getInfo()




class Lecturer(User):
    def __init__(self, first_name, last_name, ID, password):
        super(Lecturer, self).__init__(first_name, last_name, ID, password)




class Grade:
    __min__ = 0
    __max__ = 100

    def __init__(self, grade):
                self.__grade__ = grade

    def set_grade(self, grade):
                self.__grade__ = grade

    def get_grade(self):
                print self.__grade__

    def checkIfValidGrade(self):
            if self.__grade__ >= 0 and self.__grade__ <= 100:
                 pass
            else:
                print "Please, enter a grade in range 0-100"


class Course:
    def __init__(self, coursename, course_ID, credits, lecturer):
        self.coursename = coursename
        self.course_ID = course_ID
        self.credits = credits
        self.lecturer = lecturer
        self.assignments = []

    def addAssignments(self, name, percentage, grade, deadline, status, description):
        assignment = Assignment(name, percentage, grade, deadline, status, description)
        self.assignments.append(assignment)

    def displayAssinments(self):
        print "Assignments:"
        print "-----------"
        for k in self.assignments:
            k.getInfo()
            print "-------------"

    def getInfo(self):
           print "Course Name:", self.coursename ,"\n", "Course ID:",self.course_ID ,"\n", "Credits:", self.credits ,"\n", "Lecturer:", self.lecturer
           self.displayAssinments()

    def checkIfValidCourseID(self):
        if len(self.course_ID) == 7:
            pass
        else:
            print "Please, enter valid ID"

    def checkIfValidCredits(self):
        if self.credits >= 1 and self.credits <= 4:
            pass
        else:
            print "Please, enter valid number of credits in a range 1-4"

class AssignmentGrade:

    def __init__(self, course, assignment, grade):
        self.course = course
        self.assignment = assignment
        self.grade = Grade(grade)
        self.state = 0

def main():
    
    #assignment1.getInfo()
    #assignment1.checkIfValidPercentage()
    student = Student("Lina", "Gharagyozyan", "A0987645", "student.displayUsername",)
    #student.displayUsername()
    #student.displayInfo()
    #grade1 = Grade(96)
    #Grade.get_grade(grade1)
    #Grade.checkIfValidGrade(grade1)
    course1 = Course("Data Structures and Algorithms", "ENGS115", 3, "Satenik Mnatsakanyan",)
    course1.addAssignments("Homework", 15, 96, "2018.15.10", "Submitted",
                             "Find technical specification document for your laptop")
    course1.addAssignments("Homework",15,96,"2018.16.12","Submitted","OOP Lectures")
    #course1.getInfo()

    #course1.checkIfValidCourseID()
    #course1.checkIfValidCredits()
    student.addCourse(course1)
    student.printCourses()
    
main()









