student_heights=input("Input a list of student heights: ").split() # 180 124 165 173 189 169 146
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)

student_heights_sum=0
for n in range (0, len(student_heights)):
    student_heights_sum+=student_heights[n]
#avg=student_heights_sum//len(student_heights)
avg=round(student_heights_sum/len(student_heights))
print("The average height of the students is: ",avg)