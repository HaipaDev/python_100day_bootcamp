from tkinter import *

window=Tk()
window.title("test")
window.minsize(500,300)
window.config(padx=20,pady=20)

# Label
label=Label(text="0",font=("Comic Sans MS",48))
#label["text"]="Test2"
#label.pack()
#label.place(x=0,y=0)
label.grid(column=0,row=0)

# Button
click_count=0
def button_clicked():
    global click_count
    # print("I got clicked")
    # label["text"]="I got clicked"
    click_count+=1
    label["text"]=click_count
    
    if(_input.get()!=""):
        label["text"]=_input.get()
        _input.delete(0,len(_input.get()))
    


button=Button(text="Click me",font=("Comic Sans MS",48))
button["command"]=button_clicked
#button.pack()
button.grid(column=1,row=1)

# Entry/Input
_input=Entry(width=20)
if(_input.get()!=""):
    label["text"]=_input.get()
#_input.pack()
_input.grid(column=2,row=2)





window.mainloop()