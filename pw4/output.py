def display(list_student,list_subject):
    for student in list_student:
        i=0
        print(f"\n{student.get_id()} {student.get_name()} {student.get_dob()}")
        for subject in list_subject:
            print(f"{subject.get_id()} {subject.get_name()}: {student.get_mark()[i]}")
            i+=1
        print(f"Average of student {student.get_name()} {student.get_average()}")