import string
import random
import tkinter as tk
from tkinter import messagebox


# Checking the user input and returning it
def pass_length(length):
    if length.isdigit() and int(length) > 0:
        return int(length)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

# Returning the character set chosen by user
def char_choice(ch):
    if ch == "1":
        return string.ascii_letters  # Letters(uppercase and lowercase)
    elif ch == "2":
        return string.digits     # Numbers
    elif ch == "3":
        return string.ascii_letters + string.digits    # Letters and Numbers
    elif ch == "4":
        return string.ascii_letters + string.punctuation  # Letters and Symbols
    elif ch == "5":
        return string.digits + string.punctuation      # Numbers and Symbols
    elif ch == "6":
        return string.ascii_letters + string.digits + string.punctuation    # Numbers, Digits and Symbols
    else:
        messagebox.showerror("Error","Please select atleast 1 Character set")

# Randomly generating the Password from the chosen character set
def generate_pass(l, c):
    return "".join(random.choice(c) for _ in range(l))

# Function to handle the button click event
def generate_password():
    length = pass_length(entry_length.get())
    char_set = char_choice(choice.get())
    if length and char_set:
        password = generate_pass(length, char_set)
        password_entry.delete(0, tk.END)  # Clearing the previous password
        password_entry.insert(0, password)  # Inserting new password

# Copying the generated password to the clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)

# Pasting the copied password from the clipboard
def paste_password():
        pasted_password = root.clipboard_get()  # Retrieving from clipboard
        password_entry.delete(0, tk.END)  # Clearing the existing content
        password_entry.insert(0, pasted_password)  # Inserting the pasted content

# Creating the GUI using Tkinter
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")
root.configure(bg="black")

# Label and Entry field for password length
# Taking input (password length) from the user 
frame_length = tk.Frame(root, bg="black")
frame_length.pack(pady=40)

label_length = tk.Label(frame_length, text="Enter Password Length:", bg="black", fg="white")
label_length.pack(side="left", padx=5)

entry_length = tk.Entry(frame_length, bg="darkgrey", fg="black")
entry_length.pack(side="left", padx=5)

# Label for Character set 
label_choice = tk.Label(root, text="Choose Character Set:", bg="black", fg="white")
label_choice.pack(pady=10)

# Buttons for choosing Character set
choice = tk.StringVar()  

radio1 = tk.Radiobutton(root, text="Only Letters", variable=choice, value="1", bg="black", fg="white", indicatoron=False, selectcolor="grey")
radio1.pack()
radio2 = tk.Radiobutton(root, text="Only Numbers", variable=choice, value="2", bg="black", fg="white", indicatoron=False, selectcolor="grey")
radio2.pack()
radio3 = tk.Radiobutton(root, text="Letters and Numbers", variable=choice, value="3", bg="black", fg="white", indicatoron=False, selectcolor="grey")
radio3.pack()
radio4 = tk.Radiobutton(root, text="Letters and Symbols", variable=choice, value="4", bg="black", fg="white", indicatoron=False, selectcolor="grey")
radio4.pack()
radio5 = tk.Radiobutton(root, text="Numbers and Symbols", variable=choice, value="5", bg="black", fg="white", indicatoron=False, selectcolor="grey")
radio5.pack()
radio6 = tk.Radiobutton(root, text="Letters, Numbers, and Symbols", variable=choice, value="6", bg="black", fg="white", indicatoron=False, selectcolor="grey")
radio6.pack()

# Button for generating the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="grey", fg="black")
generate_button.pack(pady=20)

# Entry field for displaying the generated password
frame_length = tk.Frame(root, bg="black")
frame_length.pack(pady=30)

result_label = tk.Label(frame_length, text="Generated Password:", bg="black", fg="white")
result_label.pack(side="left", padx=5)

password_entry = tk.Entry(frame_length, bg="lightgrey", fg="black")
password_entry.pack(side="left", padx=5)

# Button to copy password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="grey", fg="black")
copy_button.pack(pady=10)

# Button to paste password from clipboard into the password entry field
paste_button = tk.Button(root, text="Paste Password", command=paste_password, bg="grey", fg="black")
paste_button.pack(pady=10)

# Running the Tkinter loop
root.mainloop()
