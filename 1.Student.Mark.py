def insert_student(n, student):
    for i in range(n):
        print("Input in the right formular ID,Name,Dob: ",end='')
        k=map(str, input().split(","))
        student.append(list(k))

def insert_subject(m,subject):
    for i in range(m):
        k=map(str,input("Input the right formula ID,name course: ").split(","))
        subject.append(list(k))

def insert_mark(n,stduent,subject,mark):
    for i in student:
        point=[]
        for j in subject:
            k=float(input(j[1]+" score of student "+i[1]+": "))
            point.append(k)
        mark.append(point)

n=int(input("Number of student: "))
student=[]
insert_student(n,student)
subject=[]*2
m=int(input("Number of object: "))
insert_subject(m,subject)
mark=[]
insert_mark(n,student,subject,mark)
print(student)
print(subject)
print(mark)