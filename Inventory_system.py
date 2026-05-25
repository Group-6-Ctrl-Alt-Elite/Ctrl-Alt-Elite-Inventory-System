import os
import tkinter as tk
from tkinter import messagebox 

file_name = "Inventory_system.txt"
deleted_file_name = "Deleted_inventory.txt"

Users = {
    "Admin": "admin123",
    "Maomao": "Mao09",
    "Elinar123": "12345", 
    "Allyzaya": "Ally05",
    "Eddieboy": "EddieIT",
    "MaryGrace": "MG0067",
    "Yeegio": "Yee2324",
}

root = tk.Tk()
root.title("Ctrl Alt Elite Inventory System")
root.geometry("520x520")
root.resizable(False, False)


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def read_inventory():
    products = []
    if not os.path.exists(file_name):
        return products

    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 5:
                continue
            products.append({
                "number": parts[0],
                "name": parts[1],
                "unit": parts[2],
                "quantity": parts[3],
                "price": parts[4]
            })
    return products


def write_inventory(products):
    with open(file_name, "w", encoding="utf-8") as file:
        for product in products:
            line = ",".join([
                product["number"],
                product["name"],
                product["unit"],
                product["quantity"],
                product["price"]
            ])
            file.write(line + "\n")


def read_deleted_inventory():
    deleted_products = []
    if not os.path.exists(deleted_file_name):
        return deleted_products

    with open(deleted_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 5:
                continue
            deleted_products.append({
                "number": parts[0],
                "name": parts[1],
                "unit": parts[2],
                "quantity": parts[3],
                "price": parts[4]
            })
    return deleted_products


def write_deleted_inventory(products):
    with open(deleted_file_name, "w", encoding="utf-8") as file:
        for product in products:
            line = ",".join([
                product["number"],
                product["name"],
                product["unit"],
                product["quantity"],
                product["price"]
            ])
            file.write(line + "\n")


def append_deleted_product(product):
    with open(deleted_file_name, "a", encoding="utf-8") as file:
        line = ",".join([
            product["number"],
            product["name"],
            product["unit"],
            product["quantity"],
            product["price"]
        ])
        file.write(line + "\n")


def get_next_product_number(products):
    if not products:
        return "1"
    numbers = [int(p["number"]) for p in products if p["number"].isdigit()]
    return str(max(numbers, default=0) + 1)


def renumber_products(products):
    for index, product in enumerate(products, start=1):
        product["number"] = str(index)
    return products


def show_login_screen():
    clear_screen()
    root.configure(bg="#39DEE4") 

    tk.Label(root, text="\nWELCOME TO THE CTRL ALT ELITE", font=("Courier", 16, "bold"), pady=10, bg="#3FD8DD").pack()
    tk.Label(root, text="INVENTORY SYSTEM\n", font=("Courier", 16, "bold"), pady=10, bg="#3FD8DD").pack()
    tk.Label(root, text="\nUSER LOG IN\n", bg="#39DEE4", font=("Courier", 14, "bold")).pack(pady=5)

    tk.Label(root, text="Username:", bg="#39DEE4", anchor="w").pack(fill="x", padx=20, pady=(15, 0))
    username_var = tk.StringVar(value="Admin")
    tk.OptionMenu(root, username_var, *Users.keys()).pack(fill="x", padx=40)

    tk.Label(root, text="Password:", bg="#39DEE4", anchor="w").pack(fill="x", padx=20, pady=(10, 0))
    password_entry = tk.Entry(root, show="*")
    password_entry.pack(fill="x", padx=40)

# LOGIN FUNCTION
    def login():
        username = username_var.get().strip()
        password = password_entry.get().strip()
        print(f"username: '{username}' password: '{password}'")
        print(f"users: {list(Users.keys())}")
        normalized_users = {u.casefold(): p for u, p in Users.items()}
        normalized_username = username.casefold()
        if normalized_username in normalized_users and normalized_users[normalized_username] == password:
            messagebox.showinfo("Login", "Login successful.")
            show_main_menu()
        else:
            if normalized_username not in normalized_users:
                messagebox.showerror("Login Failed", "Username not found.")
            else:
                messagebox.showerror("Login Failed", "Password is wrong. Passwords are case-sensitive.")

    tk.Button(root, text="Sign In", width=15, command=login).pack(pady=20)
    tk.Button(root, text="Exit", width=15, command=root.destroy).pack()

# MAIN MENU
def show_main_menu():
    clear_screen()

    tk.Label(root, text="CTRL ALT ELITE MAIN MENU", font=("Arial", 16, "bold"), pady=10).pack()

    tk.Button(root, text="Add Product", width=20, command=show_add_product_screen).pack(pady=8)
    tk.Button(root, text="View Inventory", width=20, command=show_inventory_screen).pack(pady=8)
    tk.Button(root, text="Update Product", width=20, command=show_update_product_screen).pack(pady=8)
    tk.Button(root, text="Delete Product", width=20, command=show_delete_product_screen).pack(pady=8)
    tk.Button(root, text="Restore Deleted Product", width=20, command=show_restore_product_screen).pack(pady=8)
    tk.Button(root, text="Logout", width=20, command=show_login_screen).pack(pady=20)

# ADD PRODUCT
def show_add_product_screen():
    clear_screen()

    products = read_inventory()
    product_number = get_next_product_number(products)

    tk.Label(root, text="ADD PRODUCT", bg="#39DEE4", font=("Arial", 16, "bold"), pady=10).pack()
    tk.Label(root, text=f"Product Number: {product_number}", bg="#39DEE4", font=("Arial", 12)).pack(pady=(0, 10))

    tk.Label(root, text="Product Name:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40)
    name_entry = tk.Entry(root, bg="#FFFFFF")
    name_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Unit:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    unit_entry = tk.Entry(root, bg="#FFFFFF")
    unit_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Quantity:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    quantity_entry = tk.Entry(root, bg="#FFFFFF")
    quantity_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Price:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    price_entry = tk.Entry(root, bg="#FFFFFF")
    price_entry.pack(fill="x", padx=40)

    def save_product():
        name = name_entry.get().strip()
        unit = unit_entry.get().strip()
        quantity = quantity_entry.get().strip()
        price = price_entry.get().strip()

        if not name or not unit or not quantity or not price:
            messagebox.showwarning("Missing Data", "Please complete all fields.")
            return

        if not quantity.isdigit():
            messagebox.showwarning("Invalid Value", "Quantity must be an integer.")
            return

        try:
            float(price)
        except ValueError:
            messagebox.showwarning("Invalid Value", "Price must be a number.")
            return

        products.append({
            "number": product_number,
            "name": name,
            "unit": unit,
            "quantity": quantity,
            "price": price
        })
        write_inventory(products)
        messagebox.showinfo("Saved", "Product saved successfully.")
        show_inventory_screen()

    tk.Button(root, text="Save Product", width=20, command=save_product).pack(pady=15)
    tk.Button(root, text="Return", width=20, command=show_main_menu).pack()

# VIEW INVENTORY
def show_inventory_screen():
    clear_screen()

    tk.Label(root, text="CTRL ALT ELITE INVENTORY", bg="#39DEE4", font=("Courier", 16, "bold"), pady=10).pack()

    inventory_text = tk.Text(root, width=60, height=18)
    inventory_text.pack(padx=20)
    inventory_text.configure(state="normal")

    products = read_inventory()
    if not products:
        inventory_text.insert(tk.END, "No inventory records found.\n")
    else:
        for product in products:
            inventory_text.insert(
                tk.END,
                f"#{product['number']} | {product['name']} | {product['unit']} | Qty: {product['quantity']} | Price: {product['price']}\n"
            )

    inventory_text.configure(state="disabled")

    tk.Button(root, text="Return", width=20, command=show_main_menu).pack(pady=15)

# UPDATE PRODUCT
def show_update_product_screen():
    clear_screen()

    tk.Label(root, text="UPDATE PRODUCT", bg="#39DEE4", font=("Courier", 16, "bold"), pady=10).pack()

    tk.Label(root, text="Product Number:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40)
    product_number_entry = tk.Entry(root, bg="#FFFFFF")
    product_number_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Name:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    name_entry = tk.Entry(root, bg="#FFFFFF")
    name_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Unit:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    unit_entry = tk.Entry(root, bg="#FFFFFF")
    unit_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Quantity:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    quantity_entry = tk.Entry(root, bg="#FFFFFF")
    quantity_entry.pack(fill="x", padx=40)

    tk.Label(root, text="Product Price:", bg="#39DEE4", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    price_entry = tk.Entry(root, bg="#FFFFFF")
    price_entry.pack(fill="x", padx=40)

    def search_product():
        product_number = product_number_entry.get().strip()
        products = read_inventory()
        for product in products:
            if product["number"] == product_number:
                name_entry.delete(0, tk.END)
                name_entry.insert(0, product["name"])
                unit_entry.delete(0, tk.END)
                unit_entry.insert(0, product["unit"])
                quantity_entry.delete(0, tk.END)
                quantity_entry.insert(0, product["quantity"])
                price_entry.delete(0, tk.END)
                price_entry.insert(0, product["price"])
                return
        messagebox.showerror("Not Found", "Product not found.")

    def update_product():
        product_number = product_number_entry.get().strip()
        if not product_number:
            messagebox.showwarning("Missing Data", "Enter a product number first.")
            return

        products = read_inventory()
        updated = False
        for product in products:
            if product["number"] == product_number:
                product["name"] = name_entry.get().strip()
                product["unit"] = unit_entry.get().strip()
                product["quantity"] = quantity_entry.get().strip()
                product["price"] = price_entry.get().strip()
                updated = True
                break

        if not updated:
            messagebox.showerror("Not Found", "Product not found.")
            return

        if not product["name"] or not product["unit"] or not product["quantity"] or not product["price"]:
            messagebox.showwarning("Missing Data", "Please complete all fields.")
            return

        if not product["quantity"].isdigit():
            messagebox.showwarning("Invalid", "Quantity must be an integer.")
            return

        try:
            float(product["price"])
        except ValueError:
            messagebox.showwarning("Invalid", "Price must be a number.")
            return

        write_inventory(products)
        messagebox.showinfo("Updated", "Product updated successfully.")
        show_main_menu()

    tk.Button(root, text="Search", width=15, command=search_product).pack(pady=10)
    tk.Button(root, text="Update", width=15, command=update_product).pack(pady=5)
    tk.Button(root, text="Return", width=15, command=show_main_menu).pack(pady=15)

# DELETE PRODUCT
def show_delete_product_screen():
    clear_screen()

    tk.Label(root, text="DELETE PRODUCT", bg="#39DEE4", font=("Courier", 16, "bold"), pady=10).pack()

    products = read_inventory()
    inventory_text = tk.Text(root, width=60, height=12)
    inventory_text.pack(padx=20)
    inventory_text.configure(state="normal")

    if not products:
        inventory_text.insert(tk.END, "No inventory records found. Add products first.\n")
    else:
        for product in products:
            inventory_text.insert(
                tk.END,
                f"#{product['number']} | {product['name']} | {product['unit']} | Qty: {product['quantity']} | Price: {product['price']}\n"
            )

    inventory_text.configure(state="disabled")

    tk.Label(root, text="Product Number:", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    product_number_entry = tk.Entry(root)
    product_number_entry.pack(fill="x", padx=40)

    def confirm_delete():
        product_number = product_number_entry.get().strip()
        if not product_number:
            messagebox.showwarning("Missing Data", "Enter a product number.")
            return

        answer = messagebox.askyesno("Confirm Delete", f"Delete product number {product_number}?" )
        if not answer:
            return

        products = read_inventory()
        product_to_delete = None
        new_products = []
        for p in products:
            if p["number"] == product_number:
                product_to_delete = p
            else:
                new_products.append(p)

        if product_to_delete is None:
            messagebox.showerror("Not Found", "Product number not found.")
            return

        renumber_products(new_products)
        write_inventory(new_products)
        append_deleted_product(product_to_delete)
        messagebox.showinfo("Deleted", "Product deleted successfully.")
        show_main_menu()

    tk.Button(root, text="Delete", width=15, command=confirm_delete).pack(pady=15)
    tk.Button(root, text="Return", width=15, command=show_main_menu).pack()

# RESTORE DELETED PRODUCT
def show_restore_product_screen():
    clear_screen()

    tk.Label(root, text="RESTORE DELETED PRODUCT", bg="#39DEE4", font=("Courier", 16, "bold"), pady=10).pack()

    deleted_text = tk.Text(root, width=60, height=12)
    deleted_text.pack(padx=20)
    deleted_text.configure(state="normal")

    deleted_products = read_deleted_inventory()
    if not deleted_products:
        deleted_text.insert(tk.END, "No deleted products available to restore.\n")
    else:
        for index, product in enumerate(deleted_products, start=1):
            deleted_text.insert(
                tk.END,
                f"{index}. #{product['number']} | {product['name']} | {product['unit']} | Qty: {product['quantity']} | Price: {product['price']}\n"
            )

    deleted_text.configure(state="disabled")

    tk.Label(root, text="Restore List Number:", anchor="w").pack(fill="x", padx=40, pady=(10, 0))
    product_number_entry = tk.Entry(root)
    product_number_entry.pack(fill="x", padx=40)

    def restore_product():
        restore_number = product_number_entry.get().strip()
        if not restore_number:
            messagebox.showwarning("Missing Data", "Enter a restore list number.")
            return

        if not restore_number.isdigit():
            messagebox.showwarning("Invalid Value", "Enter a valid restore list number.")
            return

        deleted_products = read_deleted_inventory()
        index = int(restore_number) - 1
        if index < 0 or index >= len(deleted_products):
            messagebox.showerror("Not Found", "Restore list number not found.")
            return

        restored = deleted_products[index]
        remaining = [p for i, p in enumerate(deleted_products) if i != index]

        inventory = read_inventory()
        inventory.append(restored)
        renumber_products(inventory)
        write_inventory(inventory)
        write_deleted_inventory(remaining)
        messagebox.showinfo("Restored", "Product restored successfully.")
        show_main_menu()

    tk.Button(root, text="Restore", width=15, command=restore_product).pack(pady=10)
    tk.Button(root, text="Return", width=15, command=show_main_menu).pack()


if __name__ == "__main__":
    show_login_screen()
    root.mainloop()
