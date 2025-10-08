## October 7, 2025 - Day 60

### What I Worked On:  
Exercism - Worked on a function to determine if an ISBN is valid. 

### Concepts Practiced:  
- Conditionals
- String manipulation
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

def is_valid(isbn):
    '''This function determines if a given isbn-10 number is valid.
    param: str
    return: Bool'''

    #Remove dashes
    stripped = isbn.replace("-", "")

    #Put the numbers in a list to better manipulate
    isbn_list = list(stripped)
    
    #Account for lengths other than 10
    if len(isbn_list) != 10:
        return False
    
    #Replace any "X"
    if isbn_list[9] == "X":
        isbn_list[9] = "10"

    #Acccount for any other letters:
    for char in isbn_list:
        if char.isalpha():
            return False

    #Add up all the numbers in the isbn number
    sum = 0
    count = 10 
    for char in isbn_list:
        sum += count * int(char)
        count -= 1

    #Check if the number is valid 
    if sum % 11 == 0:
        return True
        
    return False

```
