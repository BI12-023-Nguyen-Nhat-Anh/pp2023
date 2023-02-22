class person:
    id: str
    name: str
    dob: str
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob

    

class sub:
    id: str
    name: str
    def __init__(self,id,name):
        self.id=id
        self.name=name

class student(person):
    def show(self):
        return self.id+","+self.name+","+self.dob

class subject(sub):
    def show(self):
        return self.id+","+self.name

def display(arr1,arr2,arr3):
    for i in range(len(arr1)):
        print("\n"*2)
        print(arr1[i][0]+" "+arr1[i][1]+" "+arr1[i][2]+": ")
        for j in range(len(arr2)):
            print("                       "+arr2[j][0]+" "+arr2[j][1]+": ",end='')
            print(arr3[i][j])

n=int(input("Number of student: "))
arr1=[]
for i in range(n):
    id=input("Student ID: ")
    name=input("Student name: ")
    dob=input("Student dob: ")
    a=student(id,name,dob)
    k=map(str,a.show().split(","))
    arr1.append(list(k))

m=int(input("Number of subject: "))
arr2=[]
for i in range(m):
    id=input("Subject ID: ")
    name=input("Subject name: ")
    a=subject(id,name)
    k=map(str,a.show().split(","))
    arr2.append(list(k))

arr3=[]
for i in range(n):
    point=[]
    for j in range(m):
        k=float(input(arr2[j][1]+" score of stduent "+arr1[i][1]+": "))
        point.append(k)
    arr3.append(point)

display(arr1,arr2,arr3)