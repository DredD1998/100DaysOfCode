student_dict = {
    "student": ["Hirak","Supriya","Priyanka"],
    "score":[50,99,93]
}


import pandas

student = pandas.DataFrame(student_dict)

for (index,row) in student.iterrows():  
    # print(row)
    if row.student == "Hirak":
        print(row.score)