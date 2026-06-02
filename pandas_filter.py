import pandas as pd

df = pd.read_csv(r"c:\Users\kalpa\Desktop\aiml-crash-kalpana\students.csv")

# Select specific columns
selected = df[["name", "math", "science"]]

print("Selected Columns:")
print(selected)

# Filter students with math marks greater than 80
filtered = df[df["math"] > 80]

print("\nStudents with Math > 80:")
print(filtered)