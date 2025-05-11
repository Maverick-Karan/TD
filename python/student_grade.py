# Initialize the dictionary
# Key is the name of the student, value is the grade of the student
student_grades = {
    "John": "A",
    "Gina": "C",
    "Cathy": "B",
    "David": "D",
    "Eric": "F",
    "Alice": "A",
    "Bob": "C",
    "Helen": "F"
}

# Printing the options
print("Choose an option:")
print("1. Add a new student and grade")
print("2. Update an existing student's grade")
print("3. Print all students and their grades")

# Getting the input from the user
option = input("Enter your choice: ")

# Logic for the options
#Adding a new student and grade
if option == "1":
    name = input("Enter the name of the student: ")
    if name in student_grades:
        print("Student already exists")
    else:
        grade = input("Enter the grade of the student: ")
        student_grades[name] = grade
        print(f"Added {name}: {grade}")
#Updating an existing student's grade
elif option == "2":
    name = input("Enter the name of the student: ")
    if name in student_grades:
        new_grade = input("Enter new grade: ")
        student_grades[name] = new_grade
        print(f"Grade updated for {name}: {new_grade}")
    else:
        print("Student not found.")
#Printing all students and their grades     
elif option == "3":
    print("Printing all student grades:")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")
#Invalid choice
else:
    print("Invalid choice.")