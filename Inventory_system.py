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
import tkinter as tk
from tkinter import messagebox

file_name = "Inventory_system.txt"

root = tk.Tk()
root.title("Inventory System")
root.geometry("500x400")


# MAIN MENU


def main_menu():
    clear_screen()

    tk.Label(root, text="MAIN MENU", font=("Arial", 16)).pack(pady=20)

    tk.Button(root,
              text="View Inventory",
              width=20,
              command=view_inventory).pack(pady=10)



# VIEW INVENTORY


def view_inventory():
    clear_screen()

    tk.Label(root,
             text="VIEW INVENTORY",
             font=("Arial", 16)).pack(pady=10)

    inventory_box = tk.Text(root, width=50, height=10)
    inventory_box.pack()

    try:
        with open(file_name, "r") as file:
            inventory_box.insert(tk.END, file.read())
    except FileNotFoundError:
        inventory_box.insert(tk.END, "No inventory records found.")

    tk.Button(root,
              text="Delete a Product",
              command=delete_product_screen).pack(pady=10)

    tk.Button(root,
              text="Return",
              command=main_menu).pack(pady=5)



# DELETE PRODUCT SCREEN


def delete_product_screen():
    clear_screen()

    tk.Label(root,
             text="DELETE PRODUCT",
             font=("Arial", 16)).pack(pady=10)

    tk.Label(root,
             text="Enter Product Number:").pack()

    product_entry = tk.Entry(root)
    product_entry.pack(pady=5)

    def confirm_delete():

        product_number = product_entry.get()

        answer = messagebox.askyesno(
            "Confirmation",
            f"Are you sure you want to delete product number {product_number}?"
        )

        if answer:

            try:
                with open(file_name, "r") as file:
                    lines = file.readlines()

                with open(file_name, "w") as file:
                    for line in lines:
                        if not line.startswith(product_number):
                            file.write(line)

                messagebox.showinfo(
                    "Deleted",
                    f'The product number "{product_number}" is successfully deleted.'
                )

            except FileNotFoundError:
                messagebox.showerror("Error", "Inventory file not found.")

    tk.Button(root,
              text="YES",
              width=10,
              command=confirm_delete).pack(pady=5)

    tk.Button(root,
              text="NO",
              width=10,
              command=view_inventory).pack(pady=5)

    tk.Button(root,
              text="Return",
              width=10,
              command=main_menu).pack(pady=10)


# CLEAR SCREEN FUNCTION
    

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


# START PROGRAM
main_menu()

root.mainloop()






































#YBAÑEZ





























#End