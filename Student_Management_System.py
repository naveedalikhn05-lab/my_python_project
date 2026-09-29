# Mini Project 3    Student management system


students = []


# Add Student

def add_student():
    student = {
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "degree": input("Degree: "), 
        "field": input("Field: "),
        "cgpa": float(input("CGPA: "))
    }

    students.append(student)
    print("Student Added Successfully!")


# View All Students 

def view_students():
    for student in students:
        print(student)


# Search Student 

def search_student():
    search_name = input("Enter Name: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            print(student)
            return

    print("Student Not Found!")


# Delete Student 

def delete_student():
    delete_name = input("Enter Name: ")

    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print("Student Deleted Successfully!")
            return

    print("Student Not Found!")


# Handle The Choice 

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid Choice!")


print(students)

