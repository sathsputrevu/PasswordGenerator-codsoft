from tkinter import *
import string
import random
import pyperclip
from tkinter import ttk

def generate_password():
    password_length = int(length_Box.get())
    password_strength = strength_combo.get()

    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    if password_strength == 'Weak':
        character_pool = small_alphabets
    elif password_strength == 'Medium':
        character_pool = small_alphabets + capital_alphabets
    else:
        character_pool = small_alphabets + capital_alphabets + numbers + special_characters

    password = ''.join(random.sample(character_pool, password_length))
    passwordField.delete(0, END)
    passwordField.insert(0, password)

def copy_password():
    password = passwordField.get()
    pyperclip.copy(password)

root = Tk()
root.config(bg='#34495E')

passwordLabel = Label(root, text='Password Generator', font=('Arial', 20, 'bold'), bg='#34495E', fg='#ECF0F1')
passwordLabel.grid(pady=10)

strength_label = Label(root, text='Select Strength:', font=('Arial', 13), bg='#34495E', fg='#ECF0F1')
strength_label.grid(row=1, column=0, pady=5, padx=10, sticky=W)

strength_combo = ttk.Combobox(root, values=['Weak', 'Medium', 'Strong'], font=('Arial', 13), state='readonly')
strength_combo.current(0)
strength_combo.grid(row=1, column=1, pady=5, padx=10, sticky=W)

lengthLabel = Label(root, text='Password Length:', font=('Arial', 13), bg='#34495E', fg='#ECF0F1')
lengthLabel.grid(row=2, column=0, pady=5, padx=10, sticky=W)

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=('Arial', 13))
length_Box.grid(row=2, column=1, pady=5, padx=10, sticky=W)

generateButton = Button(root, text='Generate', font=('Arial', 13, 'bold'), command=generate_password, bg='#2ECC71', fg='#ECF0F1')
generateButton.grid(row=3, column=0, columnspan=2, pady=10)

passwordField = Entry(root, width=25, bd=2, font=('Arial', 13))
passwordField.grid(row=4, column=0, columnspan=2, pady=5)

copyButton = Button(root, text='Copy', font=('Arial', 13, 'bold'), command=copy_password, bg='#3498DB', fg='#ECF0F1')
copyButton.grid(row=5, column=0, columnspan=2, pady=5)

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x_offset = (root.winfo_screenwidth() - width) // 2
y_offset = (root.winfo_screenheight() - height) // 2
root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

root.mainloop()
