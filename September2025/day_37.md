## September 14, 2025 - Day 3

### What I Worked On:  
- Worked on Problem 3, Substitute_ hand function

### Concepts Practiced:  
- Functions & parameters
- Conditional statements
- Copying data structures
- Dictionaries
- String methods
- Random module
- List operations
          
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
    
### Problem 3 Code: 
```python
def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    # Make a string of all letters
    string_letters = string.ascii_lowercase
    letter_list = []
    
    for char in string_letters:
        if char not in hand:
            letter_list.append(char)
                   
    if letter not in hand:
       return hand
       
    else: 
        # Find out how many times letter occurs in hand
        num_letter = hand[letter]
        
        new_hand = hand.copy()
        del new_hand[letter]
               
        # Choose a random letter
        newletter = random.choice(letter_list)
    
        #Add new letter to the hand
        new_hand[newletter] = num_letter
                
        return new_hand

```
