## November 2, 2025 - Day 86

### What I Worked On:  
**Exercism:**
- Completed a function to find the square root of a number without using the math libray

**Introduction to Computational Thinking and Data Science:**
- Began the first problem set
  
### Concepts Practiced:  
- Numbers
- Reading a file 
- String methods
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Problem Set 1](https://ocw.mit.edu/courses/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/resources/ps1/)
  
### Code: 
```python
#Exercism Code:
def square_root(number):
    '''
    This function finds the square root of a number without using the pre-existing math library.
    '''
    #Dealing with 0 and 1:
    if number == 0:
        return 0
    if number == 1:
        return 1

    #Loop through list 
    guess = 2
    for num in range(2, number//2):
        if num*num == number:
            guess = num
            break
    
    return guess

#Problem Set 1 (Introduction to Computational Thinking and Data Science):
#Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #Initialize a dictionary to return
    cow_dict = {}
    
    #Opens the file, reads it, and closes it
    with open(filename, 'r') as cows:
        for line in cows:
            #Separate the words by comma
            words = line.split(",")
            
            #Get cow name
            name = words[0].strip()
            
            #Get cow weight
            weight = int(words[1].strip())
            
            #Add to dictionary
            cow_dict[name] = weight
       
    return cow_dict

```
