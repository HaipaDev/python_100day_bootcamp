student_scores=input("Input a list of student scores: ").split() # 78 65 89 86 55 91 64 89
for n in range(0, len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)

student_scores_highest=0
for n in range (0, len(student_scores)):
    if(student_scores[n]>student_scores_highest): student_scores_highest=student_scores[n]
print("The highest score in the class is: ",student_scores_highest)