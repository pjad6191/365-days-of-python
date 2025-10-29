## October 28, 2025 - Day 81

### What I Worked On:  
**Exercism:**  
I worked on a couple simple functions. One was just changing the way letters and their point values are stored for a game. It was mainly about looping through dictionary keys and values and mapping them to a new dictionary. The second function dealt with sets and the instructions were more complicated than the function itself. 

### Concepts Practiced:  
- Dictionaries
- Sets
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def transform(legacy_data):
  #Initialize dictionary for new mapping
  new_mapping = {}

  #Loop through dictionary keys
  for key in legacy_data:
      #Loop through the values (which are lists)
      for item in legacy_data[key]:
          #Add to new dictionary
          new_mapping[item.lower()] = key

  return new_mapping


def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """
    Calculate the total energy points awarded for completing a level in the fantasy-survival game.

    The player earns points based on multiples of each magical item's base value.
    For each value in `multiples`, this function finds all unique multiples of that number
    that are less than the given `limit`, combines them, removes duplicates, and returns
    the sum of all remaining values.

    Example:
        limit = 20
        multiples = [3, 5]
        Multiples of 3 < 20: 3, 6, 9, 12, 15, 18
        Multiples of 5 < 20: 5, 10, 15
        Unique combined set: {3, 5, 6, 9, 10, 12, 15, 18}
        Result = 78

    Param:
    - limit (int): Upper bound (exclusive) for the multiples to be considered.
    - multiples (list[int]): Base values of the magical items collected.

    Returns:
    - int: The sum of all unique multiples of provided base values that are less than `limit`.
    """

    multiple_set = set()
        
    for num in multiples:
        if num == 0:
            continue  #Avoids infinite loops
        count = 1
        multiple = num*count
    
        while multiple < limit:
            multiple_set.add(multiple)
            count += 1
            multiple = num * count
    
    return sum(multiple_set)

    




```
