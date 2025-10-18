## October 17, 2025 - Day 70

### What I Worked On:  
Exercism:  
Tonight I worked on one function that took a binary number and converted each digit into an action for a secret handshake. the binary number is read from right to left. I didn't want to assume that the user would input a string of numbers that would only contain five digits, so I created commands to read the number from right to left no matter what the length of the string was. 

### Concepts Practiced:  
- List methods
- Sequences
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

def commands(binary_str):
    '''This function coverts each digit in a binary number 
    to an action for a handshake. 
    The binary number is read from right to left.
    
    param: str (binary number in the form of a string)
    return: list (series of actions for the handshake)
    '''

    #List of handshake actions
    action_list = ["jump", "close your eyes", "double blink", "wink"]
    
    #Create the handshake list of actions to return
    handshake_list = []   
    
    #Initialize variable to access action_list index
    list_count = 3
    
    #Loop through binary string
    for num in range(len(binary_str)-1, len(binary_str)-5, -1):
        if binary_str[num] == '1':  #Only add if it's equal to one
            handshake_list.append(action_list[list_count])
        list_count-=1

    #Reverse list if necessary
    if binary_str[len(binary_str)-5] == '1':
        handshake_list.reverse()

    return handshake_list
```
