class Student:
    def __init__(self, student, grades):
        self.name = student
        self.grades = grades

    def average_grade(self):
        average = sum(self.grades) / len(self.grades)
        return f"{average:.2f}"


 
data = [{"student": "Tom", "grades": [5, 4, 3]},
        {"student": "Alice", "grades": [1, 1, 2]},
        {"student": "Bob", "grades": [5, 1, 2]},
        {"student": "Eve", "grades": [3, 3, 4]},
        {"student": "Charlie", "grades": [4, 5, 3]}]
avg = []

for student_data in data:
    student = Student(student_data["student"], student_data["grades"])
    avg.append({"student": student_data["student"], "average": student.average_grade()})

avg.sort(key=lambda x: x["average"])

print(avg)


    