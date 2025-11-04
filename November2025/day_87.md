## November 3, 2025 - Day 87

### What I Worked On:  
**Exercism:**
- Began a function to translate words into piglatin. I'm not finished with the whole program yet. I still need to adjust it to work for entire phrases. I will also add comments and a doc string to explain the function. 
 
### Concepts Practiced:  
- String functions 
- String manipulation
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def translate(text):
    
    #Make lowercase
    text = text.lower()
    vowels = "aeiou"
    # Rule 1
    rule1 = ("xr", "yt", "a", "e", "i", "o", "u")
    if text.startswith(rule1):
        piglatin = text + "ay"
        return piglatin
    
    # Rule 3
    if "qu" in text:
        qu_index = text.find("qu")
        
        # Check if before the 'q' are consonants (in a simple loop)
        only_consonants_before = True
        for char in text[:qu_index]:
            if char in vowels:  # if we find a vowel first, stop
                only_consonants_before = False
                break

        if only_consonants_before:
            piglatin = text[qu_index+2:] + text[:qu_index+2] + "ay"
            return piglatin
        
    # Rule 2 & 4
    rule2 = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
    if text.startswith(rule2):
        for index, char in enumerate(text):
            if char in vowels or (char == "y" and index > 0):
                piglatin = text[index:] + text[:index] + "ay"
                break
        return piglatin


```
