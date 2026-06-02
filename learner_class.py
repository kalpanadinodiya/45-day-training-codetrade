class Learner:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def get_info(self):
        return f"{self.name} is enrolled in {self.course}."

student = Learner("Kalpana", "BTech CSE")

print(student.get_info())