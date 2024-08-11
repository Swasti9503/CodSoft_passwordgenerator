import tkinter as tk
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8',
           '9', '10']
symbols = ['!', '#', '$', '%', '(', ')', '*', '@', '+', '&']

def generate_password():
    n_letters = int(ent_letters.get())
    n_symbols = int(ent_symbols.get())
    n_numbers = int(ent_numbers.get())
    password_list = []
    for i in range(1, n_letters+1):
        char = random.choice(letters)
        password_list.append(char)
    for i in range(1, n_symbols+1):
        char = random.choice(symbols)
        password_list.append(char)
    for i in range(1, n_numbers+1):
        char = random.choice(numbers)
        password_list.append(char)
    random.shuffle(password_list)
    password = "".join(password_list)
    lbl_password.config(text="Generated Password: " + password)

window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")  # increased size

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3, bg="lightblue")  # changed background color
frm_form.pack(fill="both", expand=True)

lbl_letters = tk.Label(master=frm_form, text="How many letters?", font=("Arial", 14))  # increased font size
ent_letters = tk.Entry(master=frm_form, width=20, font=("Arial", 14))  # increased font size and width
lbl_letters.grid(row=0, column=0, sticky="e", padx=10, pady=10)  # added padding
ent_letters.grid(row=0, column=1, padx=10, pady=10)

lbl_symbols = tk.Label(master=frm_form, text="How many symbols?", font=("Arial", 14))
ent_symbols = tk.Entry(master=frm_form, width=20, font=("Arial", 14))
lbl_symbols.grid(row=1, column=0, sticky="e", padx=10, pady=10)
ent_symbols.grid(row=1, column=1, padx=10, pady=10)

lbl_numbers = tk.Label(master=frm_form, text="How many numbers?", font=("Arial", 14))
ent_numbers = tk.Entry(master=frm_form, width=20, font=("Arial", 14))
lbl_numbers.grid(row=2, column=0, sticky="e", padx=10, pady=10)
ent_numbers.grid(row=2, column=1, padx=10, pady=10)

btn_generate = tk.Button(master=frm_form, text="Generate Password", command=generate_password, font=("Arial", 14), bg="green", fg="white")  # changed button color and font
btn_generate.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

lbl_password = tk.Label(master=frm_form, text="Generated Password: ", font=("Arial", 14))
lbl_password.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
