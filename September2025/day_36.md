## September 13, 2025 - Day 36

### What I Worked On:  
- Watched a lecture on Python Classes and Inhertance and took notes.
- Finished and tested Problem 5: Playing a Hand, from Problem Set 3 from the MIT CS Class. 

### Concepts Practiced:  
- Dictionaries
- String Functions
- Control Flow 
- Function calls
- Debugging
          
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
    
### Problem 3 Code: 
```python
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
     """

    # Keep track of the total score
    total_score = 0
    
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand)>0:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        word = input("Enter word, or \"!!\" to indicate that you are finished: ")
        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not two exclamation points):
        elif word != "!!":    
            
            # If the word is valid:
            if is_valid_word(word, hand, word_list) == True:
                # Tell the user how many points the word earned,
                # and the updated total score
                word_score = get_word_score(word, HAND_SIZE)
                total_score += word_score
                print(f'\"{word}\" earned {word_score} points')
            
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.") 
                
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    
    print(f"Total score:{total_score}")
        
    # Return the total score as result of function
    return total_score

```
