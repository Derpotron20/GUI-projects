import tkinter as tk

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("275x100")

answer_C = None
answer_F = None
def show_message_C():
    dgs_C = int(entry.get())
    answer_C = round(((dgs_C * 9/5) + 32), 1)
    label.config(text=answer_C)

def show_message_F():
    dgs_F = int(entry.get())
    answer_F = round(((dgs_F - 32) * 5/9), 1)
    label.config(text=answer_F)

def toggle():
    if check_state.get() == 0:
        label_type1.config(text="°C")
        label_type2.config(text="°F")

    else:
        label_type1.config(text="°F")
        label_type2.config(text="°C")

def msg_shrtcut(event):
    if event.keysym == "Return" and check_state.get() == 0:
        show_message_C()
    elif event.keysym == "Return" and check_state.get() == 1:
        show_message_F()

entry = tk.Entry(root, width=5, font=('Arial', 16))
entry.bind("<KeyPress>", msg_shrtcut)
entry.place(x=13, y=10)

label_arrow1 = tk.Label(root, text=("|\n" + "ˇ"))
label_arrow1.place(x=33, y=40)

check_state = tk.IntVar()

check = tk.Checkbutton(root, text="Convert to °C instead", font=('Arial', 14), variable=check_state, command=toggle)
check.place(x=95, y=13)


label = tk.Label(root, text=answer_C)
label.place(x=23, y=70)

label_type1 = tk.Label(root, text="°C")
label_type1.place(x=70, y=12)

label_type2 = tk.Label(root, text="°F")
label_type2.place(x=70, y=70)


root.mainloop()
