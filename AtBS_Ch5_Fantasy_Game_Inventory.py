print ('Automate the Boring Stuff Chapter 5 Fantasy Game Inventory')

#You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
#Write a function named displayInventory() that would take any possible “inventory” and display it like the following:

# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + 1
        print (v, ' ', k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)
