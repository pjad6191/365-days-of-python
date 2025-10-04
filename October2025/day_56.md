## October 3, 2025 - Day 56

### What I Worked On:  
Exercism - Practiced handling different types 

### Concepts Practiced:  
- Numbers
- Strings
- Booleans
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def is_armstrong_number(number):
    '''An Armstrong number is a number that is the sum of its own digits
    each raised to the power of the number of digits in the number.
    param: int
    return: Boolean, True if number is an Armstrong number'''
    
    sum = 0
    if number > 0: 
        for digit in str(number):
            sum+= (int(digit)**(len(str(number))))

    if sum == number:
        return True
    return False 
```
