## October 1, 2025 - Day 54

### What I Worked On:  
Exercism - I finished a dictionary assignment and then worked on an additional exercise to determine triangle type. 

### Concepts Practiced:  
- Dictionaries
- Booleans
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)

    
### Exercism Code: 
```python
"""Functions to manage a users shopping cart items."""

def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    combined = {key:[cart[key], *aisle_mapping[key]] for key in cart}
    combined_sorted = sorted(combined.items(), reverse=True) 
    return combined_sorted


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item, order in fulfillment_cart.items():
        if item in store_inventory:
            store_inventory[item][0] -= order[0]
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = "Out of Stock"
    return store_inventory


'''The following functions take a list of three sides of a triangle and return a Boolean indicating whether the three sides can form the type of triangle that the function is named after.'''

def equilateral(sides):
    if 0 not in sides:
        if sides[0] == sides[1] and sides[1] == sides[2]:
            return True
    return False 


def isosceles(sides):
    if 0 not in sides:
        if (sides[0] + sides[1]) >= sides[2] and (sides[1]+sides[2]) >= sides[0] and (sides[0]+sides[2]>=sides[1]):
            if sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]: 
                return True
    return False


def scalene(sides):
    if 0 not in sides:
        if (sides[0] + sides[1]) >= sides[2] and (sides[1]+sides[2]) >= sides[0] and sides[0]+sides[2]>=sides[1]:
            if sides[0]!=sides[1] and sides[0]!=sides[2] and sides[1]!=sides[2]:
                return True
    return False 

```
