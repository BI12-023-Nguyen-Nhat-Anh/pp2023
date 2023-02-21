#This function to enter student information
def insert_student(n, student):
    for i in range(n):
        print("Input in the right formular ID,Name,Dob: ",end='')
        k=map(str, input().split(","))
        student.append(list(k))

#This function to enter subject information
def insert_subject(m,subject):
    for i in range(m):
        k=map(str,input("Input the right formula ID,name course: ").split(","))
        subject.append(list(k))

#This function to enter student's score in each course
def insert_mark(n,stduent,subject,mark):
    for i in student:
        point=[]
        for j in subject:
            k=float(input(j[1]+" score of student "+i[1]+": "))
            point.append(k)
        mark.append(point)

#This function to show to people see the information 
def show(student,subject,mark,n,m):
    for i in range(len(student)):
        cnt=0
        print("\n"*2)
        print(student[i])
        for j in range(len(subject)):
            print(str(subject[j][0]),end=' ')
            print(str(subject[j][1])+":",end=' ')
            print(mark[i][cnt])
            cnt+=1

n=int(input("Number of student: "))
student=[]
insert_student(n,student)
subject=[]*2
m=int(input("Number of object: "))
insert_subject(m,subject)
mark=[]
insert_mark(n,student,subject,mark)
show(student,subject,mark,n,m)