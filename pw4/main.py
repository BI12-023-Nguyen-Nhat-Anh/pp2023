import math
import numpy as np
import input as ip
import output as op

list_student=[]
n=int(input("Number of student: "))
for i in range(n):
    id=input("ID of student: ")
    name=input("Name of student: ")
    dob=input("Student date of birth: ")
    k=ip.students(id,name,dob)
    list_student.append(k)

list_subject=[]
m=int(input("Number of subject: "))
for i in range(m):
    id=input("ID of subject: ")
    name=input("Name of subject: ")
    credit=int(input(f"Credit of {name}: "))
    k=ip.subjects(id,name,credit)
    list_subject.append(k)

for student in list_student:
    point=[]
    for subject in list_subject:
        i=float(input(f"Score of {subject.get_name()} of student {student.get_name()}: "))
        student.add_mark(math.floor(i))

for student in list_student:
    average_mark=[]
    j=0
    for subject in list_subject:
        for i in range(subject.get_credit()):
            average_mark.append(student.get_mark()[j])
        j+=1
    student.add_average(round(np.mean(average_mark,axis=0),1))

show=op.display(list_student,list_subject)