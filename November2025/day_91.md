## November 7, 2025 - Day 91

### What I Worked On:  
**Exercism:**  
> I worked on a function that takes a letter as an input and returns a series of strings that creates a diamond made out of letters, beginning at A and expanding out toward the given letter, then back down to A. It took some trial and error to create the image that I wanted, but I got it. One thing I don't like about Exercism is that it's not always clear what output it's looking for. It wasn't clear that it was looking for a list of strings in this case. It could have been expecting one long string with newlines built in. 
 
### Concepts Practiced:  
- Strings
- Loops
- Testing and debugging
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
import string

def rows(letter):
    """
    The diamond kata takes as its input a letter, and outputs it in a diamond shape. 
    Given a letter, it prints a diamond starting with 'A', 
    with the supplied letter at the widest point.

    Param: letter (str)
    Return: list of strings
    """
    
    #Initialize return list of strings
    return_strings = []

    #Handle the case of one row
    if letter == "A":
        return ["A"]
        
    #Create a list of letters to loop through 
    letters = []
    for char in string.ascii_uppercase:
        letters.append(char)
        
        
    #Create a dictionary to show the size of the columns and rows
    size_dict = {}  
    count = 1
    for char in string.ascii_uppercase:
        size_dict[char] = count 
        count+=2
    
    #Helpful variable that shows half the length rounded down
    half = size_dict[letter]//2
    
    #Defines first and last rows
    beg_end = " "*half + "A" + " "*half
    
    #Print first row
    return_strings.append(beg_end)
    
    
    #Print First Half 
    first_middle = 1
    first_outer = half-1
    for row in range(0, half-1):
        return_strings.append(" "*first_outer + letters[row+1] + " "*first_middle + letters[row+1] +  " "*first_outer)
        first_outer -= 1
        first_middle += 2
    
    #Print Last Half
    middle_spaces = size_dict[letter]-2
    outer_spaces = 0 
    for row in range(half, 0, -1):
        return_strings.append(" "*outer_spaces + letters[row] + " "*middle_spaces + letters[row] +  " "*outer_spaces)
        outer_spaces += 1
        middle_spaces -= 2
      
    #Print last row 
    return_strings.append(beg_end)
    
    return return_strings

```
