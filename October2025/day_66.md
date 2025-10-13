## October 13, 2025 - Day 66

### What I Worked On:  
Exercism:
- Worked on a set of functions that look up the numerical value associated with a particular color band and lists the different band colors.
- Added an additional function that will return a two-digit number. 

### Concepts Practiced:  
- Lists
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def color_code(color):
    '''This function looks up the index of the color in order to get the numerical        value associated with a particular color band
    param: str (color)
    return: int (index number) 
    '''
    return colors().index(color)


#Holds the colors for the previous function
def colors():
    '''This function stores the colors associated with the index numbers
    return: list
    '''
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return colors


#One function to return two digit numbers 
def value(colors):
    '''This function will take color names as input and output a two digit number. 
    param: list of colors
    return: int
    '''
    
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    #Get each index
    number1 = str(colors_list.index(colors[0]))
    number2 = str(colors_list.index(colors[1]))

    #Return combination of numbers as an int
    return int(number1+number2)
    
```
