## September 22, 2025 - Day 45

### What I Worked On:  
I was correct that I would not have any more time yesterday. Today I'm crawling from being so busy yesterday, so the agenda was the same - to practice something simple using Exercism. 

### Concepts Practiced:  
- String methods
- Creating clean minimal code
          
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un"+word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    string = vocab_words[0]
    for i in range(1, len(vocab_words)):
        string += " "+"::" + " " + vocab_words[0] + vocab_words[i]
        
    return string 
        

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    word = word[:-4]
    if word[-1] == "i":
        word = word.strip("i")
        word += "y"
    return word

 
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    sentence = sentence[:-1]
    wordlist = sentence.split()
    wordlist[index] += "en"
       
    return wordlist[index]
    
    

  
```
