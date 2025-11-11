## November 10, 2025 - Day 94

### What I Worked On:  
**Exercism:**  
I created a function to count the number of 1 bits the binary representation of a number. We were not allowed to use the bit-count functionality provided in the standard library. 

**Neural Data Science:**  
I watched the next video in the Neural Data Science class. I learned about the glob module which I had not come across before. You can use glob.glob to find sets of files whose names match a pattern.  

If sets of files have similar filenames, you can use it to loop through and process batches of files or to append files to single DataFrame. I can see how this would be helpful in dealing with large amounts of data. We did an exercise were we read in data from multiple experimental participants. We created a list of DataFrames, and then combined them all into one DataFrame. This was cool to me because the whole reason I am interested in Python is to use it for scientific purposes.
 
### Concepts Practiced:  
- binary numbers 
- pandas
- glob
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Neural Data Science](https://neuraldatascience.io)
  
### Code: 
```python
#Exercism Code:
def egg_count(display_value):
    """
    This function counts the number of 1 bits in a binary representation of a number
    """
    
    #Initialize count of bits
    count = 0 

    while display_value > 0:
        if display_value%2 == 1:
            count += 1
        display_value = display_value//2
    
    return count



#Example pandas code:
#Read in data from multiple experimental participants
filenames = glob.glob('data/s?.csv')
filenames = sorted.filenames

#Add to a list 
df_list = []
for f in filenames:
  df_list.append(pd.read_csv(f))

#Read using list comprehension
df_list = [pd.read_csv(f) for f in filenames]

#Combine the DataFrames
df = pd.concat(df_list)

#Set the index column
df = df.set_index('participantID') 

```
