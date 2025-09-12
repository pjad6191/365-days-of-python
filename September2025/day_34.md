## September 10, 2025 - Day 34

### What I Worked On:  
Today I focused on building a deeper understanding of recursion, which I’ve found especially challenging. I practiced writing some very simple recursive functions from scratch to help the idea “click” more clearly. 
  
### Concepts Practiced:  
- Base cases and recursive calls
- Stack frames and tracing recursive logic
- Writing recursive functions for math problems
- Debugging and testing with print() statements
           
### What I Found Challenging:  
- I still find recursion a little abstract. It’s hard to “see” what’s happening unless I either draw it out or add print() calls to follow the logic. I sometimes mix up when to return and when to call again. I'm also working on not defaulting to loops and trusting the recursive structure more.

### Key Accomplishments:  
- Wrote 3+ basic recursive functions.
    
### Resources Used:  
- Python Tutor for visualizing recursion
  
### Reflections/Insights:
Working on small, non-intimidating recursion problems made a huge difference. Instead of getting stuck on the harder ones, building from the basics gave me confidence and showed me I’m capable of understanding recursion. It just takes repetition and smaller steps. 
  
### Next Steps/Plans for Tomorrow: 
- Continue with the MIT class online. 

### Recursion Code: 
```python

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

```
