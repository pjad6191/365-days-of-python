## October 5, 2025 - Day 58

### What I Worked On:  
Exercism - Interesting to learn about Nicomachus' (60 - 120 CE) classification scheme for positive integers. Created a function to classify numbers based on his scheme. 

### Concepts Practiced:  
- Conditionals
- Error statements
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number > 0:
        factor_list = []
        for digit in range(1, number):
            if number % digit == 0:
                factor_list.append(digit)
            total = sum(factor_list)        
        if total == number:
            return "perfect"
            if total > number:
                return "abundant"
        return "deficient"

    raise ValueError("Classification is only possible for positive integers.")
    
    

```
