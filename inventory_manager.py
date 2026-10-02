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
