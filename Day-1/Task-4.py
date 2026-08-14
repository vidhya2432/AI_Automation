#Daily Challenge

marks = [int(x) for x in input("Enter marks of students: ").split()]

# 1. Remove invalid marks
valid_marks = []

for mark in marks:
    if 0 <= mark <= 100:
        valid_marks.append(mark)

print("Valid marks:", valid_marks)


# 2. Remove duplicates
unique_marks = []

for mark in valid_marks:
    if mark not in unique_marks:
        unique_marks.append(mark)

print("Unique marks:", unique_marks)


# 3. Find highest mark
highest = unique_marks[0]

for mark in unique_marks:
    if mark > highest:
        highest = mark

print("Highest mark:", highest)


# 4. Find second highest
second_highest = unique_marks[0]

for mark in unique_marks:
    if mark > second_highest and mark != highest:
        second_highest = mark

print("Second highest:", second_highest)


# 5. Find average
total = 0

for mark in unique_marks:
    total += mark

average = total / len(unique_marks)

print("Average:", average)


# 6. Count students above 75
count = 0

for mark in valid_marks:
    if mark > 75:
        count += 1

print("Students above 75:", count)