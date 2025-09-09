## September 9, 2025 - Day 32

### What I Worked On:  
Problem 4, Part A: Permutations of a String, from Problem Set 4 from the MIT CS Class. The assignment was as follows:
- Write a recursive​ function get_permutations that takes a string and returns a list of all its permutations. You will find this function helpful later in the pset for part C. 
- Testing:​ Write three test cases for your function in comments under if __name__ == ‘__main__’ .
- Each test case should display the input and actual output. 
  
### Concepts Practiced:  
- Recursive functions
- String Functions
- Loops
- Testing
- Debugging
- Exceptions
           
### What I Found Challenging:  
- This is a hard concept for me. For some reason, recursive functions do not click well in my head. 

### Key Accomplishments:  
- Finished Part A from Problem Set 4.
    
### Resources Used:  
- [Problem Set 4](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/resources/ps4/)
  
### Reflections/Insights:
I took a day off from finishing problem 3 because I saw the recursive function assignment and knew it would be difficult for me. I am going to have to practice this concept. It does not come naturally, and will take some time for me to get it down. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Problem 4 Code: 
```python

# Problem Set 4A
# Name: Pamela Brown
# Time Spent: 1 hr

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    
    base = sequence[0]
    rest = sequence[1:]
    perms_without_first = get_permutations(rest)
    
    
    results = []
    for perm in perms_without_first:        #Loop through each permutation in perms without first
        for i in range(len(perm) + 1):      # Insert base into every possible position
            new_perm = perm[:i] + base + perm[i:]
            results.append(new_perm)
            
    return results

if __name__ == '__main__':
  sequence = 'abcd'
  print("Input:", sequence)
  print("Output:", get_permutations(sequence))

```
