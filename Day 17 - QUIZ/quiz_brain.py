class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0

    def next_question(self):
        item = self.question_list[self.question_number]
        item.text=item.text.replace("&quot;","'")
        # user_answer=""
        user_answer = input(
            f"Q.{self.question_number+1}: {item.text} (True/False)?: ")
        self.check_answer(user_answer, item.answer)
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if ((user_answer.lower() == correct_answer.lower()) or (user_answer[0].lower() == correct_answer[0].lower())):
            self.user_score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(
            f"Your current score is: {self.user_score}/{self.question_number+1}")
