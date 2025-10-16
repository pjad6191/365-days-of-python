## October 15, 2025 - Day 68

### What I Worked On:  
Exercism:  
Worked on a function that was an extension of yesterday's function dealing with resistance bands. This one was a little harder due to the formatting. I got a little stuck on how to keep the decimals of the numbers at the end. I looked up ways to strip what I didn't need in the return string and finally got everything correct. It was not hard to deal with the tolerance or adding another couple bands. 

### Concepts Practiced:  
- List Methods
- Dictionaries
- Formatting strings
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

def resistor_label(colors):
    '''
    Takes a list of resistor color bands and returns the resistance value
    as a formatted string with the proper unit and tolerance.

    Supports:
    - 1-band resistors (black only → 0 ohms)
    - 4-band resistors (value1, value2, multiplier, tolerance)
    - 5-band resistors (value1, value2, value3, multiplier, tolerance)

    Returns values in ohms, kiloohms, or megaohms with tolerance (e.g. "2.54 megaohms ±1%").

    param: list of colors
    return: str
    '''
    
    #Create the colors list
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    #Create the tolerance dictionary
    tolerance_dict = {"grey":"0.05%", "violet":"0.1%", "blue":"0.25%", "green":"0.5%", "brown":"1%", "red":"2%", "gold":"5%", "silver":"10%"}
        
    #Handle different band lengths:
    if len(colors) == 1:
        return "0 ohms"
     
    #Get each index
    num = ""
    for col in range(len(colors)-2):
            num+=str(colors_list.index(colors[col]))
       
    #How many zeros to multiply by
    zeros = 10**colors_list.index(colors[-2])
    
    #Get tolerance
    tolerance = "±" + tolerance_dict[colors[-1]]
    
    #Get resistance
    fullnum = int(num)*zeros
    
    #Considering suffixes 
    if fullnum >= 1000000:
        val = fullnum / 1000000
        unit = "megaohms"
    elif fullnum >= 1000:
        val = fullnum/1000
        unit = "kiloohms"
    else:
        val = fullnum
        unit = "ohms"

    #Format return strings to keep the decimals
    return_str = f"{val:.2f}".rstrip("0").rstrip(".")
    return f"{return_str} {unit} {tolerance}"
```
