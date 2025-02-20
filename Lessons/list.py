# There is a concise way to creat list
# [expression for value in iterable if condition]

# EXAMPLE
# doubles = [x * 2 for x in range(1,11)]
# print(doubles)

# fruits = ["coconut", "banana", "watermelon", "orange"]
# fruits = [fruit.capitalize() for fruit in fruits]
# print(fruits)

# numbers = [1, -2, 3, -4, 5, -6]
# positiveNumbers = [num for num in numbers if num >= 0]
# print(positiveNumbers)

grades = [85, 42, 79, 90, 56, 61, 30]
passingGrades = [grade for grade in grades if grade >= 60]
print(passingGrades)