def display_inventory(inventory):
    """Display all items in the inventory."""
    print("\n===== CURRENT INVENTORY =====")
    if not inventory:
        print("The inventory is empty.")
    else:
        print(f"{'ID':<5}{'Name':<15}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        for item_id, item in inventory.items():
            print(f"{item_id:<5}{item['name']:<15}${item['price']:<9}{item['quantity']:<10}")
    print("=" * 40)

def add_item(inventory):
    """Add a new item to the inventory."""
    print("\n===== ADD NEW ITEM =====")
    
    # Generate a new item ID (max existing ID + 1)
    new_id = 1 if not inventory else max(inventory.keys()) + 1
    
    name = input("Enter item name: ")
    
    # Validate price input
    while True:
        try:
            price = float(input("Enter price: $"))
            if price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Validate quantity input
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    # Add the new item to inventory
    inventory[new_id] = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    
    print(f"\nItem '{name}' added to inventory with ID: {new_id}")
    return inventory

def update_item(inventory):
    """Update an existing item in the inventory."""
    if not inventory:
        print("\nThe inventory is empty. Nothing to update.")
        return inventory
        
    print("\n===== UPDATE ITEM =====")
    display_inventory(inventory)
    
    # Validate item ID input
    while True:
        try:
            item_id = int(input("\nEnter ID of item to update (or 0 to cancel): "))
            if item_id == 0:
                print("Update canceled.")
                return inventory
            if item_id not in inventory:
                print(f"No item with ID {item_id} exists. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    item = inventory[item_id]
    print(f"\nUpdating: {item['name']} (ID: {item_id})")
    print("Leave blank to keep the current value.")
    
    # Update name
    new_name = input(f"Current name: {item['name']}\nNew name: ")
    if new_name:
        item['name'] = new_name
    
    # Update price
    while True:
        new_price = input(f"Current price: ${item['price']}\nNew price: $")
        if not new_price:
            break
        try:
            new_price = float(new_price)
            if new_price < 0:
                print("Price cannot be negative. Please try again.")
                continue
            item['price'] = new_price
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Update quantity
    while True:
        new_quantity = input(f"Current quantity: {item['quantity']}\nNew quantity: ")
        if not new_quantity:
            break
        try:
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                print("Quantity cannot be negative. Please try again.")
                continue
            item['quantity'] = new_quantity
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
    
    print(f"\nItem with ID {item_id} has been updated.")
    return inventory

def remove_item(inventory):
    """Remove an item from the inventory."""
    if not inventory:
        print("\nThe inventory is empty. Nothing to remove.")
        return inventory
        
    print("\n===== REMOVE ITEM =====")
    display_inventory(inventory)
    
    # Validate item ID input
    while True:
        try:
            item_id = int(input("\nEnter ID of item to remove (or 0 to cancel): "))
            if item_id == 0:
                print("Removal canceled.")
                return inventory
            if item_id not in inventory:
                print(f"No item with ID {item_id} exists. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    item_name = inventory[item_id]['name']
    confirm = input(f"Are you sure you want to remove '{item_name}'? (y/n): ")
    
    if confirm.lower() == 'y':
        del inventory[item_id]
        print(f"\nItem '{item_name}' has been removed from the inventory.")
    else:
        print("\nRemoval canceled.")
    
    return inventory

def main():
    """Main function to run the inventory management system."""
    # Initial inventory
    inventory = {
        1: {'name': 'Laptop', 'price': 999.99, 'quantity': 10},
        2: {'name': 'Mouse', 'price': 24.99, 'quantity': 25},
        3: {'name': 'Keyboard', 'price': 49.99, 'quantity': 15},
        4: {'name': 'Monitor', 'price': 149.99, 'quantity': 8},
        5: {'name': 'Headphones', 'price': 79.99, 'quantity': 20}
    }
    
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. View all items")
        print("2. Add new item")
        print("3. Update existing item")
        print("4. Remove item")
        print("5. Exit")
        
        # Get user choice
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            inventory = add_item(inventory)
        elif choice == '3':
            inventory = update_item(inventory)
        elif choice == '4':
            inventory = remove_item(inventory)
        elif choice == '5':
            print("\nThank you for using the Inventory Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()