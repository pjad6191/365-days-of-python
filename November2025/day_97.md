## November 13, 2025 - Day 97

### What I Worked On:  
**Exercism:**  
Today's function was a lot easier compared to yesterday. I immediately knew what I needed to do, which was nice compared to the last couple of days. I created a function that returns a proverb given a list of inputs. The code did require an additional keyword argument (qualifier) which would modify the final verse of the proverb.
 
### Concepts Practiced:  
- Unpacking lists of arbitrary lengths
- Optional parameters
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def proverb(*items, qualifier=None):
    """
    Given a list of inputs, the function will generate the relevant proverb.
    """

    rhyme = []
    
    if not items:
        return []
           
    #Body of rhyme
    for i in range(len(items)-1):
        rhyme.append(f"For want of a {items[i]} the {items[i+1]} was lost.")
      
    #Last line
    if qualifier:
        rhyme.append(f"And all for the want of a {qualifier} {items[0]}.")
    else:
        rhyme.append(f"And all for the want of a {items[0]}.")
    
    return rhyme 
```
