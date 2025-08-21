## August 20, 2025 - Day 12

### What I Worked On:  
- Pandas with ChatGPT

### Concepts Practiced:  
- **Pandas DataFrames**: Sorting & Filtering, Adding Columns
       
### What I Found Challenging:  
- It was not particularly challenging today. Just the right amount of challenge to help me grow. 

### Key Accomplishments:  
- Started to feel more confident and like I knew what I was doing with filtering and conditionals. While I'm comfortable with Python, the syntax for Pandas was initially throwing me off. 
    
### Resources Used:  
- **ChatGPT**

### Reflections/Insights:
- I think I definitely have filtering down. I had ChatGPT give me a lot of difference scenarios to practice, and I was nailing the syntax. It used to confuse me, but I think I have it. We then worked on adding columns that would add True/False values based on conditions. I still made small mistakes here and there but I'm getting better.
  
### Next Steps/Plans for Tomorrow: 
- Continue practicing Pandas with ChatGPT. 

### Example Code: 
```python

table["honor_roll"] = (table["grade"] == "A") & (table["age"] < 11)
table.loc[table["honor_roll"] == True, ["name", "age"]]

```

