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
products = []
product_counter = 1


def add_product():
    global product_counter

    while True:
        print("\n==============================")
        print("        ADD PRODUCT")
        print("==============================")

        # Auto-generated product number
        product_number = product_counter

        # Input details
        product_name = input("Enter Product Name: ")
        product_unit = input("Enter Product Unit: ")
        product_quantity = int(input("Enter Product Quantity: "))
        product_price = float(input("Enter Product Price: "))

        # Store product in dictionary
        product = {
            "Product Number": product_number,
            "Product Name": product_name,
            "Product Unit": product_unit,
            "Product Quantity": product_quantity,
            "Product Price": product_price
        }

        # Confirm add
        confirm = input("\nType 'Add' to confirm product: ")

        if confirm.lower() == "add":
            products.append(product)
            product_counter += 1

            print("\nPRODUCT ADDED SUCCESSFULLY!")
            print("==============================")
            print(f"Product Number : {product['Product Number']}")
            print(f"Product Name   : {product['Product Name']}")
            print(f"Product Unit   : {product['Product Unit']}")
            print(f"Product Qty    : {product['Product Quantity']}")
            print(f"Product Price  : {product['Product Price']}")
            print("==============================")

        else:
            print("\nProduct not added.")

        # Return button
        choice = input("\nType 'Return' to go back to Main Menu: ")

        if choice.lower() == "return":
            break


# =========================
# MAIN MENU
# =========================

while True:
    print("\n==============================")
    print("         MAIN MENU")
    print("==============================")
    print("1. Add Product")
    print("2. Return / Exit")

    option = input("Choose Option: ")

    if option == "1":
        add_product()

    elif option == "2":
        print("\nReturning...")
        break

    else:
        print("\nInvalid Option.")







































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
deleted_products = []
inventory = []

def view_deleted_products():
    print("\n--- Deleted Products ---")
    if not deleted_products:
        print("No deleted products found.")
    else:
        for product in deleted_products:
            print(f"Product Number: {product['number']}, "
                  f"Name: {product['name']}, "
                  f"Unit: {product['unit']}, "
                  f"Quantity: {product['quantity']}, "
                  f"Price: {product['price']}")
    print("------------------------")

def restore_product(product_number):
    for product in deleted_products:
        if product['number'] == product_number:
            inventory.append(product)
            deleted_products.remove(product)
            print(f"\n Product number {product_number} has been successfully restored!\n")
            return
    print(f"\n Product number {product_number} not found in deleted products.\n")

def return_to_main_menu():
    print("\nReturning to Main Menu...\n")
























#End