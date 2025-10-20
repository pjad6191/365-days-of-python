## October 19, 2025 - Day 72

### What I Worked On:  
**Exercism:**  
I did a fairly simple function that took a word and a list of words and checked if any words in the list were anagrams of the single word. 

### Concepts Practiced:  
- List Methods
- Strings
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

def find_anagrams(word, candidates):
    '''This function take a word and compares it a list of candidates to see if any of the candidates are anagrams of the original word. Returns a list of the anagram words.
    param: string, list of strings
    return: list of strings'''
    
    #Make word all lowercase
    word = word.lower()
    
    #Create an empty list to create a copy of all lowercase words
    cand_copy = []
    
    #Make words in list all lowercase
    for entry in candidates:
        cand_copy.append(entry.lower())
        
    #Create a list of letters and sort them in alphabetical order 
    word_letters = list(word)
    word_letters.sort()

    #Initialize a return list
    candidate_list = []
    
    #Loop through candidate list
    #Create a sorted letter list of each and compare to initial word
    for index, entry in enumerate(cand_copy):
        if entry == word:
            continue
        else:
            cand_letters = list(entry)
            cand_letters.sort()
            if cand_letters == word_letters: 
                candidate_list.append(candidates[index]) 
       
    return candidate_list
        

```
