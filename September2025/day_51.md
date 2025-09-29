## September 28, 2025 - Day 51

### What I Worked On:  
Exercism - Worked on dictionaries. For the most part it was easy, but I got hung up on one of the functions. I didn't try to get help though. At this level, I'm able to troubleshoot until I figure it out on my own, which I did in this case. Generally I use a lot of print statements to see if I'm getting the result I want at each step. That usually helps, and I am able to find where I messed up. My goal is to learn and not just get the code. 

### Concepts Practiced:  
- Dictionaries
- Loops
- Tuples
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)

    
### Exercism Code: 
```python
"""Functions to keep track and alter inventory."""

def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    items_dict = {}
    for element in items:
        if element not in items_dict:
            items_dict[element] = 1
        else: 
            items_dict[element] += 1
    return items_dict


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for element in items:
        if element not in inventory:
            inventory[element] = 1
        else: 
            inventory[element] += 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for element in items:
        if element in inventory:
            if inventory[element] > 1:
                inventory[element] -= 1
            else:
                inventory[element] = 0
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        del inventory[item]
    return inventory 
    

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inventory_list = []
    for key in inventory:
        if inventory[key] > 0:
            inventory_list.append((key, inventory[key]))
    return inventory_list
       
```
