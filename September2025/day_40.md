## September 17, 2025 - Day 40

### What I Worked On:  
I worked on Problem Set 4, Part C: Substitution Ciper, Part 1: SubMessage:
- setter method: _ _ init _ _(self, text)
- the getter methods
  - get_message_text(self)
  - get_valid_words(self)
- build_transpose_dict(self, vowels_permutation)
- apply_transpose(self, transpose_dict) 

### Concepts Practiced:  
Object-Oriented Programming (OOP)
- Creating and using classes (SubMessage)
- Defining and using instance attributes (self.message_text, self.valid_words)
- Writing getter methods to access private data safely

Python Dictionaries
- Building mappings between letters (vowel transposition)
- Merging dictionaries with {**dict1, **dict2}

String Manipulation
- Checking if a character is a letter (char.isalpha())
- Changing case with .upper() and .lower()

Code Style Best Practices
- Avoiding the use of built-in names like dict
- Returning copies to avoid accidental mutation
          
### Resources Used:  
- [Problem Set 4](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps4/)
    
### Problem 4c Code: 
```python
class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        # Get uppercase vowel permutation:
        upper_vowel_permutation = vowels_permutation.upper()
        
        # Make lowercase vowel dictionary
        lower_vowels_dict = {}
        for i in range(len(VOWELS_LOWER)):
            lower_vowels_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
                
        # Make uppercase vowel dictionary 
        upper_vowels_dict = {}
        for i in range(len(VOWELS_UPPER)):
            upper_vowels_dict[VOWELS_UPPER[i]] = upper_vowel_permutation[i]
            
        # Join vowel dictionaries
        vowel_dict = {**lower_vowels_dict, **upper_vowels_dict}
            
        # Join consonants strings
        consonants =  CONSONANTS_LOWER + CONSONANTS_UPPER
        
        # Make consonants dictionary
        consonant_dict = {}
        for char in consonants:
            consonant_dict[char] = char
            
        # Add vowels and consonants dictionaries together:
        dictionary = {**vowel_dict, **consonant_dict}
        
        return dictionary
        
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_text = ''
        for char in self.message_text:
            if char.isalpha():
                encrypted_text += transpose_dict[char]
            else:
                encrypted_text += char   
            
        return encrypted_text
     
```
