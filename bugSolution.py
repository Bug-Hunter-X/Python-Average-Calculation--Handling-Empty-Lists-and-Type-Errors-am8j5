def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 #Handle list with no numbers
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 0, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 'a', 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}") #This will output 0 as only numbers are considered 