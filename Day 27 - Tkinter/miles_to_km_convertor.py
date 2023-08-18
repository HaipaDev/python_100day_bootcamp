from tkinter import *

def miles_to_km():
    miles=1
    if(miles_input.get().isnumeric()):
        miles=float(miles_input.get())
    km=miles*1.609
    result_label["text"]=km

window=Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)
miles_input.insert(END,1)
miles_input.focus()

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label=Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

result_label=Label(text="0")
result_label.grid(column=1,row=1)

kilometer_label=Label(text="Km")
kilometer_label.grid(column=2,row=1)

button=Button(text="Calculate")
button.grid(column=1,row=2)
button["command"]=miles_to_km

miles_to_km()


window.mainloop()