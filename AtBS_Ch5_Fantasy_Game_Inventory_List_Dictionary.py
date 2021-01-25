print ('Automate the Boring Stuff Chapter 5 List to Dictionary Function for Fantasy Game Inventory')

#Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + 1
        print (v,k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)

#new code here
def addToInventory(inventory, addedItems):

    for i in addedItems:
         inventory[i] = inventory.get(i, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
