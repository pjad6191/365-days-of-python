## November 8, 2025 - Day 92

### What I Worked On:  
**Exercism:**  
I worked on a function to compute the prime factors of a number. This took me longer than expected. It's an easy thing to do on my own, but a little harder to think through an algorithm for it. Also, I didn't want to have to store large lists and wanted to keep in mind the time it would take for the function to run with large numbers.  
 
### Concepts Practiced:  
- Mathematical concepts
- Memory management (avoiding storing large lists)
- Algorithm optimization
- Dealing with possible large numbers
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def isprime(num):
    if num < 2:
        return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def factors(value):
    """
    This function computes the prime factors of a given natural number
    Param: int
    Return: list of int
    """
    
    if value < 2:
        return []
    
    if isprime(value):
        return [value]
    
    factors = []
    divisee = value
    
    #Takes out all 2s to account for all even numbers
    while divisee%2 == 0:
        factors.append(2)
        divisee //= 2  
        
    #Takes out all odd numbers starting at 3
    divisor = 3
    #Only need to go up to sqrt(divisee)
    while divisor * divisor <= divisee:
        while divisee % divisor == 0:
            factors.append(divisor)
            divisee //= divisor
        divisor += 2  # next odd number
        
    #If there is anything left to the divisee, it must be prime
    if divisee > 1:
        factors.append(divisee)
            
    return factors


```
