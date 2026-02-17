data = {"student": "Tom", "grades": [5, 4, 3]}

def average_grade(student_data):
    grades = student_data["grades"]
    average = sum(grades) / len(grades)
    return average

avg = average_grade(data)

if avg >= 4.3:
    print(f"{data['student']} has not passed, average grade: {avg:.2f}.")
else:
    print(f"{data['student']} has passed, average grade: {avg:.2f}.")