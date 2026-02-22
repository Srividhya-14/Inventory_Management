import json 

# Task 1 - Read the inventory
with open('inventory.json', 'r') as file_handler:
    inventory = json.load(file_handler) 
    print(len(inventory))

# Task 2 — Update and save
new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}
inventory.append(new_book) 

with open("inventory.json",'w') as file_handler:
    json.dump(inventory,file_handler,indent=4) 

# Task 3 — Display the inventory
with open('inventory.json', 'r') as file_handler: 
    display_inventory = json.load(file_handler) 

for book in display_inventory:
        print(f"Title: {book['title']:<15} | Author: {book['author']:<15} | Price: ${book['price']:<15}")
