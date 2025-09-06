## September 5, 2025 - Day 28

### What I Worked On:  
- I worked on Problem 1: Word Scores from Problem Set 3 from the MIT CS Class. The objective was to implement a function that calculates the score for a single word. The score for a word is the product of two components:
-   the sum of the point for letters in the word
-   either [7 * word_length - 3 * (n-word_length)] or 1, whichever value is greater, where:
  - word_length is the number of letters used in the word
  - n is the number of letters available in the current hand
- We are to use the scrabble_letter_values dictionary that was defined at the top of the program outline
  
### Concepts Practiced:  
- Dictionaries
- Loops
- Testing
- Debugging
- Exceptions
- Creating a program with multiple functions 
           
### What I Found Challenging:  
- This problem was that bad. I didn't find it that challenging

### Key Accomplishments:  
- Finished Problem #1 from Problem Set 3 
    
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
  
### Reflections/Insights:
- For this problem, I tested each step as I went to make sure it was successful. I used the print statement a lot to make sure that I was getting the intended results. The assignment had us test the function with a test code to see if it was successful, and my function passed. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 1 Code: 
```python
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	  The score for a word is the product of two components:

  	The first component is the sum of the points for letters in the word.
	  The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	  Letters are scored as in Scrabble; A is worth 1, B is
	  worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    # Make sure all the letters are lowercase
    lc_word = word.lower()


    # Separate the word into individual letters
    letter_list = []
    for char in lc_word:
        letter_list.append(char)
        
    # FIRST COMPONENT   
        
    # Initiate variable for first component score
    score1 = 0

    # Go through each letter in the list 
    for char in letter_list:
        #get the score by using the letter from the list as the key
        letter_value = SCRABBLE_LETTER_VALUES[char]
        #add it to score1
        score1 += letter_value


    # SECOND COMPONENT

    # Get word length
    word_length = len(lc_word)

          
    # Formula for second component
    formula = 7 * word_length - 3 * (n-word_length)

    # Initialize variable for second component score
    score2 = 1 

    # Check to see if formula is greater
    if formula > 1:
        score2 = formula

    # Final score
    word_score = score1 * score2
    
    return word_score
```
