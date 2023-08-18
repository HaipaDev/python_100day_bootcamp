# numbers=[1,2,3]
# new_numbers=[n+1 for n in numbers]
# print(new_numbers)

# name="Angela"
# letters_list=[letter for letter in name]
# print(letters_list)

# double=[n*2 for n in range(1,5)]
# print(double)

# new_double=[n*2 for n in range(1,5) if n%2==0]
# print(new_double)


numbers=[1,1,2,3,5,8,13,21,34,55]
squared_numbers=[n**2 for n in numbers]
print(squared_numbers)

even_numbers=[n for n in numbers if n%2==0]
print(even_numbers)

print("\n")
with open("file1.txt") as file1:
    # numbers1=file1.readlines()
    # print([int(n) for n in numbers1])
    numbers1 = [int(n.strip()) for n in file1.readlines()]
    print(numbers1)
    
with open("file2.txt") as file2:
    # numbers2=file2.readlines()
    # print([int(n) for n in numbers2])
    numbers2 = [int(n.strip()) for n in file2.readlines()]
    print(numbers2)
    
numbers_shared=[n for n in numbers1 if n in numbers2]
print(numbers_shared)



## Dictionary Comprehension
print("\n")
import random
names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
student_scores={student:random.randint(1,100) for student in names}
print(student_scores)
passed_students={student:score for (student,score) in student_scores.items() if score>=60}
print(passed_students)

print("\n")
sentence="What is the Airspeed Velocity of an Unladen Swallow?"
word_dict={word:len(word) for word in sentence.split()}
print(word_dict)

print("\n")
weather_c={
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f={day:((temp_c*9/5)+32) for (day,temp_c) in weather_c.items()}
print(weather_f)


print("\n")
student_dict={
    "student": ["Angela","James","Lily"],
    "score": [56,76,98],
}
import pandas
student_data_frame=pandas.DataFrame(student_dict)
for (index,row) in student_data_frame.iterrows():
    print(row.student)
new_dict={index:row for (index,row) in student_data_frame.iterrows()}