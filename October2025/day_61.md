## October 8, 2025 - Day 61

### What I Worked On:  
Exercism - Worked on a function that when given a positive integer, returns the number of steps it takes to reach 1,       according to the rules of the Collatz Conjecture. I was surprised that it was actually easy. Often even easy programs take some working out but I got it on the first try. 

### Concepts Practiced:  
- Numbers
- Handling errors
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def steps(number):
    '''Given a positive integer, returns the number of steps it takes to reach 1       
    according to the rules of the Collatz Conjecture.'''
    
    if number < 1:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    
    #Count number of steps:
    count = 0
    
    while number > 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        count += 1

    return count 

```
