def transcript(coursedetails, studentdetails, grades):
    course_dict = dict(coursedetails)
    student_dict = dict(studentdetails)
    
    student_grades = {}
    for rollnumber, coursecode, grade in grades:
        if rollnumber not in student_grades:
            student_grades[rollnumber] = []
        student_grades[rollnumber].append((coursecode, grade))
    
    transcript_list = []
    for rollnumber, name in studentdetails:
        if rollnumber in student_grades:
            student_grades[rollnumber].sort(key=lambda x: x[0])  # Sort grades by course code
            courses_with_grades = [(code, course_dict[code], grade) for code, grade in student_grades[rollnumber]]
            transcript_list.append((rollnumber, name, courses_with_grades))
    
    transcript_list.sort(key=lambda x: x[0])
    
    return transcript_list

print(transcript([("MA101","Calculus"),("PH101","Mechanics"),("HU101","English")],[("UGM2021001","Rohit Grewal"),("UGP2021132","Neha Talwar")],[("UGM2021001","MA101","AB"),("UGP2021132","PH101","B"),("UGM2021001","PH101","B")]))