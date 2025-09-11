## September 10, 2025 - Day 33

### What I Worked On:  
Watched a lecture on Object Oriented Programming and took notes.

Problem 5: Playing a Hand, from Problem Set 3 from the MIT CS Class. I worked on the parts of the assignment as followed:
- Created the helper function calculate_handlen.
- Started writing out the process for playing the game, but did not finish 

Recursion:
- Worked with ChatGPT to practice some simple recursion problems.

### Concepts Practiced:  
- Dictionaries
- String Functions
- Recursion
           
### What I Found Challenging:  
- Still recursion. This is a difficult concept for me to grasp, but I'm getting better. 

### Key Accomplishments:  
- Finished half of Problem 5 from Problem Set 3.
    
### Resources Used:  
- [Problem Set 3](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps3/)
  
### Reflections/Insights:
I was tired tonight, so I didn't feel like fully doing the long process of figuring out the game in the problem set. Instead I focused on some weak areas I still have with recursion. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 3 Code: 
```python
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

#Small recursion functions:
def count_down(n):
    if n == 1:
        print(1)
        return
    print(n)
    count_down(n - 1)

def sum_up_to(n): 
  if n==1: 
    return 1 

  sum = n + sum_up_to(n-1) 
  return(sum)



```
