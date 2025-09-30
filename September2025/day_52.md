## September 29, 2025 - Day 52

### What I Worked On:  
Exercism - Worked more on dictionaries. I learned different ways to combine dictionaries and dictionaries plus other iterables. I only knew update before.  

### Concepts Practiced:  
- Dictionaries
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)

    
### Exercism Code: 
```python
"""Functions to manage a users shopping cart items."""

def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart[item] = 1
    return cart
    

def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    ideas |= recipe_updates
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetical order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))
       
```
