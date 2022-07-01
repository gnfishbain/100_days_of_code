student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for item in student_scores:
    student_grades = {item: (studen t_scores[item])}
    if student_scores[item] < 70:
        student_grades[item] = "Fail"
    elif student_scores[item] < 81:
        student_grades[item] = "Acceptable"
    elif student_scores[item] <91:
        student_grades[item] = "Exceeds Expectations"
    elif student_scores[item] < 100:
        student_grades[item] = "Outstanding"

    #(student_scores[item])
    print (student_grades)

# 🚨 Don't change the code below 👇
print(student_grades)


"""
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
"""



