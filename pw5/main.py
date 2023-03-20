import numpy as np
import input as ip
import output as op
import zipfile as file
import os.path

#This is the name of the zip file
zip_name="student.dat"

# #Check if student.dat file exists or not, if yes extract it
if os.path.exists("student.dat"):
    with file.ZipFile("student.dat", 'r') as f:
        f.extractall()
    f.close()
    os.remove("student.dat")

#All this line of code below for upload the data from the file txt
list_student=[]
if os.path.exists("student.txt"):
    with open("student.txt","r") as f:
        arr1=[]
        a=f.read()
        arr=a.split("\n")
        for i in range(len(arr)):
            arr1.append(arr[i].split("_"))
            #Delete empty array
            if(arr[i]==''):
                arr1.pop(i)
    for data in arr1:
        k=ip.students(data[0],data[1],data[2])
        list_student.append(k)
    f.close()
    
list_subject=[]
if os.path.exists("subject.txt"):
    with open("subject.txt","r") as f:
        arr1=[]
        a=f.read()
        arr=a.split("\n")
        for i in range(len(arr)):
            arr1.append(arr[i].split("_"))
            #Delete empty array
            if(arr[i]==''):
                arr1.pop(i)
    for data in arr1:
        k=ip.subjects(data[0],data[1],int(data[2]))
        list_subject.append(k)
    f.close()

if os.path.exists("mark.txt"):
    # Load the data from the mark.txt to the program
    with open("mark.txt","r") as f:
        arr2=[]
        arr1=[]
        a=f.read()
        arr=a.split("\n")
        for i in range(len(arr)):
            if(arr[i]==''):
                arr.pop(i)
    f.close()
    for i in range(len(arr)):
        if(arr[i]==''):
            arr.pop(i)
    for i in arr:
        arr1.append(i.split("_"))
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr2.append(arr1[i][j].split(":"))
    j=0
    for student in list_student:
        for i in range(len(list_subject)+1):
            if("Average mark" in arr2[j]):
                student.add_average(arr2[j][1])
            else:
                student.add_mark(arr2[j][1])
            j+=1

while(True):
    os.system("cls")
    print("+------------------------------------------+")
    print("|      Student and subject information     |")
    print("|             storage system               |")
    print("| 1. Add student                           |")
    print("| 2. Add subject                           |")
    print("| 3. Change mark                           |")
    print("| 4. Show student information              |")
    print("| 5. Show subject information              |")
    print("| 6. Show mark                             |")
    print("| 7. Exit                                  |")
    print("|                              Made by Nanh|")
    print("+------------------------------------------+")
    while(True):
        option=int(input("Your option is: "))
        if(option>=1 and option<=7):
            break
        else:
            print("Error wrong option! Try again.\n")

    if(option==1):
        with open("student.txt","a+") as f:
            n=int(input("Number of student: "))
            for i in range(n):
                id=input("ID of student: ")
                name=input("Name of student: ")
                dob=input("Student date of birth: ")
                k=ip.students(id,name,dob)
                list_student.append(k)
                f.write(k.get_id()+"_"+k.get_name()+"_"+k.get_dob()+"\n")
            f.close()

    if(option==2):
        list_subject=[]
        m=int(input("Number of subject: "))
        with open("subject.txt","a+") as f:
            for i in range(m):
                id=input("ID of subject: ")
                name=input("Name of subject: ")
                credit=int(input(f"Credit of {name}: "))
                k=ip.subjects(id,name,credit)
                list_subject.append(k)
                f.write(k.get_id()+"_"+k.get_name()+"_"+str(k.get_credit())+"\n")
            f.close()

    if(option==3):
        cnt_st=cnt_su=0
        show=op.display_student(list_student)
        n=input("Choose ID of student you want to change mark: ")
        for student in list_student:
            cnt_st+=1
            if(student.get_id()==n):
                show=op.display_subject(list_subject)
                m=input("\nChoose ID of subject you want to change mark: ")
                for subject in list_subject:
                    cnt_su+=1
                    if(subject.get_id()==m):
                        contents=[]
                        with open("mark.txt","r") as f:
                            k=f.read()
                            contents=k.split("\n")
                        f.close()
                        for i in range(len(contents)):
                            if(contents[i]==''):
                                contents.pop(i)
                        if(contents[len(contents)-1]==''):
                            contents.pop(len(contents)-1)
                        i=float(input(f"{subject.get_name()} score of student {student.get_name()}: "))
                        student.change_mark(cnt_su-1,i)

                        average=round(np.mean(student.get_mark(),axis=0),1)
                        student.add_average(average)
                        j=0
                        contents[cnt_st-1]=''
                        for subject in list_subject:
                            contents[cnt_st-1]+=f"{subject.get_name()}:{student.get_mark()[j]}_"
                            j+=1

                        contents[cnt_st-1]+=f"Average mark:{student.get_average()}"
                        with open('mark.txt', 'w') as f:
                            for i in contents:
                                f.write(i+"\n")
                        f.close()

    #Show information of all student
    if(option==4):
        show=op.display_student(list_student)

    #Show information of all subject
    if(option==5):
        show=op.display_subject(list_subject)

    #Show information of all mark
    if(option==6):
        show=op.display_mark(list_student,list_subject)
    
    if(option==7):
        break

    #Ask user want to continue or stop
    ans=input("\nDo you want to continue(y or n): ")
    if(ans=="y" or ans=="Y"):
        continue
    elif(ans=="n" or ans=="N"):
        break
    else:
        print("The anwser is not on the list so the answer default is no")
        break

# #file_list contains the path of all the files to be compressed
file_list=['student.txt','subject.txt','mark.txt']
with file.ZipFile(zip_name,'w') as f:
    for i in file_list:
        f.write(i)
f.close()
# #Remove all file after compressed
for i in file_list:
    os.remove(i)

# I will improve my code in lab work 3 then I will comeback to complete you