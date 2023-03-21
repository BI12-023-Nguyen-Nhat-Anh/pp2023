import math
import numpy as np
#Class person has all the basic human information
class person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob

#Class student inherits the name and date of birth attributes from the person and gets the id value
class students(person):
    def __init__(self,id,name,dob):
        super().__init__(name,dob)
        self.id=id
        self.__mark={}
        self.__average=0


    def add_mark(self,n,x):
        self.__mark[n]=x
    
    def get_mark(self):
        return self.__mark

    def add_average(self,x):
        self.__average=x

    def get_average(self):
        return self.__average
    
    def show(self):
        return self.id,self.name,self.dob

#Class subject has function to get id and name of subject
class subjects:
    def __init__(self,id,name,credit):
        self.__id=id
        self.__name=name
        self.__credit=credit

    def get_info(self):
        return self.__id, self.__name, self.__crerdit
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_credit(self):
        return self.__credit

#Display function makes the output easier to see
def display(list_student,list_subject):
    for student in list_student:
        i=0
        print(f"\n{student.id} {student.name} {student.dob}")
        for subject in list_subject:
            print(f"{subject.get_id()} {subject.get_name()}: {student.get_mark()[subject.get_name()]}")
            i+=1
        print(f"Average of student {student.name} {student.get_average()}")

#list_student and list_subject are used to store all addresses of class student and class subject
n=int(input("Number of student: "))
list_student=[]
for i in range(n):
    id=input("Student's ID: ")
    name=input("Student's name: ")
    dob=input("Student's date of birth: ")
    a=students(id,name,dob)
    list_student.append(a)

m=int(input("Number of subject: "))
list_subject=[]
for i in range(m):
    id=input("Enter course ID: ")
    name=input("Enter course name: ")
    credit=int(input(f"Number of credits of the {name}: "))
    a=subjects(id,name,credit)
    list_subject.append(a)

for student in list_student:
    for subject in list_subject:
        i=float(input(f"Score of {subject.get_name()} of student {student.name}: "))
        student.add_mark(f"{subject.get_name()}",math.floor(i))

for student in list_student:
    average_mark=[]
    for subject in list_subject:
        for i in range(subject.get_credit()):
            average_mark.append(student.get_mark()[subject.get_name()])
    student.add_average(round(np.mean(average_mark,axis=0),1)) #This line for calculate the average mark of each student round function for round 1 number after comma

#This line help me to overwrite the list_student in descending order
list_student=sorted(list_student,key=lambda x: x.get_average(), reverse=True)

display(list_student,list_subject)