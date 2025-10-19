## October 18, 2025 - Day 71

### What I Worked On:  
Exercism:  
I did not feel like doing anything complicated tonight. I am tired and want a break, so I just did a simple function to calculate a Scrabble score.  

### Concepts Practiced:  
- Dictionaries
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def score(word):
    score_dict = {"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "R":1, "S":1, "T":1, "D":2, "G":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, "K":5, "J":8, "X":8, "Q":10, "Z":10}

    #Capitalize every letter to utilize dictionary 
    word = word.upper()

    #Initialize score variable
    score = 0

    #Loop through letters in the word
    for char in word:
        score += score_dict[char]

    return score

```
