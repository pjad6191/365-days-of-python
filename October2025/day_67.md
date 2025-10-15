## October 14, 2025 - Day 67

### What I Worked On:  
Exercism:
- Worked on a function that looks up the numerical value associated with two particular color bands as well as the number of zeros that should be added to the number. It then returns a string with the correct units. The name of the unit changes according to the size of the number, for example ohms vs. kiloohms.

### Concepts Practiced:  
- List Methods
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def label(colors):
    '''This function will take color names as input and 
    output a string number with units. 
    
    param: list of colors
    return: str
    '''
    
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    #Get each index
    number1 = str(colors_list.index(colors[0]))
    number2 = str(colors_list.index(colors[1]))

    #Create 2 digit number:
    num = int(number1+number2)
    
    #Get num of zeros based on third color in list
    zeros = colors_list.index(colors[2])

    #Create full number based on zeros
    fullnum = num * (10**zeros)

    #Format return strings considering suffixes 
    if zeros >= 8:
        return_string = str(int(fullnum/(1*10**9))) + " gigaohms"
    elif zeros >= 5:
        return_string = str(int(fullnum/(1*10**6))) + " megaohms"
    elif zeros >= 2:
        return_string = str(int(fullnum/(1*10**3))) + " kiloohms"
    else:
        return_string = str(fullnum) + " ohms"
        
    return return_string
```
