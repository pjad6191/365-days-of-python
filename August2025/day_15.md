## August 23, 2025 - Day 15

### What I Worked On:  
- Pandas with ChatGPT

### Concepts Practiced:  
- **Pandas DataFrames**: 
    - Mapping
    - Masking
       
### What I Found Challenging:  
- Still doing great with just the right amount of challenge. I had not fully understood masking before, but I get it now with ChatGPT. It's either because I'm getting a lot more comfortable with Pandas or because ChatGPT explains it well. 

### Key Accomplishments:  
- Better understand mapping and masking 
    
### Resources Used:  
- **ChatGPT**

### Reflections/Insights:
-  Pandas is getting easier for me. I feel like I will be readu to really analyze, breakdown, and transform large datasets soon. That is what I'm working toward. 
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing Pandas with ChatGPT. 

### Example Code: 
```python

#Creating a new column mapping Grades to Feedback:
table["feedback"] = table["grade"].map({"A":"Excellent", "B":"Good", "C":"Needs Work"})

#Using mask to replace ages under 9 with "Too Young":
table["age"] = table["age"].mask(table["age"] <9, "Too Young")

```

