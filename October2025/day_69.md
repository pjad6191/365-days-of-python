## October 16, 2025 - Day 69

### What I Worked On:  
Exercism:  
Tonight I worked on a couple of biology related functions which was very fun for me. Besides practicing Python, I love studying biology and neuroscience. These functions allowed me to connect it all. 

### Concepts Practiced:  
- Generating expressions
- Raising and handling errors
- Sequences
         
### Resources Used:  
- [Exercism.org](https://exercism.org/tracks/python/exercises)
    
### Exercism Code: 
```python

def distance(strand_a, strand_b):
    '''This function compares two single strands of DNA / RNA and 
    returns the Hamming distance (the number of differences between
    the strands)
    param: 2 strings 
    return: int
    '''
    
    # When the sequences being passed are not the same length.
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    # Account for variations in uppercase 
    strand_a = strand_a.upper()
    strand_b = strand_b.upper()
    
    count = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            count+=1
    return count

def proteins(strand):
    '''This function takes an RNA strand (string) and 
    translates the codons in the strand to the corresponding amino acid.
    It also takes into account any STOP codons to stop reading the string. 
    
    param: string (RNA strand)
    return: list (containing the amino acids) 
    '''

    #Define the codons:
    codons = {
        "AUG":"Methionine", 
        "UUU":"Phenylalanine", 
        "UUC":"Phenylalanine", 
        "UUA":"Leucine", 
        "UUG":"Leucine", 
        "UCU":"Serine",
        "UCC":"Serine",
        "UCA":"Serine",
        "UCG":"Serine",
        "UAU":"Tyrosine", 
        "UAC":"Tyrosine", 
        "UGU":"Cysteine", 
        "UGC":"Cysteine", 
        "UGG":"Tryptophan",
        "UAA":"STOP", 
        "UAG":"STOP", 
        "UGA":"STOP"}

    #Initialize variables
    cursor=0
    amino_list= []

    while cursor < len(strand):
        #Get the codon
        codon=strand[cursor:cursor+3]
    
        #Get the amino acid that correaltes to that codon
        amino=codons[codon]

        #Check for a STOP codon
        if amino == "STOP":
            break
    
        #Add the amino acid to the list
        amino_list.append(amino)
    
        #Move the cursor to where the next codon starts
        cursor+=3
    
    return amino_list
```
