## October 23, 2025 - Day 76

### What I Worked On:  
**Exercism:**  
I created a function that takes a nested array of any depth and returns a fully flattened array. I had a little bit of a hard time first thinking of the logic to keep going deeper into a list until it was totally flat. I had to do a bit of testing and debugging. 

**Neural Data Science:**  
I read the section on panda DataFrames, mostly as review, and went out the exercises in the online text. 

### Concepts Practiced:  
- Lists
- Loops
- Testing and debugging
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Neural Data Science](https://neuraldatascience.io/3-python/pandas_dataframes.html)
    
### Exercism Code: 
```python

def flatten(iterable):
    '''
    This function takes a nested array of any depth and return a fully flattened array.
    param: list (nested)
    return: list (flattened)
    '''
    
    #Initialize lists
    stack = [iterable]
    return_list = []
    
    while stack:
        #Takes the last item off the stack
        current = stack.pop()

        #If it's a list, pushes its items in reverse order
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
                
        #If it's a number and not bool, adds it to the return list
        elif isinstance(current, (int, float)) and not isinstance(current, bool):
            return_list.append(current)
        
    return return_list

```
