## November 11, 2025 - Day 95

### What I Worked On:  
**Exercism:**  
I created a function to compress a string of numbers. I have no idea why I got hung up on this function but it took me forever. There was a hiccup in my head for some reason. There is another part to the Exercism exercise, but I didn't get to it today, because the first part took me so long. It was really simple too. Live and learn I guess. I also didn't get to anything else today, which was disappointing because I wanted to cover more on my day off. I may still work on more, but I wanted to write down what I did accomplish before midnight so that I don't miss a day of activity. 
 
### Concepts Practiced:  
- Loops
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def decode(string):
    if not string:
        return ""

    compressed = ""
    count = 1

    #Loop through string starting with the second character
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed += str(count) + string[i - 1]
            count = 1

    compressed += str(count) + string[-1]
    return compressed

```
