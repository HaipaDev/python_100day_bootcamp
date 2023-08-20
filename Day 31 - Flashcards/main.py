## I modified this quite a bit from what the course intended ##

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sys

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME="Arial"
WIDTH=800
HEIGHT=526

DATASET_FILE="jlpt_n5_normalized.csv"
TIME_BEFORE_FLIP=3
SHOW_READINGS_ON_FRONT=True
ITALIC_READINGS_FONT=True

import subprocess
subprocess.run(["pip", "install", "pandas"])
import pandas
subprocess.run(["pip", "install", "pyperclip"])
import pyperclip
print("\n")
# ---------------------------- READING DATA ------------------------------- # 
import json
def read_config():
    global DATASET_FILE,TIME_BEFORE_FLIP,SHOW_READINGS_ON_FRONT,ITALIC_READINGS_FONT
    try:
        with open("config.json","r") as config_file:
            config_data=json.load(config_file)
            try:
                TIME_BEFORE_FLIP=config_data["time_before_flip"]
                SHOW_READINGS_ON_FRONT=config_data["show_readings_on_front"]
                ITALIC_READINGS_FONT=config_data["italic_readings_font"]
            except:
                print("config.json broken | You should replace it with a new one")
                
            try:
                DATASET_FILE="data/"+(config_data["dataset"].replace("data/",""))
            except:
                messagebox.showerror(title="Error",message=f"config.json broken | Leaving the dataset as {DATASET_FILE}")
                print(f"config.json broken | leaving the dataset as {DATASET_FILE}")
                DATASET_FILE="data/"+(DATASET_FILE.replace("data/",""))
            else:
                if(DATASET_FILE=="" or DATASET_FILE=="data/"):
                    DATASET_FILE="data/"+"jlpt_n5_normalized.csv"
                print(f"Setting the dataset to {DATASET_FILE}")
    except:
        print(f"config.json not found/broken | leaving the dataset as {DATASET_FILE}")
        with open("config.json","w") as config_file:
            default_config_data={
                "dataset": DATASET_FILE,
                "time_before_flip": TIME_BEFORE_FLIP,
                "show_readings_on_front": SHOW_READINGS_ON_FRONT,
                "italic_readings_font": ITALIC_READINGS_FONT,
            }
            json.dump(default_config_data, config_file,indent=4)
            DATASET_FILE="data/"+DATASET_FILE

# def get_default_dataset():
#     global DATASET_FILE
#     try:
#         with open("default_dataset.txt","r") as default_dataset:
#             DATASET_FILE="data/"+default_dataset.read()
#             print(f"Setting the dataset to {DATASET_FILE}")
#     except FileNotFoundError:
#         print(f"default_dataset.txt not found | leaving the dataset as {DATASET_FILE}")
#         with open("default_dataset.txt","w") as default_dataset:
#             default_dataset.write(DATASET_FILE)
#             DATASET_FILE="data/"+DATASET_FILE
    
read_config()

data_dict={}

def save_current_dataset():
    with open(DATASET_FILE,"w", encoding="utf-8") as dataset_file:
        dataframe=pandas.DataFrame(data_dict)
        dataset_file.write(dataframe.to_csv(index=False))
        print(f"{len(data_dict)} words written to {DATASET_FILE}")

def tryget_current_dataset():
    global data_dict
    try:
        with open(DATASET_FILE,"r",encoding="utf-8"):
            data=pandas.read_csv(DATASET_FILE)
    except FileNotFoundError:
        try:
            print("Current DATASET_FILE not found/broken, pulling from the original")
            original_dataset_file=DATASET_FILE.replace("data/", "data/original/")
            data=pandas.read_csv(original_dataset_file)
        except FileNotFoundError:
            print(f"No dataset file found by the name|path of {DATASET_FILE}")
            messagebox.showerror(title="Error",message=f"No dataset file found by the name|path of {DATASET_FILE}")
            sys.exit()
        else:
            data_dict=data.to_dict(orient="records")
            print(f"{len(data_dict)} words loaded from {DATASET_FILE}")
            ## Write a new file if only original exists
            save_current_dataset()
    except Exception as e:
        print(f"File {DATASET_FILE} is either empty or in incorrect format\n{e}")
        messagebox.showerror(title="Error",message=f"File {DATASET_FILE} is either empty or in incorrect format")
        sys.exit()
    else:
        data_dict=data.to_dict(orient="records")
        print(f"{len(data_dict)} words loaded from {DATASET_FILE}")

tryget_current_dataset()

def reset_dataset_to_default():
    global data_dict
    prompt=messagebox.askyesno(title="Reset??",message="Are you sure you want to reset your current dataset to the original one?")
    if prompt:
        original_dataset_file=DATASET_FILE.replace("data/", "data/original/")
        try:
            data=pandas.read_csv(original_dataset_file)
            data_dict=data.to_dict(orient="records")
            print(f"{len(data_dict)} words loaded from {DATASET_FILE}")
            save_current_dataset()
            random_word()
        except:
            print(f"No dataset file found by the name|path of {original_dataset_file}")
            messagebox.showerror(title="Error",message=f"No dataset file found by the name|path of {original_dataset_file}")
            
    pass
# ---------------------------- GETTING RANDOM WORD ------------------------------- # 
import random
current_card={}
card_flipped=False

def checked_wrong():
    if(card_flipped):
        random_word()
    
def checked_right():
    global data_dict
    if(card_flipped):
        if current_card in data_dict:
            data_dict.remove(current_card)
            save_current_dataset()
        random_word()
    
    
def random_word():
    global current_card,card_flipped
    try:
        current_card=random.choice(data_dict)
    except:
        print("Incorrect dictionary? Cant set current_card to random")
    
    word=""
    try:
        word=current_card["word"]
    except KeyError:
        try:
            word=current_card["expression"]
        except KeyError:
            try:
                word=current_card["front"]
            except KeyError:
                print("Incorect data format?\nThe word key should either be 'word', 'expression' or 'front'")
            
    canvas.itemconfig(word_text,text=word)
    
    if(not SHOW_READINGS_ON_FRONT):
        canvas.itemconfig(reading_text,text="")
    else:
        try:
            reading=current_card["reading"]
        except KeyError:
            canvas.itemconfig(reading_text,text="")
            print("No reading for the word?")
        else:
            ## Dont show readings that are exactly the same as the base word ##
            if(reading==word):
                reading=""
            canvas.itemconfig(reading_text,text=reading)
            
    canvas.itemconfig(card_img,image=card_front_img)
    canvas.itemconfig(word_text,fill="black")
    canvas.itemconfig(meaning_text,fill="black",text="")
    card_flipped=False
    window.after(1000*TIME_BEFORE_FLIP,flip_card)
    
    
def flip_card():
    global card_flipped
    if(not SHOW_READINGS_ON_FRONT):
        try:
            reading=current_card["reading"]
        except KeyError:
            canvas.itemconfig(reading_text,text="")
            print("No reading for the word?")
        else:
            ## Dont show readings that are exactly the same as the base word ##
            if(reading==canvas.itemcget(word_text,"text")):
                reading=""
            canvas.itemconfig(reading_text,text=reading)
    
    try:
        meaning=current_card["meaning"]
    except KeyError:
        try:
            meaning=current_card["back"]
        except KeyError:
            print("Incorrect data format?\nMeaning of the word key should either be 'meaning' or 'back'")
            messagebox.showwarning(title="Error",message="Incorrect data format?\nThe meaning of the words key should either be 'meaning' or 'back'")
    else:
        canvas.itemconfig(meaning_text,text=meaning)
        canvas.itemconfig(card_img,image=card_back_img)
        canvas.itemconfig(word_text,fill="white")
        canvas.itemconfig(meaning_text,fill="white")
        
    card_flipped=True
    
def copy_word(event=None):
    word=""
    try:
        word=current_card["word"]
    except KeyError:
        try:
            word=current_card["expression"]
        except KeyError:
            try:
                word=current_card["front"]
            except KeyError:
                print("Couldnt copy the word?")
    finally:
        if(word!=""):
            print(f"{word} coppied to clipboard")
            messagebox.showinfo(title="Coppied to clipboard",message=f"{word} coppied to clipboard")
            pyperclip.copy(word)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("HyperFlashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.after(1000*TIME_BEFORE_FLIP,flip_card)

style=ttk.Style()
#style.theme_use("winnative")
style.configure("TButton",
                padding=-1, relief="flat", background=BACKGROUND_COLOR,
                highlightthickness=-1, borderwidth=-1)

style.map("TButton",
          background=[("active", BACKGROUND_COLOR)],
          borderwidth=[("active", -1)],
          padding=[("active", -1)])

card_front_img=PhotoImage(file="images/card_front.png")
card_back_img=PhotoImage(file="images/card_back.png")

canvas=Canvas(width=WIDTH,height=HEIGHT)
card_img=canvas.create_image(WIDTH/2,HEIGHT/2,image=card_front_img)


word_text=canvas.create_text(WIDTH/2,120, text="word", fill="black", font=(FONT_NAME,40,""), width=WIDTH-20)
reading_text=canvas.create_text(WIDTH/2,200, text="reading", fill="#707078", font=(FONT_NAME,40,"italic"), width=WIDTH-20)
meaning_text=canvas.create_text(WIDTH/2,340, text="meaning", fill="black", font=(FONT_NAME,40,"bold"), width=WIDTH-20)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
canvas.tag_bind(word_text, "<Button-1>", copy_word)

if(not ITALIC_READINGS_FONT):
    canvas.itemconfig(reading_text,font=(FONT_NAME,40,""))
else:
    canvas.itemconfig(reading_text,font=(FONT_NAME,40,"italic"))

wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=ttk.Button(window,image=wrong_img)
wrong_button["command"]=checked_wrong
wrong_button.grid(row=1,column=0)

reset_img=PhotoImage(file="images/revert.png")
reset_button=ttk.Button(window,image=reset_img)
reset_button["command"]=reset_dataset_to_default
reset_button.grid(row=2,column=0,columnspan=3)

right_img=PhotoImage(file="images/right.png")
right_button=ttk.Button(window,image=right_img)
right_button["command"]=checked_right
right_button.grid(row=1,column=1)


window.after(200,random_word)
window.mainloop()