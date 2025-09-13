## September 12, 2025 - Day 35

### What I Worked On:  
Problem Set 4, Part B: Cipher Like Caesar (Part 1: Message) 
This part works on created a cipher to encrypt messages. To quote the assignment: "The idea of the Caesar Cipher is to pick an integer and shift every letter of your message by that integer. In other words, suppose the shift is k. Then, all instances of the "i"th letter of the alphabet that appear in the plaintext should become the (i + k)th letter of the alphabet in the ciphertext. You will need to be careful with the case in which i + k > 26 (the length of the alphabet). We will treat uppercase and lowercase letters individually, so that uppercase letters are always mapped to an uppercase letter, and lowercase letters are always mapped to a lowercase letter. If an uppercase letter maps to “A”, then the same lowercase letter should map to “a”. Punctuation and spaces should be retained and not changed. For example, a plaintext message with a comma should have a 
corresponding ciphertext with a comma in the same position. 

Part B is broken up into three additional parts. I worked on the first part today which was as follows:
We have provided skeleton code in the Message class for the following functions - your task is to implement them. Please see the docstring comment with each function for more information about the function specification. 
-  \_\_init\_\_(self, text)
- The getter methods:
  - get_message_text(self) (Note: This should return an immutable version of the message text we added to this object in init. Luckily, strings are already immutable objects, so we can simply return that string. 
  - get_valid_words(self) (Note: this should return a COPY of self.valid_words to prevent someone from accidentally mutating the original list.)
  - build_shift_dict(self, shift) (Note: you may find the string ​​ module’s ascii_lowercase constant helpful here.)
  - apply_shift(self, shift) Hint: use build_shift_dict(self, shift). Remember that spaces and punctuation should not be changed by the cipher.
  
### Concepts Practiced:  
- Classes & Objects
- Inheritance
- Encapsulation
- String Manipulation
- Dictionaries
           
### What I Found Challenging:  
- Understanding self as the object. I don't always know when I should include ".self" 

### Key Accomplishments:  
- Finished Part A of the second part of Problem Set 4
    
### Resources Used:  
- [Problem Set 4](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps4/)
  
### Reflections/Insights:
I didn't think I was going to get to all of this today, but once I got going, it was easy to continue. The functions themselves were not hard. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 4 Code: 
```python

# Problem Set 4B, Part 1
# Name: Pamela Brown
# Time Spent: 1.25 hrs

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
       
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        shiftlower = ""
        shiftupper = ""

        for i in range(len(lowercase)):
            shifted_index = (i + shift) % 26
            shiftlower = shiftlower + lowercase[shifted_index]
        for i in range(len(uppercase)):
            shifted_index = (i + shift) % 26
            shiftupper = shiftupper + uppercase[shifted_index]

        lowerdict = {}
        for i in range(len(lowercase)):
            lowerdict[lowercase[i]] = shiftlower[i]
            
        upperdict = {}
        for i in range(len(uppercase)):
            upperdict[uppercase[i]] = shiftupper[i] 
            
        combined_dict = {**lowerdict, **upperdict}
        
        return combined_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        cipher_message = ""
        for char in self.message_text:
            if char.isalpha():
                cipher_message += shift_dict[char]
            else:
                cipher_message += char
        
        return cipher_message

```
