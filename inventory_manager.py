import json
import os

FILENAME = "inventory.json"

def load_inventory():
    """Loads inventory and transaction history from inventory.json if it exists."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error loading file. Starting with empty inventory.")
    
    # Initial default structure if file does not exist
    return {
        "products": [
            {"id": "101", "name": "Laptop", "stock": 10, "price": 1200.0, "transactions": []},
            {"id": "102", "name": "Mouse", "stock": 25, "price": 25.0, "transactions": []},
            {"id": "103", "name": "Keyboard", "stock": 15, "price": 45.0, "transactions": []}
        ]
    }
def save_inventory(inventory):
    """Saves inventory data to inventory.json."""
    try:
        with open(FILENAME, "w") as file:
            json.dump(inventory, file, indent=4)
        print("Inventory saved successfully.")
    except Exception as e:
        print(f"Error saving inventory: {e}")


def display_all(inventory):
    """Displays all products and their details."""
    products = inventory.get("products", [])
    if not products:
        print("\nNo products in inventory.")
        return

    print("\n--- Current Inventory ---")
    for prod in products:
        print(f"ID: {prod['id']} | Name: {prod['name']} | Stock: {prod['stock']} | Price: ${prod['price']:.2f}")
        if prod.get("transactions"):
            print(f"   Transaction History (Amounts): {prod['transactions']}")

def add_product(inventory):
    """Adds a new product dictionary to the inventory list."""
    prod_id = input("Enter Product ID: ").strip()
    
    # Check if ID already exists
    for prod in inventory["products"]:
        if prod["id"] == prod_id:
            print("Error: A product with this ID already exists.")
            return

    name = input("Enter Product Name: ").strip()
    try:
        stock = int(input("Enter Initial Stock Quantity: "))
        price = float(input("Enter Product Price: "))
    except ValueError:
        print("Invalid input for stock or price. Product creation canceled.")
        return

    new_prod = {
        "id": prod_id,
        "name": name,
        "stock": stock,
        "price": price,
        "transactions": []  # Stores history of all transaction amounts
    }
    
    inventory["products"].append(new_prod)
    print(f"Product '{name}' added successfully.")


def update_stock(inventory):
    """Updates the stock level and records transaction amount history."""
    prod_id = input("Enter Product ID to update stock: ").strip()
    
    for prod in inventory["products"]:
        if prod["id"] == prod_id:
            try:
                change = int(input("Enter stock change quantity (positive to add, negative to reduce): "))
            except ValueError:
                print("Invalid number.")
                return

            if prod["stock"] + change < 0:
                print("Error: Stock cannot fall below zero.")
                return

            prod["stock"] += change
            # Record the transaction amount history as requested in the scenario
            prod["transactions"].append(change)
            print(f"Updated stock for {prod['name']}. New Stock: {prod['stock']}")
            return

    print("Product not found.")
