## September 8, 2025 - Day 31

### What I Worked On:  
Problem 4: Wildcards, from Problem Set 3 from the MIT CS Class. The assignment was as follows:
- Modify the deal_hand function to support always giving one wildcard in each hand. 
- Note that deal_hand currently ensures that one third of the letters are vowels and the rest are consonants. Leave the consonant count intact, and replace one of the vowel slots with the wildcard. 
- Modify the is_valid_word function to support wildcards. 
- Hint:​ Check to see what possible words can be formed by replacing the wildcard with other vowels. You may want to review the documentation for string module’s find() function and make note of its behavior when a character is not found. 
- Testing:​ Make sure the test_wildcard tests pass. You may also want to test your implementation with some reasonable inputs. 
  
### Concepts Practiced:  
- Dictionaries
- String Functions
- Loops
- Testing
- Debugging
- Exceptions
           
### What I Found Challenging:  
- I am aware of the use of wildcards, but it was a challenge to figure out how to handle this without using regex. 

### Key Accomplishments:  
- Finished Problem #4 from Problem Set 3.
    
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
  
### Reflections/Insights:
It took me a little while to deal with updating the valid word fuction just because I needed to figure out a way to do it using the skills taught in the class so far. I also forgot to update the score function to account for the *, which gets no points. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 3 Code: 
```python

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3), 
    and one card should be a wildcard, denoted by *. 

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    # Get the first key which is a vowel and delete to replace with *
    first_key = next(iter(hand))
    del hand[first_key]
    hand["*"] = 1
    
    return hand

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
        
        if char not in new_hand:  # Breaks loop if not in hand
            in_hand = False
            break
        if new_hand[char] == 0:   # Breaks loop if letter in hand has been used up
            in_hand = False
            break
        new_hand[char] -= 1     # Takes occurence of letter out of hand
    
                    
    # Checks to see if word is in the word list:

    # Initiate variables
    in_wordlist = False
    letter_list = []
    vowels = ["a", "e", "i", "o", "u"]
    matches = []
    
    # Checks to see if * is in the word
    if word.find("*") != -1: 
       for char in word:
            letter_list.append(char)
       for i in range(len(word)):
            if letter_list[i] == "*":
                for vowel in vowels:
                    letter_list[i] = vowel
                    match = "".join(letter_list)
                    matches.append(match)
       
       for match in matches:
          if match in word_list:
              in_wordlist = True
              break
   
    # If * is not in word            
    else:
       if word in word_list:
           in_wordlist = True
    

    # Returns true only if both are true
    if (in_hand == True) and (in_wordlist == True):
        return True
    else:
        return False

```
