# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Pamela Brown
# Time spent    : 10 hours

import math
import random
import string


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words1.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
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

    #Separate the word into individual letters
    letter_list = []
    for char in lc_word:
        letter_list.append(char)
        
    # FIRST COMPONENT   
        
    #initiate variable for first component score
    score1 = 0

    #Go through each letter in the list 
    for char in letter_list:
        #get the score by using the letter from the list as the key
        letter_value = SCRABBLE_LETTER_VALUES[char]
        #add it to score1
        score1 += letter_value

    # SECOND COMPONENT
    #get word length
    word_length = len(lc_word)
          
    #formula for second component
    formula = 7 * word_length - 3 * (n-word_length)

    #initialize variable for second component score
    score2 = 1 

    # Check to see if formula is greater
    if formula > 1:
        score2 = formula

    # Final score 
    word_score = score1 * score2
    
    return word_score
        

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print("Current hand: ", end='')
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


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

#
# Problem #2: Update a hand by removing letters
#
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

#
# Problem #3: Test word validity
#
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
                       
    # Checks to see if word is in the word list 
        in_wordlist = False
    letter_list = []
    vowels = ["a", "e", "i", "o", "u"]
    matches = []
        
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
                
    else:
       if word in word_list:
           in_wordlist = True
    

    # Returns true only if both are true
    if (in_hand == True) and (in_wordlist == True):
        return True
    else:
        return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    
    letterSum = 0
    for value in hand.values():
        letterSum += value

    return letterSum


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
                print("")
            
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("That is not a valid word. Please choose another word.") 
                
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    
    print(f"Total score for this hand:{total_score}")
    print("------------------")
    
        
    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

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
 
       
    num_of_hands = int(input("Enter total number of hands: "))
    hand_count = 1
    
    # Initialize total score:
    total_score = 0 
    
    # Initialize replay variable: 
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

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)













