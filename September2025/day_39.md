## September 16, 2025 - Day 39

### What I Worked On:  
- Watched Lecture 10: Understanding Programming Efficiency, Part 1 and took notes
- Read Chapter 9 
- I finished Part B of Problem Set 4 -Cipher Like Caesar. I worked on 2 - 4 to finish it up. 
- The entire Part B for Problem Set 4 can be found here: [PS4 - Part B](https://github.com/pjad6191/365-days-of-python/blob/main/September2025/Assignments/ps4/ps4b.py)

### Concepts Practiced:  
Caesar Cipher / Cryptography Basics:
- Understanding how shifting letters encrypts/decrypts messages
- Brute-force decryption by trying all 26 shifts
- Evaluating which shift makes the most valid words

Loops and Control Flow
- for loops to try every shift
- Conditional logic (if, >=) to track the best result
- Resetting counters inside a loop

Working with Strings
- Splitting strings into words with .split()
- Rebuilding messages character-by-character
- Using helper functions like is_word() to check word validity

Code Reuse and Efficiency
- Avoiding repetition by reusing existing methods
- Returning copies of data to prevent accidental changes (.copy())
          
### Resources Used:  
- [Problem Set 4](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps4/)
- [Introduction to Computation and Programming Using Python]
- [Lecture 10: Understanding Program Efficiency, Part 1]
    
### Problem 4 Code from today: 
```python
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message.__init__(self, text) 
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift) 

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.message_text_encrypted = self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object         
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text) 

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the 
        best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        # Initialize variables
        best_shift = 0
        max_valid = 0
                
        #Loop through every possible combination 
        for i in range(26):
            count = 0
            decrypted = self.apply_shift(i)
            
            #split the string apart using spaces 
            split = decrypted.split()
                        
            for word in split:
                if is_word(self.valid_words, word):
                    count += 1            
            
            if count >= max_valid:
                max_valid = count
                best_shift = i
                    
        message = self.apply_shift(best_shift)       
        
        return(best_shift, message)
        
        
        

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage("let's go!", 5)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage("qjy'x lt!")
    print('Expected Output:', (21, "let's go!"))
    print('Actual Output:', ciphertext.decrypt_message())

    # Best shift value and unencrypted story 
    story = get_story_string()
    cipher_story = CiphertextMessage(story)
    print(cipher_story.decrypt_message())

```
