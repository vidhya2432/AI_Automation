## Find the largest, smallest, and average of a list of numbers

numbers = [int(x) for x in input("Enter numbers: ").split()]

largest = numbers[0]
smallest = numbers[0]
total = 0

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

    total += num

average = total / len(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)