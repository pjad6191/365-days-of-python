## October 6, 2025 - Day 59

### What I Worked On:  
Exercism - Worked on a function to determine if a sentence is a panagram. It was a nice review of a couple string manipulation tools. 

### Concepts Practiced:  
- Conditionals
- String manipulation
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

import string 

def is_pangram(sentence):
    '''Determines if a sentence is a panagram.
    param: string
    return: Boolean
    '''
    
    lsentence = sentence.lower()
    stripped = lsentence.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    lowercase = string.ascii_lowercase
    
    for letter in lowercase:
        if letter not in stripped:
            return False
    return True 

```
