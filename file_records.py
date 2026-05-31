# Student Records using CSV

import csv

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        avg = (
            int(row["math"]) +
            int(row["science"]) +
            int(row["english"])
        ) / 3

        grade = calculate_grade(avg)

        results.append({
            "name": row["name"],
            "average": round(avg, 2),
            "grade": grade
        })

with open("results.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "average", "grade"]
    )

    writer.writeheader()
    writer.writerows(results)

print("results.csv created successfully!")