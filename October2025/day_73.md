## October 20, 2025 - Day 73

### What I Worked On:  
I finally finished up Problem Set 4 from Introduction to Computer Science and Programming in Python. It took me forever to remember what I did with the rest of the problem, but after reviewing, it didn't take that long to put the rest together. The full code for part C can be found here: September2025/Assignments/ps4/ps4c.py

### Concepts Practiced:  
- Classes and inheritance
- Dictionaries
- String manipulation
- Testing and debugging
         
### Resources Used:  
- [Problem Set 4](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps4/)
    
### Problem Set 4, Part C Code: 
```python

class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text) 
        

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        #Defaults to the orginal text if nothing else is better 
        best_message = self.message_text 
        max_valid_words = 0

        for perm in get_permutations(VOWELS_LOWER):
            transpose_dict = self.build_transpose_dict(perm)
            candidate = self.apply_transpose(transpose_dict)

            # count valid words in this candidate
            count = 0
            for word in candidate.split():
                if is_word(self.valid_words, word):
                    count += 1

            if count > max_valid_words:
                max_valid_words = count
                best_message = candidate

        return best_message

```
