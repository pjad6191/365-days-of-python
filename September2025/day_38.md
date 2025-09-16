## September 15, 2025 - Day 38

### What I Worked On:  
- Worked on the last part of Problem 3 - Playing the game. I finally finished it too. Problem Set 3 is done!
- The entire game for Problem Set 3 can be found here: [PS3](https://github.com/pjad6191/365-days-of-python/blob/main/September2025/Assignments/ps3/ps3.py)

### Concepts Practiced:  
- Working with functions
- String handling
- Using dictionaries 
- Random choices
- Loops (while, for) to repeat actions until done
- Conditionals (if, else) for checking valid words, substitutions, replay
- Copying data (using .copy() so replay works right)
- Scoring and keeping totals
- Game logic design (substitution rule, replay rule, ending conditions)
- Debugging (catching where rules didn’t match your code)
          
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
    
### Problem 3 Code: 
```python
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # Get num of hands to play
    num_of_hands = int(input("Enter total number of hands: "))

    # Initialize variables:
    total_score = 0
    hand_count = 1
    replay_used = False
    
    while num_of_hands > 0:
        
        # Deal and display hand
        print(f"Hand #{hand_count}")
        hand = deal_hand(HAND_SIZE)
        original_hand = hand.copy()
        display_hand(hand)
        
        # Deal with possible letter substitution:
        answer = input("Would you like to substitute a letter? yes or no: ")
        answer = answer.lower()
        if answer == "yes":
            letter = input("What letter would you like to replace? ")
            hand = substitute_hand(hand, letter)
        print("")
        
        # Play a hand
        score = play_hand(hand, word_list)
        print("")
    
        # Replay hand? 
        if not replay_used: 
            replay_question = input("Would you like to replay the hand? yes or no: ") 
            print("")
            if replay_question.lower() == "yes": 
                score2 = play_hand(original_hand, word_list) 
                score = max(score, score2) 
                replay_used = True
        
        # Update
        total_score +=score
        num_of_hands -= 1
        hand_count += 1
                    
    print("Total score over all hands: ", total_score)
    
```
