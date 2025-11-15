## November 15, 2025 - Day 99

### What I Worked On:  
**Exercism:**  
I created an implementation of the Atbash cipher, an ancient encryption system created in the Middle East. There are two functions, one to encode and the other to decode. 

Also, I'm on day 99! Almost to 100. It's been a journey! 
 
### Concepts Practiced:  
- String manipulation
- String cleaning
- Dictionaries
- Loops
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
import string

def encode(plain_text):
    """
    This function creates an implementation of the Atbash ciper. 
    Param: str (string to be encoded)
    Returns: str (encoded text) 
    """
    
    #Ensure lowercase
    plain_text = plain_text.lower()

    #Get a list of punctuation
    punc = list(string.punctuation)
    
    #Remove spaces and punctuation
    clean_text = ""
    for char in plain_text:
        if char == " " or char in punc:
            clean_text += ""
        else:
            clean_text += char
            
    #Get alphabet
    alpha = string.ascii_lowercase
    
    #Reverse alphabet
    reverse =  alpha[::-1]

    #Create dictionary for cipher
    cipher = {}
    for index, char in enumerate(alpha):
        cipher[char] = reverse[index]
    
    #Encode the text
    ciphered_text = ""
    for index, char in enumerate(clean_text):
        if char.isalpha():
            if index%5 == 0 and index >=5: 
                ciphered_text += " " + cipher[char]
            else: 
                ciphered_text += cipher[char]
        else:
            if index%5 == 0:
                ciphered_text += " " + char 
            else: 
                ciphered_text += char
                
    return ciphered_text



def decode(ciphered_text):
    """
    This function decodes text that has been encoded using the Atbash ciper. 
    Param: str (string to be decoded)
    Returns: str (decoded text) 
    """
    
    #Ensure lowercase
    ciphered_text = ciphered_text.lower() 
    
    #Remove spaces
    no_spaces = ""
    for char in ciphered_text:
        if char == " ":
            no_spaces += ""
        else:
            no_spaces += char
    
    #Get alphabet
    alpha = string.ascii_lowercase
    
    #Reverse alphabet
    reverse =  alpha[::-1]

    #Create dictionary for reverse cipher
    reverse_cipher = {}
    for index, char in enumerate(reverse):
        reverse_cipher[char] = alpha[index]
    
    #Encode the text
    plain_text = ""
    for char in no_spaces:
        if char.isalpha():
            plain_text += reverse_cipher[char]
        else:
            plain_text += char
            
    return plain_text


```
