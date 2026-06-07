# amirrezagharoori9

import string 
import random
import tkinter as tk
from tkinter import messagebox
import pyperclip
def random_pass():
    window = tk.Tk()
    window.title("random password")
    window.geometry("500x600")
    window.configure(bg="#1e1e1e")

    label = ("Segoe UI", 20, "bold")
    font = ("Segoe UI", 12)
    button = "#ff9500"
     
    tk.Label(window, text="password", font=label,fg='white', bg=window["bg"]).pack(pady=10)
    entry = tk.Entry(window, font=font, width=20)
    entry.pack(pady=5)
    entry.insert(0, "enter the length:")
    output = tk.Text(window, font=font, height=2,
                     width=50, bg="#2e2e2e", fg="white")
    output.pack(pady=5)
    
    def exit():
        window.destroy()

    def click(e):
        if entry.get() == "enter the length:":

            entry.delete(0, tk.END)
            entry.config(fg='black')
    entry.bind("<FocusIn>", click)

    def intger(length):
        numbers = string.digits
        output.delete("1.0", tk.END)
        output.insert(tk.END, ''.join(random.choice(numbers) for _ in range(length)))
  


    def stri(length):
        letter = string.ascii_letters
        output.delete("1.0", tk.END)
        output.insert(tk.END, ''.join(random.choice(letter) for _ in range(length)))
        

    def copyy():
        password_text = output.get("1.0", "end-1c") 
        if password_text and password_text != "":
            pyperclip.copy(password_text)


    def mix(length):
        chars = string.ascii_letters + string.digits
        output.delete("1.0", tk.END)
        output.insert(tk.END, ''.join(random.choices(chars, k = length)))
    


    def buton(label, command):
        return tk.Button(window, text=label, font=font, fg="white", bg=button,
                         activebackground="#ffb347", width=25, height=2, command=command)
    
    def call_I():
        try:
            length = int(entry.get())
            intger(length)
        except ValueError:
            output.delete("1.0", tk.END)
            messagebox.showerror("please enter a valid number") 
    def call_S():
        try:
            length = int(entry.get())
            stri(length)
        except ValueError:
            output.delete("1.0", tk.END)
            messagebox.showerror("please enter a valid number") 

    def call_M():
        try:
            length = int(entry.get())
            mix(length)
        except ValueError:
            output.delete("1.0", tk.END)
            messagebox.showerror("please enter a valid number") 
    buton("Intiger", call_I).pack(pady=5)
    buton("String", call_S).pack(pady=5)
    buton("Mix", call_M).pack(pady=5)
    buton("copy passw", copyy).pack(pady=5)
    buton("Exit", exit).pack(pady=20)
    window.mainloop()

random_pass()



