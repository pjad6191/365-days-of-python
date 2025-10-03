## October 2, 2025 - Day 55

### What I Worked On:  
Exercism - Practiced raising an exception

### Concepts Practiced:  
- Dictionaries
- Try and except
- Raise statements
- Handling errors
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def square(number):
    '''Calculates the number of grains of wheat on a chessboard.
    A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, 
    square 3 has four grains, and so on, doubling each time.
    This function returns the number of grains on a give square. 
    Assumes the number is between 1 and 64'''
    
    #Build a dictionary for the squares:    
    square_dict = {}
    square = 1
    for num in range(1,65):
        square_dict[num] = square
        square *=2

    try:
        return square_dict[number]
    except:
        # when the square value is not in the acceptable range        
        raise ValueError("square must be between 1 and 64")


def total():
    '''This function calculates the total number of grains on the chessboard'''
    total = 0
    for num in range(1,65):
        total += square(num)
    return total



```
