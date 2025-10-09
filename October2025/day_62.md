## October 9, 2025 - Day 62

### What I Worked On:  
Exercism - Worked on a simple function dealing with conditionals for strings. 

### Concepts Practiced:  
- String conditionals
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def response(hey_bob):
    '''This function determines what Bob (a lackadaisical teenager) will reply when someone says something to him
    param: str
    return: str'''
    
    if hey_bob.isupper() and hey_bob[-1] == "?":
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    elif "?" in hey_bob and hey_bob[-1] != ".":
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

```
