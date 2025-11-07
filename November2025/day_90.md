## November 6, 2025 - Day 90

### What I Worked On:  
**Exercism:**
- Created a function that converts a phrase to an acronym.
 
### Concepts Practiced:  
- Strings 
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def abbreviate(words):
    """
    Converts a phrase to its acronym
    Param: str (phrase)
    Return: str (acronym)
    """
    
    #Replace any hyphens with a space, Make capita;
    words = words.replace("-", " ").replace("_", " ").upper()
    
    #Separate words
    word_list = words.split()
    
    #Initialize return string
    acronym = ""
    
    #Take first letter from each word 
    for word in word_list:
        acronym = acronym + word[0]

    return acronym



```
