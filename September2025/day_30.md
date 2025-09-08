## September 7, 2025 - Day 30

### What I Worked On:  
Problem 3: Valid Words, from Problem Set 3 from the MIT CS Class. The assignment was as follows:
- Implement the is_valid_word function according to its specifications.
- A valid word is in the word list (we ignore the case of words here) and​ it is composed entirely of letters from the current hand. 
- Make sure the test_is_valid_word tests pass. You should also test your implementation with some reasonable inputs. In particular, you may want to test your implementation by calling it multiple times on the same hand.
  
### Concepts Practiced:  
- Dictionaries
- Loops
- Testing
- Debugging
- Exceptions
           
### What I Found Challenging:  
- I had initially forgot to account for if the word had two of the same letters but the hand didn't.

### Key Accomplishments:  
- Finished Problem #3 from Problem Set 3 and completed 30 days of consistent Python practice.
    
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
  
### Reflections/Insights:
I'm gaining more confidence in my abilities. This problem set has gone smoothly so far. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 3 Code: 
```python

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
      
    # Account for any capital letters
    word = word.lower()
    
    # Make a new hand to alter so that one letter isn't used more than once in the hand 
    new_hand = hand.copy()

    # Initialize in_hand variable to be True
    in_hand = True
        
    for char in word:  # Loops through each char
        if char not in new_hand:  # Makes in_hand = False and breaks loop if not in hand
            in_hand = False
            break
        if new_hand[char] == 0:   # Makes in_hand = False and breaks loop if letter in hand has been used up
            in_hand = False
            break
        new_hand[char] -= 1     # Takes occurence of letter out of hand
                    
    # Checks to see if word is in the word list 
    in_wordlist = word in word_list
    
    # Returns true only if both are true
    if (in_hand == True) and (in_wordlist == True):
        return True
    else:
        return False

```
