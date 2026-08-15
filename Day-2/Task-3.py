#Task-3  Data Validation

students = [
    {"name": "Arun", "mark": 78},
    {"name": "Priya", "mark": 92},
    {"name": "Karthik", "mark": 65},
    {"name": "Divya", "mark": 88},
    {"name": "Santhiya", "mark": 92}
]


def search_student(students, name):

    for student in students:

        if student["name"].lower() == name.lower():

            print("Name:", student["name"])
            print("Mark:", student["mark"])

            return

    print("Student not found")


# Get student name
name = input("Enter student name: ")

# Search
search_student(students, name)