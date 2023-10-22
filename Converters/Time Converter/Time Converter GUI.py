import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Time Converter")
root.geometry("510x130")


def msg_shrtcut(event):
    print(event)
    if event.keysym == "Return" and choice.get() == 1:
        weeks_days()
    elif event.keysym == "Return" and choice.get() == 2:
        days_hours()
    elif event.keysym == "Return" and choice.get() == 3:
        hours_minutes()
    elif event.keysym == "Return" and choice.get() == 4:
        hours_minutes()

def weeks_days():
    global rev
    counter = 0
    num = int(input.get())
    # Weeks into Days
    if rev.get() == 0:
        num = num * 7
        answer.config(text=f'{num} days')
        
    # Days into Weeks
    elif rev.get() == 1:
        while num > 7:
            num -= 7
            counter += 1
        if num == 0:
            answer.config(text=f'{counter} weeks')
        elif num > 0:
            answer.config(text=f'{counter} weeks and {num} days')

def days_hours():
    global rev
    counter = 0
    num = int(input.get())
    # Days into Hours
    if rev.get() == 0:
        num = num * 24
        answer.config(text=f'{num} hours')
        
    # Hours into Days
    elif rev.get() == 1:
        while num > 24:
            num -= 24
            counter += 1
        if num == 0:
            answer.config(text=f'{counter} days')
        elif num > 0:
            answer.config(text=f'{counter} days and {num} hours')

def hours_minutes():
    global rev
    counter = 0
    num = int(input.get())
    # Hours into Minutes
    if rev.get() == 0:
        num = num * 60
        answer.config(text=f'{num} hours')
        
    # Minutes into Hours
    elif rev.get() == 1:
        while num > 60:
            num -= 60
            counter += 1
        if num == 0:
            answer.config(text=f'{counter} hours')
        elif num > 0:
            answer.config(text=f'{counter} hours and {num} minutes')

        
    # Seconds into Minutes
    elif rev.get() == 1:
        while num > 60:
            num -= 60
            counter += 1
        if num == 0:
            answer.config(text=f'{counter} minutes')
        elif num > 0:
            answer.config(text=f'{counter} minutes and {num} seconds')

def toggle():
    if rev.get() == 0:
        option1.config(text="Weeks to Days")
        option2.config(text="Days to Hours")
        option3.config(text="Hours to Minutes")
        option4.config(text="Minutes to Seconds")

    else:
        option1.config(text="Days to Weeks")
        option2.config(text="Hours to Days")
        option3.config(text="Minutes to Hours")
        option4.config(text="Seconds to Minutes")

__name__ = "__main__"
if __name__ == "__main__":
    choice = tk.IntVar()

    option1 = tk.Radiobutton(root, text="Weeks to Days", font=('Arial', 13), variable=choice, value=1)
    option1.place(x=10, y=50)

    option2 = tk.Radiobutton(root, text="Days to Hours", font=('Arial', 13), variable=choice, value=2)
    option2.place(x=150, y=50)

    option3 = tk.Radiobutton(root, text="Hours to Minutes", font=('Arial', 13), variable=choice, value=3)
    option3.place(x=10, y=90)

    option4 = tk.Radiobutton(root, text="Minutes to Seconds", font=('Arial', 13), variable=choice, value=4)
    option4.place(x=150, y=90)

    input = tk.Entry(root, font=('Arial', 15))
    input.bind("<KeyPress>", msg_shrtcut)
    input.place(x=10, y=10)

    answer = tk.Label(root, text="", font=('Arial', 14))
    answer.place(x=330, y=13)

    arrow = Image.open("arrow.png")

    resizedarrow = arrow.resize((60,18), Image.LANCZOS)

    properarrow = ImageTk.PhotoImage(resizedarrow)

    properarrowlabel = tk.Label(root, width=60, height=18, image=properarrow)
    properarrowlabel.place(x=240, y=15)

    rev = tk.IntVar()

    reverse = tk.Checkbutton(root, text="Would you like to reverse?", font=('Arial', 13), variable=rev, command=toggle)
    reverse.place(x=310, y=67)

root.mainloop()