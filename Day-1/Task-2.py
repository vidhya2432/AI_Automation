## Find the Second Largest Number in Python without using sort() function
##numbers = [10, 45, 23, 89, 45, 12]

numbers = [int(x) for x in input("Enter numbers: ").split()]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)


# using sort function
#numbers = [10, 25, 5, 40, 15]
#numbers.sort()
#print("Second Largest:", numbers[-2]) 