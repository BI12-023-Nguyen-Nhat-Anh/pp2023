n=int(input("Number of student: "))
sinhvien_name=[]
sinhvien_id=[]
sinhvien_dob=[]
for i in range(n):
    k=input("ID of student "+str(i+1)+": ")
    sinhvien_id.append(k)
    k=input("Name of student "+str(i+1)+": ")
    sinhvien_name.append(k)
    k=input("Date of birth of student "+str(i+1)+": ")
    sinhvien_dob.append(k)

m=int(input("Number of course: "))
course_id=[]
course_name=[]
for i in range(m):
    k=input("ID of course "+str(i+1)+": ")
    course_id.append(k)
    k=input("Name of course: ")
    course_name.append(k)

diem=[]
for i in range(m):
    for j in range(n):
        k=float(input(course_name[i]+" score of "+sinhvien_name[j]+": "))
        diem.append(k)

cnt=0

print("\n")
print("List of student:")
for i in range(n):
    print(sinhvien_id[i],sinhvien_name[i],sinhvien_dob[i])

for i in range(m):
    print("ID course:",course_id[i])
    print("Name course:",course_name[i])
    for j in range(n):
        print(sinhvien_id[j],sinhvien_name[j]+": ",diem[cnt])
        cnt+=1        