## September 21, 2025 - Day 44

### What I Worked On:  
This was THE easiest exercise from Exercism, but at least my streak is continuing. I am going to be gone for most of the day and don't know if I'll have time to do anything else. So I'm submitting this, and if it turns out I have more time and energy tonight, I will do something a little more substanstial. 

### Concepts Practiced:  
- String methods
- Creating clean minimal code
          
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python
"""Functions to help edit essay homework using string manipulation."""

def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    return title.title()


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip(" ")


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    return sentence.replace(old_word, new_word)
  
```
