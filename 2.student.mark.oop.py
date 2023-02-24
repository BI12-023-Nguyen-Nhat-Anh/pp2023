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

    def show(self):
        return self.id,self.name,self.dob

#Class subject has function to get id and name of subject
class subject:
    __id: str
    __name: str
    def __init__(self,id,name):
        self.__id=id
        self.__name=name

    def get_info(self):
        return self.__id, self.__name

#Display function makes the output easier to see
def display(arr1,arr2,arr3):
    for i in range(len(arr1)):
        print("\n"*2)
        print(arr1[i][0]+" "+arr1[i][1]+" "+arr1[i][2]+": ")
        kc=len(arr1[i][0])+len(arr1[i][1])+len(arr1[i])
        for j in range(len(arr2)):
            print(" "*(kc+3)+arr2[j][0]+" "+arr2[j][1]+": ",end='')
            print(arr3[i][j])

#array 1, array 2, array 3 are used to store all your input information
n=int(input("Number of student: "))
arr1=[]
for i in range(n):
    id=input("Student's ID: ")
    name=input("Student's name: ")
    dob=input("Student's date of birth: ")
    a=student(id,name,dob)
    arr1.append(a.show())

m=int(input("Number of subject: "))
arr2=[]
for i in range(m):
    id=input("Enter course ID: ")
    name=input("Enter course name: ")
    a=subject(id,name)
    arr2.append(a.get_info())

arr3=[]
for i in range(n):
    point=[]
    for j in range(m):
        k=float(input(arr2[j][1]+" score of stduent "+arr1[i][1]+": "))
        point.append(k)
    arr3.append(point)

display(arr1,arr2,arr3)