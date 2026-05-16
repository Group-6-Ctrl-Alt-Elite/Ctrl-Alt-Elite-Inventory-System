import tkinter as tk
from tkinter import *

file = "Inventory_system.txt"

def save():
    text = Entry.get()
    with open("Inventory_system.txt", "a") as file:
        file.write(text + "\n")
        
root = tk.Tk()
root.state()

frame = tk.Frame(root, padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")

root.title("Inventory System")
tk.Label(root, text="\nWELCOME TO THE INVENTORY SYSTEM\n").pack()
tk.Label(root, text= "\nUSER LOG IN\n").pack()

root.geometry("400x300")


#USER LOG IN
Users = {
    "Admin": "admin123",
    "User1": "user123",
    "User2": "12345"
}

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    while True:
        if username in Users and Users[username] == password:
            tk.Label(root, text="Login successful!").pack()
            break
        
        else:
            tk.Label(root, text="Invalid username or password.").pack()
            break
        
tk.Label(root, text="Username:").pack()
username_entry = Entry(root, show="").pack()
tk.Label(root, text="Password:").pack()
password_entry = Entry(root, show="*").pack()
sign_in = Button(root, text="Sign In", command=login)
sign_in.pack()

root.mainloop()








#MAESTRADO







































#Ranile







































#YEE







































#TUPAG







































#YBAÑEZ





























#End