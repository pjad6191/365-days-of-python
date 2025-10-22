## October 21, 2025 - Day 74

### What I Worked On:  
**Exercism:**  
I created a function that built the rhyme "This is the House that Jack Built" which was harder for me than I thought. I didn't create a recursive function but I used concepts of recursion.  

### Concepts Practiced:  
- Recursive methods
- Loops
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def recite(start_verse, end_verse):
    '''This function recites the nursery rhyme This is the House that Jack Built. It takes two parameters which are integers which give the starting verse and ending verse lines numbers.'''
    
    #Store the parts of the rhyme
    pieces = [
      "the house that Jack built.",
      "the malt that lay in ",
      "the rat that ate ",
      "the cat that killed ",
      "the dog that worried ", 
      "the cow with the crumpled horn that tossed ", 
      "the maiden all forlorn that milked ",
      "the man all tattered and torn that kissed ",
      "the priest all shaven and shorn that married ", 
      "the rooster that crowed in the morn that woke ", 
      "the farmer sowing his corn that kept ",
      "the horse and the hound and the horn that belonged to "
      ]

    #Initialize the list 
    verses = []

    #Outer loop to add verses to list 
    for verse_num in range(start_verse, end_verse + 1):
        rhyme = "This is "
        #Inner loop to build the lines
        for i in range(verse_num - 1, -1, -1):
            rhyme += pieces[i]
        verses.append(rhyme)

    return verses
```
