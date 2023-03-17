def display_student(list_student):
    for student in list_student:
        print(f"Student ID: {student.get_id()}\nStudent name: {student.get_name()}\nStudent date of birth: {student.get_dob()}\n")

def display_subject(list_subject):
    for subject in list_subject:
        print(f"Subjetc ID: {subject.get_id()}\nName of subject: {subject.get_name()}\nNumber of credits: {subject.get_credit()}\n")   

def display_mark(list_student, list_subject):
    for student in list_student:
        i=0
        print(f"\nStudent ID: {student.get_id()}\nStudent name: {student.get_name()}")
        for subject in list_subject:
            print(f"{subject.get_id()} {subject.get_name()}: {student.get_mark()[i]}")
            i+=1
        print(f"Average of student {student.get_name()} {student.get_average()}")