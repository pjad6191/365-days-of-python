## November 9, 2025 - Day 93

### What I Worked On:  
**Exercism:**  
I worked on a function to convert numbers from Arabic numerals to Roman numerals. 

**Neural Data Science:**  
I finally got my computer all set up to deal with the assignments for this class. It was mainly about being able to use templates from github and then being able to clone repositories on my computer to be able to work with the data and files. It seemed simple enough, but there was one hiccup after another. I then watched the video on working with pandas, and did the exercises for that chapter in a jupyter notebook. 
 
### Concepts Practiced:  
- Conditionals 
- pandas 
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Neural Data Science](https://neuraldatascience.io)
  
### Code: 
```python
#Exercism Code:
def roman(number):
    """
    This function coverts a number from Arabic numerals to Roman numers. 
    Only deals with numbers up to 3999.
    Param: int
    Return: str
    """
    
    #Make number a string to manipulate digits
    str_num = str(number)
    
    #Reverse so that you deal with the smallest numbers first
    reverse = str_num[::-1]   
    
    #Initialize return string
    rom_num = "" 
    
    
    #First Digit 
    if len(str_num) >=1:
        num = int(reverse[0])
        if num <= 3:
            digit = num*"I"
        if num == 4:
            digit = "IV"
        if num == 5:
            digit = "V"
        if num >= 6 and num <9:
            digit = "V" + (num-5)*"I"
        if num == 9:
            digit = "IX"
        rom_num = digit
        
    
    #Second Digit 
    if len(str_num) >=2:
        num = int(reverse[1])
        if num <= 3:
            digit = num*"X"
        if num == 4:
            digit = "XL"
        if num == 5:
            digit = "L"
        if num >= 6 and num <9:
            digit = "L" + (num-5)*"X"
        if num == 9:
            digit = "XC"
        rom_num = digit + rom_num
    
    #Third Digit
    if len(str_num) >=3:
        num = int(reverse[2])
        if num <= 3:
            digit = num*"C"
        if num == 4:
            digit = "CD"
        if num == 5:
            digit = "D"
        if num >= 6 and num <9:
            digit = "D" + (num-5)*"C"
        if num == 9:
            digit = "CM"
        rom_num = digit + rom_num
    
    #Fourth Digit
    if len(str_num) ==4:
        num = int(reverse[3])
        if num <= 3:
            digit = num*"M"    
        rom_num = digit + rom_num
    
    return rom_num




```
