# Task-2 - Student Database

students = [
    {"name": "Arun", "mark": 78},
    {"name": "Priya", "mark": 92},
    {"name": "Karthik", "mark": 65},
    {"name": "Divya", "mark": 88}
]

# 1. Find Topper


def find_topper(students):

    topper = students[0]

    for student in students:

        if student["mark"] > topper["mark"]:
            topper = student

    return topper

# 2. Find Average


def find_average(students):

    total = 0

    for student in students:
        total += student["mark"]

    average = total / len(students)

    return average

# 3. Find Students Above 80


def students_above_80(students):

    result = []

    for student in students:

        if student["mark"] > 80:
            result.append(student)

    return result

# 4. Find Lowest Scorer


def find_lowest(students):

    lowest = students[0]

    for student in students:

        if student["mark"] < lowest["mark"]:
            lowest = student

    return lowest


# 5. Count Students Above Average


def count_above_average(students):

    average = find_average(students)

    count = 0

    for student in students:

        if student["mark"] > average:
            count += 1

    return count


# Call Functions


topper = find_topper(students)

average = find_average(students)

above_80 = students_above_80(students)

lowest = find_lowest(students)

above_average_count = count_above_average(students)



print("Topper:", topper["name"], "-", topper["mark"])

print("Average:", round(average, 2))

print("\nStudents above 80:")

for student in above_80:
    print(student["name"], "-", student["mark"])

print("\nLowest scorer:", lowest["name"], "-", lowest["mark"])

print("\nStudents above average:", above_average_count)
