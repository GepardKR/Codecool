
def display_inventory(inventory):

    for kubus,tygrysek in inventory.items():
        print(kubus,tygrysek)

def add_to_inventory(inventory, added_items):
    for x in range(len(added_items)):
        for y in inventory:
            '''if added_items[x] in inventory:
                added_items[x] += added_items[x]
                print(added_items)'''
            if added_items[x] == y:
                inventory[y] += 1
        
    for x in range(len(added_items)):
        if added_items[x] not in inventory:
            inventory[added_items[x]] = 1

def main():
    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inv, dragon_loot)
    display_inventory(inv)

main()