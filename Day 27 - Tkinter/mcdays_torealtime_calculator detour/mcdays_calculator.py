from tkinter import *

TICKS_IN_SECOND=20
TICKS_IN_MCDAY=24000
days=1
minutes=0
hours=0

window=Tk()
window.title("test")
window.minsize(500,300)
window.config(padx=20,pady=20)

label=Label(text="How many days in Minecraft\nto calculate into minutes:",font=("Comic Sans MS",24))
label.pack()

def calculate(event=None):
    global days,minutes,hours
    days=int(_input.get())
    seconds=(days*TICKS_IN_MCDAY)/TICKS_IN_SECOND
    minutes=round(seconds/60,2)
    hours=round(minutes/60,2)
    if(days==1):
        output_label["text"]=f"{days} minecraft day\nis {minutes}min (or {hours}h)"
    else:
        output_label["text"]=f"{days} minecraft days\nis {minutes}min (or {hours}h)"

_input=Spinbox(from_=1,to=2147483647,width=10,font=("Comic Sans MS",24))
_input["command"]=calculate
_input.pack()
_input.focus()
window.bind('<Return>', calculate)

# button=Button(text="Calculate",font=("Comic Sans MS",24))
# button["command"]=calculate
# button.pack()

output_label=Label(font=("Comic Sans MS",24))
output_label.pack()
calculate()
output_label["text"]=f"{days} minecraft day\nis {minutes}min (or {hours}h)"

window.mainloop()