from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

WIDTH=200
HEIGHT=224
BG_COLOR=YELLOW
#✔

window=Tk()

reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer",fg=GREEN)
    checkmarks_label["text"]=""
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    long_break_sec=LONG_BREAK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    work_sec=WORK_MIN*60
    # for reps in range(4):
    #     countdown(work_sec)
    #     countdown(short_break_sec)
    # countdown(long_break_sec)
    if reps%8 ==0:
        countdown(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps%2 ==0:
        countdown(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if(count_sec<10):
        count_sec=f"0{count_sec}"
    timer_formatted=f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text,text=timer_formatted)
    if(count>0):
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        if(reps%2==0):
            checkmarks_label["text"]+="✔"
        
# ---------------------------- UI SETUP ------------------------------- #
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=BG_COLOR)

canvas=Canvas(width=WIDTH,height=HEIGHT,bg=BG_COLOR,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(WIDTH/2,HEIGHT/2,image=tomato_img)
timer_text=canvas.create_text(WIDTH/2,HEIGHT/2+28, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

title_label=Label(text="Timer",font=(FONT_NAME,35,"bold"), fg=GREEN, bg=BG_COLOR)
title_label.grid(column=1,row=0)

start_button=Button(text="Start", width=5, font=(FONT_NAME,10), bg=BG_COLOR,highlightthickness=0)
start_button["command"]=start_timer
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset", width=5, font=(FONT_NAME,10), bg=BG_COLOR,highlightthickness=0)
reset_button["command"]=reset
reset_button.grid(column=2,row=2)

checkmarks_label=Label(font=(FONT_NAME,10), fg=GREEN, bg=BG_COLOR)
checkmarks_label.grid(column=1,row=3)




window.mainloop()