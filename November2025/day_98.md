## November 14, 2025 - Day 98

### What I Worked On:  
**Exercism:**  
Today I got into the holiday season by creating a function that returned the lyrics of *The Twelve Days of Christmas*. It was fairly straightforward and not that difficult. It was just enough for me today as I was not in the programming mood. 
 
### Concepts Practiced:  
- Lists
- Loops
- Conditionals 
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:

def recite(start_verse, end_verse):
"""This function returns the lyrics of the song The Twelve Days of Christmas."""

    days = ["first", 
            "second", 
            "third", 
            "fourth", 
            "fifth", 
            "sixth", 
            "seventh", 
            "eighth", 
            "ninth", 
            "tenth", 
            "eleventh", 
            "twelfth"]
    
    gifts = ["a Partridge in a Pear Tree.", 
             "two Turtle Doves", 
             "three French Hens", 
             "four Calling Birds",
             "five Gold Rings",
             "six Geese-a-Laying", 
             "seven Swans-a-Swimming", 
             "eight Maids-a-Milking", 
             "nine Ladies Dancing", 
             "ten Lords-a-Leaping", 
             "eleven Pipers Piping", 
             "twelve Drummers Drumming"]
    
    song = []
    
    for day in range(start_verse, end_verse + 1):
        new_line = f"On the {days[day-1]} day of Christmas my true love gave to me: "
        
        if day == 1:
            new_line += gifts[0]
        else:
            lines = []
            for num in range(day - 1, 0, -1):
                lines.append(gifts[num])
            
            new_line += ", ".join(lines) + ", and " + gifts[0]
        
        song.append(new_line)
        
    return song
        

```
