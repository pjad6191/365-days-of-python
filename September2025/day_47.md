## September 24, 2025 - Day 47

### What I Worked On:  
Continued to work on Exercism with simple functions for Black Jack. Also picked back up on Google's Advanced Data Analytics Python course. I finished a lab on Pandas and started writing the project documentation for the Python course's final project.  

Something I like about Exercism is that it evaluates your code and tells you where you can improve. I feel like I have learned how to write cleaner code and have been getting better scores and feedback as time goes on, so it's been helpful to work on these exercises, even though they are more simple than what I have been practicing. 

### Concepts Practiced:  
- Comparisons
- List Methods
- Pandas
- Writing clean minimal code
          
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Google's Advanced Data Analytics Python Course](https://www.coursera.org/learn/get-started-with-python/home)
    
### Exercism Code: 
```python
"""Functions for tracking poker hands and assorted card tasks.
Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds_list = [number, number+1, number+2]
    return rounds_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    new_list = rounds_1 + rounds_2
    return new_list
    

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    avg = (hand[0]+hand[-1])/2
    middle = hand[len(hand) // 2]
    if avg == card_average(hand) or middle == card_average(hand):
        return True
    return False 


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    odd_list = hand[::2]
    even_list = hand[1::2]
    odd_avg = sum(odd_list) / len(odd_list)
    even_avg = sum(even_list) / len(even_list)
    return odd_avg == even_avg


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
      
```
