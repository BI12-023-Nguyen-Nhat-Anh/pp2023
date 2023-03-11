#Class person has all the basic human information
class person:
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob

#Class student inherits the name and date of birth attributes from the person and gets the id value
class student(person):
    def __init__(self,id,name,dob):
        super().__init__(name,dob)
        self.id=id
        self.__mark=[]

    def add_mark(self,x):
        self.__mark.append(x)
    
    def get_mark(self):
        return self.__mark

    def show(self):
        return self.id,self.name,self.dob

#Class subject has function to get id and name of subject
class subject:
    def __init__(self,id,name):
        self.__id=id
        self.__name=name

    def get_info(self):
        return self.__id, self.__name
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id

#Display function makes the output easier to see
def display(list_student,list_subject):
    for student in list_student:
        i=0
        print(f"{student.id} {student.name} {student.dob}")
        for subject in list_subject:
            print(f"{subject.get_id()} {subject.get_name()}: {student.get_mark()[i]}")
            i+=1

#list_student and list_subject are used to store all addresses of class student and class subject
n=int(input("Number of student: "))
list_student=[]
for i in range(n):
    id=input("Student's ID: ")
    name=input("Student's name: ")
    dob=input("Student's date of birth: ")
    a=student(id,name,dob)
    list_student.append(a)

m=int(input("Number of subject: "))
list_subject=[]
for i in range(m):
    id=input("Enter course ID: ")
    name=input("Enter course name: ")
    a=subject(id,name)
    list_subject.append(a)

# list_mark=[]
for student in list_student:
    point=[]
    for subject in list_subject:
        i=float(input(f"Score of {subject.get_name()} of student {student.name}: "))
        student.add_mark(i)

display(list_student,list_subject)