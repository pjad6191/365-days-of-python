## September 6, 2025 - Day 29

### What I Worked On:  
I worked on Problem 2: Dealing with Hands, from Problem Set 3 from the MIT CS Class. The assignment was as follows:
- The player starts with a full hand of n letters.
- As the player spells out words, letters from the set are used up. For example, the player could start with the following hand: a, q, l, m, u, i, l The player could choose to play the word quail. This would leave the following letters in the player's hand: l, m.
- Write a function that takes a hand and a word as inputs, uses letters from that hand to spell the word, and returns a new hand containing only the remaining letters.
- Your function should not modify the input hand.
  
### Concepts Practiced:  
- Dictionaries
- Loops
- Testing
- Debugging
- Exceptions
           
### What I Found Challenging:  
- This problem was also fairly easy. I didn't find it challenging. 

### Key Accomplishments:  
- Finished Problem #2 from Problem Set 3 
    
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
  
### Reflections/Insights:
Again, I tested each step as I went to make sure it was successful. I was checking to make sure of the following conditions:   
- If the player guesses a word that is invalid, either because it is not a real word or because they used letters that they don't actually have in their hand, they still lose the letters from their hand that they did guess as a penalty.
- Do not assume that the word you are given only uses letters that actually exist in the hand. If a letter was not in the hand to begin with, the guess will have no effect on the hand.
- Make sure the test_update_hand tests passes.
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 2 Code: 
```python

def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Make a copy of a new dictionary to return 
    new_hand = hand.copy()
    
    # Make sure word is all lowercase
    word = word.lower()
    
    # Cycle through each letter, and remove it from the new_hand
    for char in word:
        if new_hand.get(char, 0) >=1:
            new_hand[char] -= 1
            
    return new_hand
```
