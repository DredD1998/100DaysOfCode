import random
name = ["Hirak","Supriya","Priyanka","Dhruv"]

students_score = {student:random.randint(1,100) for student in name}
passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students)


