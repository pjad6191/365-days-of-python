## October 22, 2025 - Day 75

### What I Worked On:  
**Exercism:**  
I created a function to conduct a binary search. I remember this being covered in the class I did, but it was a different challenge figuring it out on my own, since I didn't remember all the details of the program covered in class. I'm not sure that I did it in the most efficient way, but it works. 

### Concepts Practiced:  
- Binary Search 
- Loops
- Handling errors
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
def find(search_list, value):
    '''
    This function uses a binary search to search for an item in a list.
    param: list, int
    return: int (the index number of the item in the list)
    '''

    #Handle empty list
    if len(search_list) == 0:
        raise ValueError("value not in array")

    #If only one correct value in the list:
    if search_list[0] == value:
        return 0
    
    #Initialize start and end of search array
    min = 0
    max = len(search_list)

    #Define search area:
    search_area = search_list[min:max]
    
    #Find middle point
    middle_point = len(search_area)//2
    
    while len(search_area) > 1:
        #Get guess to compare to value
        guess = search_area[middle_point]
        
        if guess == value:
            break
            
        elif guess < value:
            min = middle_point
            max = len(search_area)
            
        else:
            min = 0
            max = middle_point
        
        #Define new search area:
        search_area = search_area[min:max]
        print(search_area)
    
        #Define new middle point:
        middle_point = len(search_area)//2

    #Return values
    if guess == value:
        return search_list.index(guess)
    else:
        raise ValueError("value not in array")

```
