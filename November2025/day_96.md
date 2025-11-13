## November 12, 2025 - Day 96

### What I Worked On:  
**Exercism:**  
I finished functions that implemented run-length encoding and decoding. Run-length encoding (RLE) is a simple form of data compression, where runs (consecutive data elements) are replaced by just one data value and count. Decoding reverses the operation. For something that seemed relatively simple, it tripped me up. It took me far longer than i was comfortable with. Glad those are over though. 
 
### Concepts Practiced:  
- Iteration
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
  
### Code: 
```python
#Exercism Code:
def decode(string):  
    if not string:
        return ""
    
    decode = ""
    count = ""
    
    for i in range(len(string)):
        if string[i].isnumeric():
            count += string[i]              
        else:
            if count == "":
                decode += string[i]
            else:
                decode += string[i] * int(count)
                count = ""                  
                
    return decode


def encode(string):
    if not string:
        return ""
    
    encode = ""
    count = 1

    #Loop through string starting with the second character
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            if count > 1:
                encode += str(count) 
            encode += string[i - 1]
            count = 1  
    if count > 1:
        encode += str(count)
    encode += string[-1]
    
    return encode
```
