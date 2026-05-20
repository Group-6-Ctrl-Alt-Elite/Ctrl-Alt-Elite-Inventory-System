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







































#YBAÑEZ





























#End