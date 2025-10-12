## October 11, 2025 - Day 64

### What I Worked On:  
Exercism:
- Worked on a function for reversing a string, but it was only one line long, so I wanted to do something else.
- I worked on an additional function that determined if a string was an isogram. 

### Concepts Practiced:  
- Sequences
- Strings
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def reverse(text):
    return text[::-1]

def is_isogram(string):
    '''This function determines if a word or phrase is an isogram.
    An isogram is a word or phrase without a repeating letter, however spaces and
    hyphens are allowed to appear multiple times.

    param: string
    return: Boolean
    '''

    #Initialize a list to hold letters in string
    letter_list = []

    #To account for capital letters
    word = string.lower()

    for char in word:
        if char.isalpha():  #Only concerned with letters
            if char in letter_list:
                return False
             
            else:
                letter_list.append(char)
    return True

```
