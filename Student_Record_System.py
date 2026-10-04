# Mini Project   Student Record System 

students = []


def add_student():

    student = {
        "name": input("Name: "),
        "age": input("Age: "),
        "degree": input("Degree: "),
        "field": input("Field: "),
        "cgpa": input("CGPA: ")


    }

    students.append(student)

    print("Student Added Successfully!")


def view_students():

    print("\n--- Student Records---")

    for student in students:
        print("student")


def search_student():

    search_student_name = input("Enter Student Name To Search: ")

    for student in students:
        if student["name"].lower() == search_student_name.lower():
            print("\n Student Found!")
            print(student)
            return
        
        
    print("Student Not Found!")


def delete_student():

    delete_student_name = input("Enter Student Name to Delete: ")

    for student in students:
        if student["name"].lower() == delete_student.lower():
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


while True:
    print("\n--- Student Record System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")



add_student()
view_students()
search_student()
delete_student()