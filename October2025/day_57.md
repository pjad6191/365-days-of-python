## October 4, 2025 - Day 57

### What I Worked On:  
Exercism - A nice quick, easy function for a busy Saturday.

### Concepts Practiced:  
- Conditionals
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def convert(number):
    '''This function converts a number (int) into its corresponding raindrop sounds.
    If a given number:
        is divisible by 3, add "Pling" to the result.
        is divisible by 5, add "Plang" to the result.
        is divisible by 7, add "Plong" to the result.
        is not divisible by 3, 5, or 7, the result should be the number as a string.'''

    raindrops = ""
    if number % 3 == 0:
        raindrops += "Pling"
    if number % 5 == 0:
        raindrops += "Plang"
    if number % 7 == 0:
        raindrops += "Plong"
    if raindrops == "":
        return str(number)
    return raindrops
```
