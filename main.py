import math
from tkinter import *

screen = Tk()
timeing = None
repitations = 0

label= Label(text="timer",font=("arial",40,"normal"))
label.grid(column=2,row=1)

screen.config(padx=200,pady=200)
canvas = Canvas(width=300,height=250)
img = PhotoImage(file="tomato.png")
canvas.create_image(150,100,image = img)
time_Text = canvas.create_text(150,120,text="00:00", fill="black",font=("arial",35,"normal"))
canvas.grid(column=2,row=2)
def start_timer():
    global repitations
    repitations+=1
    if repitations%8==0:

        timer(count=20 * 60)
        label.config(text="LONGBREAK")
    elif repitations%2==0:

        timer(count=5 * 60)
        label.config(text="SHORTBREAK")
    else:

        timer(count=25*60)
        label.config(text = "WORK")


def timer(count):

        min = math.floor(count/60)
        sec = count%60
        canvas.itemconfig(time_Text, text=f"{min}:{sec}")

        if sec <= 9:

            canvas.itemconfig(time_Text, text=f"{min}:0{sec}")
        if count>0:
            global timeing
            timeing = canvas.after(1000,timer,count-1)

        else:

            start_timer()
            mark=''
            work_sessions=math.floor(repitations/2)

            for _ in range(work_sessions):
                mark+="✓"
            tick_mark.config(text=mark)


# def tick_use():
#     tick_mark = Label(text="✓",font=("arial",20,"normal"))
#     tick_mark.grid(column=2,row=3)

def reset_use():
    canvas.after_cancel(timeing)
    label.config(text ="TIMER")
    canvas.itemconfig(time_Text,text="00:00")


start_button = Button(width=15, text="Start",font=("arial",15,"normal"),command=start_timer)
start_button.grid(column=1,row=3)

tick_mark = Label(text="",font=("arial",20,"normal"))
tick_mark.grid(column=2,row=3)

reset_button = Button(width=15,text="Reset",font=("arial",15,"normal"),command=reset_use)
reset_button.grid(column=3,row=3)

screen.mainloop()
