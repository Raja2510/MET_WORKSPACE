in_name=input("enter name : ")
in_grade=input("enter grade : ")

def display_student_info(name,grade):
    print(f"Name: {name}")
    print(f"grade {grade.upper()}")

display_student_info(in_name,in_grade)