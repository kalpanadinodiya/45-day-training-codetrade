# List Comprehension Drills

# 1. Numbers divisible by 3
numbers = list(range(1, 21))
div_by_3 = [x for x in numbers if x % 3 == 0]
print("Divisible by 3:", div_by_3)

# 2. Words longer than 4 characters in title case
words = ["apple", "cat", "banana", "dog", "orange", "book"]
long_words = [word.title() for word in words if len(word) > 4]
print("Long words:", long_words)

# 3. Celsius to Fahrenheit
celsius = [0, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Fahrenheit:", fahrenheit)

# 4. Flatten nested list
nested = [[1, 2], [3, 4], [5, 6], [7, 8]]
flat = [num for sublist in nested for num in sublist]
print("Flattened list:", flat)

# Explore: Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Dictionary Comprehension:", squares)

# Explore: Set Comprehension
unique_lengths = {len(word) for word in words}
print("Set Comprehension:", unique_lengths)