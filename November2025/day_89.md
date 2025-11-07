## November 5, 2025 - Day 89

### What I Worked On:  
**Exercism:**
- Created a function that given a string containing brackets [], braces {}, parentheses (), or any combination thereof, it will verify that any and all pairs are matched and nested correctly. I could easily determine in the pairs were matching, but the nested part took a little bit to figure out. I needed to create a dictionary for the pairs, and to use a list to add values to temporarily to check if they were nested correctly. 
 
### Concepts Practiced:  
- Conditionals 
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def is_paired(input_string):
    """
    Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly.
    
    Param: str
    Return: Bool
    """
    #Create a set containing left end of pairs
    l_set = set("([{")

    #Create a dictionary of pairs
    pairs = {
        ")":"(", 
        "]":"[", 
        "}":"{"
    }

    #Initialize a list to check symbols 
    check_list = []
    
    #Loop through string to check for symbols
    for char in input_string:

        if char in l_set:
            check_list.append(char)  #Adds left part to check_list

        elif char in pairs:
            #Check to see if its matching pair in in check_list
            #Check to see if its the last one added for nesting purposes
            if not check_list or check_list[-1] != pairs[char]:
                return False 
            #Take out the last item 
            check_list.pop()

    #True if check_list empty, no unbalanced symbols         
    return not check_list

```
