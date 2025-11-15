## November 15, 2025 - Day 99

### What I Worked On:  
**Exercism:**  
I created an implementation of the Atbash cipher, an ancient encryption system created in the Middle East. There are two functions, one to encode and the other to decode. 

**Neural Data Science:**
I worked on exercises involving reaction time data, looking at accuracy, and removing outliers. 

Also, I'm on day 99! Almost to 100. It's been a journey! 
 
### Concepts Practiced:  
- String manipulation and cleaning
- Dictionaries
- Loops
- List manipulation
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
- [Neural Data Science](https://neuraldatascience.io/)
  
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



#Example Neural Data Science Code
rt = [0.394252808, 0.442094359, 0.534764366, 0.565906723, 0.570404592, 
      0.486154719, 0.518792127, 0.844916827, 0.495622859, 0.476159436, 
      0.612854746, 0.529661203, 0.389157455, 1.517088266, 0.573962432, 
      0.714152493, 0.409225638, 0.435308188, 0.509801957, 0.544626271, 
      0.437877745, 0.333356848, 0.401773569, 0.479840688
      ]

err = [False, False, True, False, False, False, False, False, True, False, 
       False, True, False, False, False, False, True, True, True, False, 
       ]

#Insert values into err
err.insert(0, True)
err.extend([False, False, False])

#Find the position of the slower RT in the data
slowest_index = rt.index(slowest)

#Removes the slowest RT value 
rt.remove(max(rt))

#Removes the corresponding err value 
err.pop(slowest_index) 

#Print the slowest RT remaining, rounded to decimal places
print("Slowest RT", round(max(rt), 2))

#Check the length of both lists
print(f"Length of rt: {len(rt)} and length of err: {len(err)}")

```
