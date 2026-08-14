#Enter a number and check if it is valid age or not


num=int(input("Enter a number: "))
def validate_age(age):
    if age >= 1 and age <= 100:
        return "Valid"
    else:
        return "Invalid"


print(validate_age(num))


#extend validation to check name, age, and mark of a student
name = input("Enter name: ")
age = int(input("Enter age: "))
mark = int(input("Enter mark: "))

def validate_student(name, age, mark):
    if name == "":
        return "Invalid"

    if validate_age(age) == "Invalid":
        return "Invalid"

    if mark < 0 or mark > 100:
        return "Invalid"

    return "Valid"


print(validate_student(name, age, mark))
