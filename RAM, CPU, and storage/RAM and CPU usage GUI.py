import tkinter as tk
import customtkinter as ctk
import psutil

root = ctk.CTk()


CPUbar = ctk.CTkProgressBar(root, width=100, orientation="horizontal")
RAMbar = ctk.CTkProgressBar(root, width=100, orientation="horizontal")
STRbar = ctk.CTkProgressBar(root, width=100, orientation="horizontal")
CPUbar.place(x=35, y=55)
RAMbar.place(x=200, y=55)
CPUlbl = ctk.CTkLabel(root, text="")
RAMbtn = ctk.CTkLabel(root, text="")
menubar = ctk.CTkLabel(root, text="")
RAMinfo = ctk.CTkLabel(root, text="")
RAMinfo_check = False
STRinfo_check = False



#Changing the progress bar's values
def display_usage(cpu_usage, mem_usage, str_usage):
    cpu_percent = (cpu_usage / 100.0)
    mem_percent = (mem_usage / 100.0)
    str_percent = (str_usage/ 100.0)


    CPUbar.set(cpu_percent)
    RAMbar.set(mem_percent)
    STRbar.set(str_percent)
    


def RAM_values():
    global RAMinfo
    total_gb = round((psutil.virtual_memory()[0]/1000000000), 2)
    available_gb = round((psutil.virtual_memory()[1]/1000000000), 2)
    used_gb = round((psutil.virtual_memory()[3]/1000000000), 2)
    free_gb = round((psutil.virtual_memory()[4]/1000000000), 2)
    RAMinfo.config(text=f"RAM Total (GB): {total_gb}\nRAM Available (GB) {available_gb}\nRAM Used (GB) {used_gb}\nRAM Free (GB) {free_gb}")

def STR_values():
    global STRinfo
    total_GB = round((psutil.disk_usage('/')[0]/1000000000), 2)
    used_GB = round((psutil.disk_usage('/')[1]/1000000000), 2)
    free_GB = round((psutil.disk_usage('/')[2]/1000000000), 2)
    STRinfo.config(text=f"STR Total (GB): {total_GB}\nSTR Used (GB) {used_GB}\nSTR Free (GB) {free_GB}")



def set_value():
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage('/')[3])
    global RAMinfo, RAMinfo_check
    total_gb = round((psutil.virtual_memory()[0]/1000000000), 2)
    available_gb = round((psutil.virtual_memory()[1]/1000000000), 2)
    used_gb = round((psutil.virtual_memory()[3]/1000000000), 2)
    free_gb = round((psutil.virtual_memory()[4]/1000000000), 2)
    global STRinfo, STRinfo_check
    total_GB = round((psutil.disk_usage('/')[0]/1000000000), 2)
    used_GB = round((psutil.disk_usage('/')[1]/1000000000), 2)
    free_GB = round((psutil.disk_usage('/')[2]/1000000000), 2)
    if RAMinfo_check == True:
        RAMinfo.configure(text=f"RAM Total (GB): {total_gb}\nRAM Available (GB) {available_gb}\nRAM Used (GB) {used_gb}\nRAM Free (GB) {free_gb}")
    elif STRinfo_check == True:
        STRinfo.configure(text=f"STR Total (GB): {total_GB}\nSTR Used (GB) {used_GB}\nSTR Free (GB) {free_GB}")
    root.after(500, set_value)

#Deleting inside current window

def root_frame_delete(btn_pressed):
    global CPUbar, CPUlbl, RAMbar, RAMbtn, menubar, STRbtn
    CPUlbl.destroy()
    RAMbtn.destroy()
    STRbtn.destroy()
    menubar.destroy()
    if btn_pressed == "RAM":
        RAM_frame_create()
    elif btn_pressed == "STR":
        STR_frame_create()

def RAM_frame_delete():
    global RAMinfo_check
    RAMinfo_check = False
    RAMlabel.destroy()
    backbtn2.destroy()
    RAMinfo.destroy()
    root_frame_create()

def STR_frame_delete():
    global STRinfo_check
    STRinfo_check = False
    STRlabel.destroy()
    backbtn3.destroy()
    STRinfo.destroy()
    root_frame_create()



def RAM_frame_create():
    global RAMlabel, RAMbar, backbtn2, CPUbar, RAMinfo, RAMinfo_check
    root.title("RAM Info")
    root.geometry("300x200")

    RAMlabel = ctk.CTkLabel(root, text="RAM")
    RAMlabel.pack(pady=10)

    RAMinfo_check = True

    RAMinfo = ctk.CTkLabel(root, text="")
    RAMinfo.place(x=80, y=60)

    backbtn2 = ctk.CTkButton(root, text="Back", font=('Arial', 10), command=RAM_frame_delete, height=24, width=25, fg_color="black")
    backbtn2.place(x=5, y=5)

    RAMbar.place(x=100, y=45)
    STRbar.place(x=10000, y=10000)
    CPUbar.place(x=10000, y=10000)

    RAMmenubar = tk.Menu(root)
    filemenu = tk.Menu(RAMmenubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    RAMmenubar.add_cascade(label="File", menu=filemenu)

    window = tk.Menu(RAMmenubar, tearoff=0)
    window.add_command(label="Option Page Current Window", command=RAM_frame_delete)
    RAMmenubar.add_cascade(label="Information", menu=window)

    root.config(menu=RAMmenubar)

def STR_frame_create():
    global STRlabel, STRbar, backbtn3, CPUbar, STRinfo, STRinfo_check, RAMbar
    root.title("STR Info")
    root.geometry("300x200")

    STRlabel = ctk.CTkLabel(root, text="Storage")
    STRlabel.pack(pady=10)

    STRinfo_check = True

    STRinfo = ctk.CTkLabel(root, text="")
    STRinfo.place(x=80, y=60)

    backbtn3 = ctk.CTkButton(root, text="Back", font=('Arial', 10), command=STR_frame_delete, height=24, width=25, fg_color="black")
    backbtn3.place(x=5, y=5)

    STRbar.place(x=100, y=45)
    RAMbar.place(x=10000, y=10000)
    CPUbar.place(x=10000, y=10000)

    STRmenubar = tk.Menu(root)
    filemenu = tk.Menu(STRmenubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    STRmenubar.add_cascade(label="File", menu=filemenu)

    window = tk.Menu(STRmenubar, tearoff=0)
    window.add_command(label="Option Page Current Window", command=STR_frame_delete)
    STRmenubar.add_cascade(label="Information", menu=window)

    root.config(menu=STRmenubar)


#Opening the RAM seperate window
def openRAMWindow():

    newWindow = ctk.CTkToplevel(root)
    newWindow.title("RAM Info")
    newWindow.geometry("300x200")
    global RAMlabel, CPUbar, RAMinfo, RAMinfo_check

    RAMlabel = ctk.CTkLabel(newWindow, text="RAM")
    RAMlabel.place(x=130, y=8)

    RAMinfo_check = True

    RAMinfo = ctk.CTkLabel(newWindow, text="")
    RAMinfo.place(x=80, y=60)

    RAMbar = ctk.CTkProgressBar(newWindow, width=100, orientation="horizontal")
    RAMbar.place(x=100, y=45)

    set_value()

def openSTRwindow():

    newWindow = ctk.CTkToplevel(root)
    newWindow.title("Storage Info")
    newWindow.geometry("300x200")
    global STRlabel, CPUbar, STRbar, STRinfo, STRinfo_check

    STRlabel = ctk.CTkLabel(newWindow, text="STR")
    STRlabel.place(x=130, y=8)

    STRinfo_check = True

    STRinfo = ctk.CTkLabel(newWindow, text="")
    STRinfo.place(x=80, y=60)

    STRbar = ctk.CTkProgressBar(newWindow, width=100, orientation="horizontal")
    STRbar.place(x=100, y=45)

    set_value()

def root_frame_create():
    root.title("Activity Monitor")
    root.geometry("335x180")
    global CPUbar, CPUlbl, RAMbar, RAMbtn, menubar, btn_pressed, STRbar, STRbtn
    btn_pressed = None
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    window = tk.Menu(menubar, tearoff=0)
    window.add_command(label="RAM info current window", command=lambda: root_frame_delete("RAM"))
    window.add_command(label="Storage info current window", command=lambda: root_frame_delete("STR"))
    window.add_separator()
    window.add_command(label="RAM info new window", command=openRAMWindow)
    window.add_command(label="Storage info new window", command=openSTRwindow)
    menubar.add_cascade(label="Information", menu=window)

    root.config(menu=menubar)

    #RAM and CPU buttons
    CPUlbl = ctk.CTkLabel(root, text="CPU")
    CPUlbl.place(x=70, y=10)
    RAMbtn = ctk.CTkButton(root, text="RAM", command=lambda: root_frame_delete("RAM"), height=35, width=150, fg_color="black")
    RAMbtn.place(x=175, y=10)
    STRbtn = ctk.CTkButton(root, text="STR", command=lambda: root_frame_delete("STR"), height=35, width=150, fg_color="black")
    STRbtn.place(x=10, y=90)

    #RAM and CPU Progress Bars

    CPUbar.place(x=35, y=55)
    RAMbar.place(x=200, y=55)
    STRbar.place(x=35, y=145)

    set_value()


root_frame_create()

root.mainloop()