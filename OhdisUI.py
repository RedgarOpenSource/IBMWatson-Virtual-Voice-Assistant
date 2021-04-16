import os
import subprocess
import tkinter as tk
import tkinter.font as font

app = tk.Tk()
app.geometry("400x400")
app.configure(bg='gray')

photo = tk.PhotoImage(file=r"C:\Users\bedga\PycharmProjects\GUIdev\ohdis_button_active.png")
myFont = font.Font(family='Helvetica', size=20, weight='normal')

tk.Label(app, text='Ohdis App Version 1.0', bg='gray', font=(
    'Verdana', 15)).pack(side=tk.TOP, pady=10)

tk.Label(app, text='Ohdis AI Version 1.3', bg='gray', font=(
    'Verdana', 15)).pack(side=tk.TOP, pady=10)

app.iconbitmap(r'C:\Users\bedga\PycharmProjects\GUIdev\ohdis_icon.ico')


def ohdis_activation():
    global pro
    print("Ohdis Running!")
    ohdis_activation_button['state'] = 'disabled'
    pro = subprocess.Popen("python Ohdis1.3.py", shell=True)


def ohdis_stop():
    global pro
    print("Stopping Ohdis... Please Wait!")
    os.kill(pro.pid, 0)
    ohdis_activation_button['state'] = 'normal'


# Essentially, the Stop button refreshes the state as normal once clicked and the activation button becomes disabled
# state once pressed

ohdis_activation_button = tk.Button(app, bg='black', image=photo, width=120, height=120, command=ohdis_activation)

ohdis_stop_button = tk.Button(app, bg='Gray', text='Stop Ohdis', width=12, command=ohdis_stop, height=3)

ohdis_stop_button['font'] = myFont

app.title("Ohdis Beta 1")
ohdis_activation_button.pack(side=tk.TOP)
ohdis_stop_button.pack(side=tk.LEFT)

# app.mainloop()
while True:
    try:
        app.update()
        app.update_idletasks()
    except KeyboardInterrupt:
        pass
