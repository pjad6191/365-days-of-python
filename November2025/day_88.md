## November 4, 2025 - Day 88

### What I Worked On:  
**Exercism:**
- Finished the Pig Latin code from yesterday. Added a function to translate phrases and not just single words. I also added comments and docstrings to explain the functions.
 
### Concepts Practiced:  
- String functions 
- String manipulation
- Conditionals
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def translate_words(text):
    """
    Convert a single English word to Pig Latin based on the four rules:
    Rules Applied:
    1. If a word starts with a vowel, "xr", or "yt", simply add "ay" to the end.
    2. If a word begins with consonants, move those consonants to the end,
       then add "ay".
    3. If a word contains "qu" after optional starting consonants, move the
       consonant(s) + "qu" to the end, then add "ay".
    4. If a word has consonants followed by "y", move those consonants to
       the end, then add "ay".

    Param: text(str) - A single word to translate.
    Returns: str - The translated Pig Latin word.
    """
    # Make lowercase so rules apply consistently
    text = text.lower()
    vowels = "aeiou"
    
    # Rule 1: Word starts with vowel or special cases "xr" / "yt"
    rule1 = ("xr", "yt", "a", "e", "i", "o", "u")
    if text.startswith(rule1):
        piglatin = text + "ay"
        return piglatin
    
    # Rule 3: Handle "qu" pattern (zero or more consonants before it)
    if "qu" in text:
        qu_index = text.find("qu")
        
        # Check if characters before "qu" are consonants only
        only_consonants_before = True
        for char in text[:qu_index]:
            if char in vowels:
                only_consonants_before = False
                break

        # If valid "qu" situation, rearrange according to Rule 3
        if only_consonants_before:
            piglatin = text[qu_index+2:] + text[:qu_index+2] + "ay"
            return piglatin
        
    # Rule 2 & Rule 4: Starts with consonants (including handling "y" in special location)
    rule2 = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")
    if text.startswith(rule2):
        # Find where the vowel (or special-case 'y') appears
        for index, char in enumerate(text):
            # Stop moving consonants when we hit a vowel
            # OR a 'y' that is not in the first position → Rule 4 case
            if char in vowels or (char == "y" and index > 0):
                piglatin = text[index:] + text[:index] + "ay"
                break
        return piglatin


def translate(text):
    """
    Translate a full phrase into Pig Latin by processing each word.
    Param: text(str) - A phrase containing one or more words.
    Returns: str - The phrase translated into Pig Latin.
    """

    # Split the sentence into individual words
    word_list = text.split()

    # Translate each word using translate_words()
    translated_words = []
    for word in word_list:
        # Translate each word separately
        translated_words.append(translate_words(word))

    # Rejoin into full sentence
    return " ".join(translated_words)

     



```
