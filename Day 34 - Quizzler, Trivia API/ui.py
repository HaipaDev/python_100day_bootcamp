from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
GREEN_COLOR = "#29b677"
RED_COLOR = "#ee665d"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.on_cooldown = False
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0 / 0 [/{len(self.quiz.question_list)}]", fg="white", bg=THEME_COLOR, font=("Arial",15,""))
        self.score_label.grid(row=0,column=1)

        self.canvas=Canvas(width=300, height=250, bg="white")
        self.question_text=self.canvas.create_text(300/2,250/2,
                                                   width=300-10,
                                                   text="Question Text",
                                                   fill=THEME_COLOR, font=("Arial",20,"italic")
                                                )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        false_img=PhotoImage(file="images/false.png")
        self.false_button=Button(image=false_img, highlightthickness=0, background=THEME_COLOR)
        self.false_button["command"]=self.false_pressed
        self.false_button.grid(row=2,column=0)
        
        true_img=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_img, highlightthickness=0, background=THEME_COLOR)
        self.true_button["command"]=self.true_pressed
        self.true_button.grid(row=2,column=1)

        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.on_cooldown=False
            self.true_button["state"]="active"
            self.false_button["state"]="active"
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end.")
            self.true_button["state"]="disabled"
            self.false_button["state"]="disabled"
    
    def false_pressed(self):
        if not self.on_cooldown:
            self.give_feedback(self.quiz.check_answer("f"))
    
    def true_pressed(self):
        if not self.on_cooldown:
            self.give_feedback(self.quiz.check_answer("t"))

    def give_feedback(self,is_right:bool):
        if(is_right):
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.score_label.config(text=f"Score: {self.quiz.score} / {self.quiz.question_number} [/{len(self.quiz.question_list)}]")
        self.on_cooldown=True
        self.true_button["state"]="disabled"
        self.false_button["state"]="disabled"
        self.window.after(1000,self.get_next_question)