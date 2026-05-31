students = [
    {"name": "Aman", "score": 90},
    {"name": "Riya", "score": 80},
    {"name": "Rahul", "score": 70},
    {"name": "Sneha", "score": 60},
    {"name": "Karan", "score": 40}
]

def classify(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"

for student in students:
    print(student["name"], classify(student["score"]))