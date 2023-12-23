# Importing Everything
import customtkinter as ctk
import psutil

# Creates a New Window under the name "root"
root = ctk.CTk()

# Defines the progress bars early so that new ones are made each time root_frame_create is called
CPUbar = ctk.CTkProgressBar(root, width=100, orientation="horizontal")
RAMbar = ctk.CTkProgressBar(root, width=100, orientation="horizontal")
STRbar = ctk.CTkProgressBar(root, width=100, orientation="horizontal")

# Two variables for chcking if we should show data about RAM and storage
RAMinfo_check = False
STRinfo_check = False

#Changing the progress bar's values
def display_usage():
    # Sets the values to percentages
    cpu_percent = (psutil.cpu_percent() / 100.0)
    mem_percent = (psutil.virtual_memory().percent / 100.0)
    str_percent = (psutil.disk_usage('/')[3] / 100.0)

    # Sets the progress bars outputs to the percentages made above.
    CPUbar.set(cpu_percent)
    RAMbar.set(mem_percent)
    STRbar.set(str_percent)


def set_value():
    # Changes what the progress bars display
    display_usage()

    # Gains access to the RAM and storage information label, and if it needs to be displayed
    global RAMinfo, RAMinfo_check, STRinfo, STRinfo_check


    # Changes what is said by the RAM information label if it needs to
    if RAMinfo_check == True:
        # Defines what will be shown for RAM
        total_gb = round((psutil.virtual_memory()[0]/1000000000), 2)
        available_gb = round((psutil.virtual_memory()[1]/1000000000), 2)
        used_gb = round((psutil.virtual_memory()[3]/1000000000), 2)
        free_gb = round((psutil.virtual_memory()[4]/1000000000), 2)
        RAMinfo.configure(text=f"RAM Total (GB): {total_gb}\nRAM Available (GB) {available_gb}\nRAM Used (GB) {used_gb}\nRAM Free (GB) {free_gb}")
    
    # Changes what is said by the storage information label if it needs to
    elif STRinfo_check == True:
        # Defines what will be shown for storage
        total_GB = round((psutil.disk_usage('/')[0]/1000000000), 2)
        used_GB = round((psutil.disk_usage('/')[1]/1000000000), 2)
        free_GB = round((psutil.disk_usage('/')[2]/1000000000), 2)
        STRinfo.configure(text=f"STR Total (GB): {total_GB}\nSTR Used (GB) {used_GB}\nSTR Free (GB) {free_GB}")
    
    # Re-executes this function every 0.5 seconds
    root.after(500, set_value)


def root_frame_delete(btn_pressed):
    global CPUlbl, RAMbtn, STRbtn

    # Destroyes all of these elements
    CPUlbl.destroy()
    RAMbtn.destroy()
    STRbtn.destroy()

    # Chooses which new frame to create
    if btn_pressed == "RAM":
        RAM_frame_create()
    elif btn_pressed == "STR":
        STR_frame_create()


# Creates the RAM window to show information about the current RAM usage
def RAM_frame_create():
    # Acesses all of the elements needed to be changed, but also allows acces to all elements that can be changed
    global RAMlabel, RAMbar, RAMbackbtn, CPUbar, STRbar, RAMinfo, RAMinfo_check

    # Changes window title
    root.title("RAM Info")

    # Changes window size and shape
    root.geometry("300x200")

    # Creates a Label to show it's the RAM tab
    RAMlabel = ctk.CTkLabel(root, text="RAM")
    RAMlabel.pack(pady=10)

    # Allows the RAM info to be shown on the RAM info label
    RAMinfo_check = True

    # Decides where the bar will be shown
    RAMbar.place(x=100, y=45)

    # Moves the other bars off screen
    STRbar.place(x=10000, y=10000)
    CPUbar.place(x=10000, y=10000)


    # Creates a back button
    RAMbackbtn = ctk.CTkButton(root, text="Back", font=('Arial', 10), command=RAM_frame_delete, height=24, width=25, fg_color="black")
    RAMbackbtn.place(x=5, y=5)

    # Places where the RAM info will be shown
    RAMinfo = ctk.CTkLabel(root, text="")
    RAMinfo.place(x=80, y=60)

    set_value()

    

# Creates the Storage window to show information about the current storage usage
def STR_frame_create():
    # Acesses all of the elements needed to be changed, but also allows acces to all elements that can be changed
    global STRlabel, STRbar, STRbackbtn, CPUbar, RAMbar, STRinfo, STRinfo_check

    # Changes window title
    root.title("Storage Info")

    # Changes window size and shape
    root.geometry("300x200")

    # Creates a Label to show it's the storage tab
    STRlabel = ctk.CTkLabel(root, text="Storage")
    STRlabel.pack(pady=10)

    # Allows the storage info to be shown on the storage info label
    STRinfo_check = True

    # Decides where the bar will be shown
    STRbar.place(x=100, y=45)

    # Moves the other bars off screen
    RAMbar.place(x=10000, y=10000)
    CPUbar.place(x=10000, y=10000)

    # Creates a back button
    STRbackbtn = ctk.CTkButton(root, text="Back", font=('Arial', 10), command=STR_frame_delete, height=24, width=25, fg_color="black")
    STRbackbtn.place(x=5, y=5)

    # Places where the RAM info will be shown
    STRinfo = ctk.CTkLabel(root, text="")
    STRinfo.place(x=80, y=60)

    set_value()


# Creates a function to delete the widgets of the RAM window
def RAM_frame_delete():
    global RAMinfo_check
    RAMinfo_check = False
    RAMlabel.destroy()
    RAMbackbtn.destroy()
    RAMinfo.destroy()
    root_frame_create()

# Creates a function to delete the widgets of the storage window
def STR_frame_delete():
    global STRinfo_check
    STRinfo_check = False
    STRlabel.destroy()
    STRbackbtn.destroy()
    STRinfo.destroy()
    root_frame_create()


# Function to allow repeatedly creating the home page
def root_frame_create():
    # Allows other functions to access everything inside this function
    global CPUlbl, RAMbtn, STRbtn

    # Change the window title
    root.title("Activity Monitor")

    # changes window size
    root.geometry("335x180")

    # Creates and places mutliple progress bars
    
    CPUbar.place(x=35, y=55)
    RAMbar.place(x=200, y=55)
    STRbar.place(x=35, y=145)

    # Creates and places buttons to access other windows, as well as the label for CPU
    CPUlbl = ctk.CTkLabel(root, text="CPU")
    CPUlbl.place(x=70, y=10)

    # When these buttons are pressed, it deletes the elements off the screen, and says which new screen to make
    RAMbtn = ctk.CTkButton(root, text="RAM", command=lambda: root_frame_delete("RAM"), height=35, width=150, fg_color="black")
    RAMbtn.place(x=175, y=10)
    STRbtn = ctk.CTkButton(root, text="STR", command=lambda: root_frame_delete("STR"), height=35, width=150, fg_color="black")
    STRbtn.place(x=10, y=90)

    set_value()

# Completes what's in the root_frame_create function
root_frame_create()

# Creates the Window
root.mainloop()
