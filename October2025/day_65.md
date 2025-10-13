## October 12, 2025 - Day 65

### What I Worked On:  
Exercism:
- Worked on a simple function to create an complementary RNA strand given a DNA template. 
- Worked on a function to return a ciphertext based on the Caesar Cipher. 

### Concepts Practiced:  
- String Methods
- Dictionaries
- Writing clean minimal code
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

def to_rna(dna_strand):
    '''Given a DNA strand, determine the RNA complement.
    param: str
    return: str'''

    complement = ""
    for char in dna_strand:
        if char == "G":
            complement += "C"
        if char == "C":
            complement += "G"
        if char == "T":
            complement += "A"
        if char == "A":
            complement += "U"
    return complement
            

import string

def rotate(text, key):
    '''Create an implementation of the Caesar cipher. 
    The Caesar cipher transposes all the letters in the alphabet 
    using an integer key between 0 and 26. 
    
    param: str (text to be turned into a cipher
        int (key) 
    return: str (ciphered text) 
    
    '''
    #Create strings of alphabet
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase

    #Create strings that have been shifted by the key
    lowercase_shift = lowercase[key:] + lowercase[:key]
    uppercase_shift = uppercase[key:] + uppercase[:key]

    #Create a dictionary to create a cipher for lowercase letters        
    lower_dict = {}
    for index, char in enumerate(lowercase):
        lower_dict[char] = lowercase_shift[index]

    #Create a dictionary to create a cipher for lowercase letters  
    upper_dict = {}
    for index, char in enumerate(uppercase):
        upper_dict[char] = uppercase_shift[index]

    #Join the dictionaries
    cipher_dict = lower_dict | upper_dict

    #Create the cypher text
    cipher_text = ""
    for char in text:
        if char.isalpha():
            cipher_text += cipher_dict[char]
        else:
            cipher_text += char
        
    return cipher_text

```
