from question_model import Question
from data import question_data
from trivia_data import trivia_data
from quiz_brain import QuizBrain
# import random

question_bank=[]

question_bank_id=0
if(question_bank_id==1):
    for q in trivia_data:
        question_bank.append(Question(q["question"],q["correct_answer"]))
else:
    for q in question_data:
        question_bank.append(Question(q["text"],q["answer"]))

quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.user_score}/{quiz.question_number+1}")