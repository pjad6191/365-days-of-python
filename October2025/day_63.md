## October 10, 2025 - Day 63

### What I Worked On:  
Exercism - Worked on a simple function dealing with scoring for darts. This was easy and quick, which is good because my kids are coming home for fall break today! 

### Concepts Practiced:  
- Conditionals
- Comparisons
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def score(x, y):
    '''This function take two coordinates which determine the location of a dart on a dart board and returns the score. 
    If dart lands outside the target - 0 points
    If dart lands in the outer circle - 1 point
    If dart lands in the middle circle - 5 points
    If dart lands in the inner circle - 10 points
    Outer circle - radius 10 
    Middle circle - radius 5
    Inner circle - radius 1

    param: 2 int 
    return int
    '''
    #Determine the distance based on Pythagorean theorem 
    line = (x**2 + y**2)**.5

    #Determine score
    if line <= 1:
        return 10
    if line >1 and line<=5:
        return 5
    if line>5 and line<=10:
        return 1
    return 0 
  
```
