## September 30, 2025 - Day 53

### What I Worked On:  
Exercism - I tried some of the regular practice questions, not part of the learning modules. Very tired today!!  

### Concepts Practiced:  
- Writing functions
- Practicing previous skills. 
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)

    
### Exercism Code: 
```python

def leap_year(year):
    """ Determine if a year is a leap year 
    :param year: int - year to check 
    :return: Bool - True if it's a leap year 
    """

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        return False
    if year % 4 == 0:
        return True 
        
    return False 
   

```
