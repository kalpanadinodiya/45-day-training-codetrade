# Pandas DataFrame Practice

import pandas as pd

data = {
    "name": ["Kalpana", "Rahul", "Priya", "Aman", "Neha",
             "Riya", "Karan", "Anjali", "Vikas", "Pooja"],

    "city": ["Delhi", "Mumbai", "Delhi", "Jaipur", "Mumbai",
             "Jaipur", "Delhi", "Mumbai", "Jaipur", "Delhi"],

    "math_score": [90, 78, 95, 65, 88, 72, 81, 76, 69, 92],

    "science_score": [85, 80, 91, 70, 84, 75, 79, 82, 73, 89],

    "english_score": [88, 74, 93, 68, 86, 78, 80, 85, 71, 90]
}

df = pd.DataFrame(data)

# 1. Average score in each subject
print("Average Scores:")
print(df[["math_score", "science_score", "english_score"]].mean())

# 2. Student with highest total score
df["total"] = (
    df["math_score"]
    + df["science_score"]
    + df["english_score"]
)

top_student = df.loc[df["total"].idxmax()]
print("\nTop Student:")
print(top_student)

# 3. Students from each city
print("\nStudents per City:")
print(df["city"].value_counts())

# 4. Students with math score > 75
print("\nMath Score > 75:")
print(df[df["math_score"] > 75])

# Explore: Top 3 students
print("\nTop 3 Students:")
print(df.nlargest(3, "total")[["name", "total"]])